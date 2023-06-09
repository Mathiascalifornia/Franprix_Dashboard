import plotly.express as px 
import pandas as pd

### Fonctions servant à renvoyer différents graphiques ### 


def scatter_plot(df : pd.DataFrame , X : str , y : str , title : str , color='blue'):
    ''' Nuage de points '''

    fig = px.scatter(data_frame=df , x=X , y=y , color_discrete_sequence=[color])

    # Définir le titre du graphique centré
    fig.update_layout(
    title={
        'text': title,
        'x': 0.5,  # Centrer horizontalement
        'y': 0.95,  # Centrer verticalement
        'xanchor': 'center',
        'yanchor': 'top'
    })
    return fig



def line_plot(df : pd.DataFrame , y : str , X : str , title : str , color='blue'):
    ''' Une simple ligne '''

    fig = px.line(data_frame=df , x=X , y=y)
    
    fig.update_traces(line_color=color)

    # Définir le titre du graphique centré
    fig.update_layout(
    title={
        'text': title,
        'x': 0.5,  # Centrer horizontalement
        'y': 0.95,  # Centrer verticalement
        'xanchor': 'center',
        'yanchor': 'top'
    })


    return fig



def bar_plot(df : pd.DataFrame , X : str , y : str , title : str):
    ''' Graphique en barre '''

    fig = px.bar(df, x=X, y=y)
    fig.update_traces(marker_line_color='black', marker_line_width=1)
    
    # Définir le titre du graphique centré
    fig.update_layout(
    title={
        'text': title,
        'x': 0.5,  # Centrer horizontalement
        'y': 0.95,  # Centrer verticalement
        'xanchor': 'center',
        'yanchor': 'top'
    })

    return fig