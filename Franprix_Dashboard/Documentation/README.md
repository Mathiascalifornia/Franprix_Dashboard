# Analyse Franprix

## Méthodologie

Pour ce projet j'ai un jeu de donnée comptable de franprix , s'étendant de fin 2007 à fin 2021.
Ces données , tel quel , n'était pas exploitable , aussi ais-je récupéré les données qui m'intéressait avec excel , et les ais-je 
séparé en trois jeux de données différents : un sur les actifs , un sur les passifs , et un sur les chiffres clés.

Ce projet a été codé en python , avec la librairie Dash pour la partie Web-application , plotly pour les graphiques interactifs ,
et tkinter pour l'interface utilisateur , permettant de passer d'une catégorie à une autre.

## Utilisation 

Pour utiliser cette application , suivez ces étapes :
- Ouvrez le dossier FRANPRIX_DASHBOARD avec votre IDE
- Executer la commande suivante dans votre terminal : pip install -r requirements.txt . Cela installera tout les modules et dépendances nécessaires.
- Executer le fichier 'main.py'
- Choisissez une catégorie 
- Cliquer sur le bouton "Lancer l'analyse" , un navigateur s'ouvrira avec votre Dashboard.
- Vous pouvez ouvrir plusieurs Dashboard différents en même temps , cela ne fera pas planter l'application.