#PDLData

Ce projet a pour but d'utiliser les données de la région Pays de la Loire concernant l'ensemble des activités et complexes de loisirs disponibles sur le territoire régional.

## Fonctionnement

Le projet fonctionne en utilisant un serveur python (bottle) et en utilisant une base de données SQL. La base de donnée est complétée à l'aide de fichiers CSV.

### Lancement du site

Pour télécharger le dépôt PDLData :

> git clone https://github.com/babastienne/PDLdata.git

Ensuite, aller dans le dossier PDLData et lancer le site internet :

> cd PDLdata/
> python3 server.py

Vous pouvez à présent accéder au site internet via l'adresse http://localhost:8080/

### Création de la base de donnée

La base de données nommée 'PDLData.db' est disponible au chemin suivant : ./architecture/db/PDLData.db
La base de données est créée à partir de 3 fichiers csv disponible au chemin suivant : ./data/\*.csv

Note : Les fichiers csv utilisés sont disponibles via l'API de la région à l'adresse suivante :
- Installations : http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-installations/
- Activites : http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-activites-des-fiches-equ/
- Equipements : http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-equipements/

Si la BD est manquante ou que vous souhaitez l'avez supprimée, vous pouvez la recréer à l'aide de la commande suivante :

> cd /architecture/db/
> python3 Application.py

## Problèmes potentiels

Pour le bon fonctionnement du projet, l'utilisateur doit posséder SQLite3 sur son PC. Le projet utilise également des ressources Javascript potentiellement non compatibles avec certains navigateurs web (anciennes version de IE notamment).

Les bibliothèques Bottle, JQuery ainsi que Semantic sont incorporées au projet. En cas de suppression de celles-ci le programme ne pourra fonctionner correctement.

## Credits

Ce projet a été créé par binome à l'IUT de Nantes en 2016 dans le cadre du module 'Technologies pour la production de logiciels'. 
