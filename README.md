#PDLData

This project use the open data of the 'Pays de la Loire' state which concern the all activities and entertainment complexes available in the regional territory.

## How it works

This project works with a python server (Bottle library) et use a SQL database. The database is build from the three CSV files which represent the data of the region. 

### Launch the website

For clone the PDLData repository :

> git clone https://github.com/babastienne/PDLdata.git

Then, go to the PDLData repostory and launch the server :

> cd PDLdata/
> python3 server.py

You can now access to the website at this adress : http://localhost:8080/

### Creation of the database from CSV files.

The database is called 'PDLData.db' and is available at the path : ./architecture/db/PDLData.db
The database is build from 3 CSV files availables at this path : ./data/\*.csv

Tips : The CSV files used are available at the following adress (it's the open data of the region) :
- Installations : http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-installations/
- Activites : http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-activites-des-fiches-equ/
- Equipements : http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-equipements/

If the database is missing or you want to delete it, you can recreate the it with the following commands :

> cd /architecture/db/
> python3 Application.py

## Potential problems

For the proper functioning of the project, the user must have SQLite3 on his PC. The project also uses potentially incompatible Javascript resources with some web browsers (older versions of IE in particular).

Bottle libraries, JQuery and Semantic are incorporated in the project. If deleting them the program can't work properly.

## Credits

This project was created at the Nantes IUT of IT in 2016 for the module 'Technologies for Software Production'. 
