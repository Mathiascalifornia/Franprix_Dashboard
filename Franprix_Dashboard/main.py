# Dash 
import dash
from dash import dcc
from dash import html

# Visualisation et manipulation de données
import plotly.express as px
import pandas as pd
from fonctions import *

# Threading et gestion de ports
from threading import Timer
import webbrowser
from threading import Thread

# GUI
from tkinter import *
from tkinter import ttk



### Création des applications ###

class AppPassif:

    """ Cette classe retourne une application Dash , avec des graphiques intéractifs sur les passifs de Franprix. """

    def __init__(self):
        self.df = pd.read_csv('data/passif.csv')
        self.app = dash.Dash(__name__) # Instantier l'application
        self.app.layout = html.Div([

            # Le titre de l'application
            html.H1(children=['-------------------------------------------------------    Analyse des passifs    -------------------------------------------------------'],
                    style={'border': '1px solid black'}),


            # Les graphiques
            dcc.Graph(figure=line_plot(df=self.df, y="Fonds propres", X='date', title="Fonds propres (bleu) vs Dette (rouge) par année") \
                      .add_trace(line_plot(df=self.df, y='Dettes', X='date',
                                           title="Fonds propres vs Dette par année", color='red').data[0])),

            dcc.Graph(figure=scatter_plot(df=self.df, y="Total du passif", X='date', title="Total du passif par année")),

            dcc.Graph(figure=bar_plot(df=self.df, y="Provisions pour risques et charges", X='date',
                                      title="Provisions pour risques et charges par année"))
        ])


    def run(self):
        ''' Cette méthode lance l'application sur le port local spécifié '''
        self.app.run_server(port=8051)  # Utiliser un port différent des deux autres applis





class AppActif:

    """ Cette classe retourne une application Dash , avec des graphiques intéractifs sur les actifs de Franprix. """

    def __init__(self):
        self.df = pd.read_csv('data/actif.csv')
        self.app = dash.Dash(__name__) # Instantier l'application
        self.app.layout = html.Div([

            # Le titre de l'application
            html.H1(children=['-------------------------------------------------------    Analyse des actifs    -------------------------------------------------------'],
                    style={'border': '1px solid black'}),

            # Les graphiques
            dcc.Graph(figure=line_plot(df=self.df, y="Total de l'actif", X='date',
                                       title="Total de l'actif (bleu) vs actifs circulants nets (rouge) par année") \
                      .add_trace(line_plot(df=self.df, y=".Autres actifs circulants nets", X='date',
                                           
                                           title="", color='red').data[0])),
            dcc.Graph(figure=scatter_plot(df=self.df, y="Actif immobilisé net", X='date', title="Actif immobilisé net par année")),

            dcc.Graph(figure=bar_plot(df=self.df, y='.Stocks nets', X='date', title="Stocks nets par année")),
        ])

    def run(self):
        ''' Cette méthode lance l'application sur le port local spécifié '''
        self.app.run_server(port=8052)  # Utiliser un port différent des deux autres applis





class AppChiffreClef:

    """ Cette classe retourne une application Dash , avec des graphiques intéractifs sur les chiffres clefs de Franprix. """

    def __init__(self):
        self.df = pd.read_csv('data/chiffre_clef.csv')
        self.app = dash.Dash(__name__) # Instantier l'application
        self.app.layout = html.Div([

            # Le titre de l'application
            html.H1(children=['--------------------------------------------------   Analyse des chiffres clés   --------------------------------------------------'],
                    style={'border': '1px solid black'}),

            # Les graphiques
            dcc.Graph(figure=line_plot(df=self.df, y="Endettement (%)", X='date',
                                       title="Endettement (bleu) vs Rentabilité nette (rouge) par année") \
                      .add_trace(line_plot(df=self.df, y='Rentabilité nette (%)', X='date',
                                           title="", color='red').data[0])),

            dcc.Graph(figure=scatter_plot(self.df, 'date', 'Effectif moyen du personnel',
                                          title='Effectif moyen du personnel par année')),

            dcc.Graph(figure=line_plot(self.df, X='date', y='Fonds de roulement net global',
                                       title="Fonds de roulement (bleu) et Capacité d'autofinancement (rouge)") \
                      .add_bar(y=self.df["Capacité d'autofinanc. avant répartition"], x=self.df['date']).update_traces(
                showlegend=False, selector=dict(type='bar')))


        ])


    def run(self):
        ''' Cette méthode lance l'application sur le port local spécifié '''
        self.app.run_server(port=8053)  # Utiliser un port différent des deux autres applis




### Création de l'interface graphique ###

def run_dash(input_):
    ''' Cette fonction a pour vocation de récupérer la bonne application , puis à l'éxécuter à l'intérieur d'une Thread (au sein de la fonction run_app)'''
    app = dictio_cat_appli.get(input_)
    app.run()




def open_browser(port):
    ''' 
    Cette fonction permet d'ouvrir automatiquement
    un navigateur web avec l'URL du serveur local en utilisant le numéro de port spécifié. 
    Cela facilite l'accès à l'application web exécutée localement.
    '''
    webbrowser.open_new(f'http://127.0.0.1:{port}/')


def run_app():
    '''
    Cette fonction est le callback du bouton de la fenêtre tkinter. 
    Elle récupère l'input utilisateur et lance l'application dans une Thread.
    La Thread sert à éviter à la fenêtre tkinter de crasher à chaque clique , en 
    garantissant une éxecution indépendante d'une appli à l'autre.
    '''
    input_ = language.get()

    # Lancer l'application Dash dans un thread séparé
    t = Thread(target=run_dash, args=(input_,))
    t.start()

    # Ouvrir le navigateur après un court délai
    Timer(1, lambda: open_browser(8051 if input_ == "Passifs" else 8052 if input_ == "Actifs" else 8053)).start()


### Constantes ###
categories = ["Chiffres clés", 'Actifs', "Passifs"]
applis = [AppChiffreClef(), AppActif(), AppPassif()]
dictio_cat_appli = dict(zip(categories, applis)) # Lier les deux listes au dessus dans un dictionnaire



root = Tk() # Initialisation de la fenêtre
root.title('Analyse Franprix') # Le titre de la fenêtre

label = Label(root, text="Choisissez la catégorie que vous voulez analyser").pack() # Texte au dessus du dropdown
language = ttk.Combobox(root, values=categories, width=40) # Dropdown , l'utilisateur doit choisir une valeur dans la liste de choix proposés
language.pack() # Les widget doivent être packer séparements
button = Button(root, text="Lancer l'analyse", command=run_app, width=36, height=0, borderwidth=4).pack() # Création du bouton , lié à la fonction run_app




root.mainloop() # Boucle infini de la fenêtre tkinter , qui ne s'arrêtera que si on clique sur la croix de fermeture

