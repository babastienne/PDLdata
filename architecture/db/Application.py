from ExtractCSV import *
from DataClass import DataClass

""" Creation of the database from the csv files.
	This file call ExtractCSV.py wich call Dao.py
	ex : For add installations in the database
	- we create a list of lists wich contain the data names and types. Here it's attributInstallation
	- we create dataClass wich contain the list created, the path to the csv file corresponding and the name of the table (for the database)
	- We create the database and then we add the data to the table in the database (with the exctractCSV file)

	The main avantage of this contruction is the use of the generic class : dataClass. We can add any csv file with this procedure
	and we don't have to create the class corresponding. """


# In the lists below we give the name of each row of the csv file and the type of data corresponding
attributEquipement = [["ComInsee","int"], ["ComLib","int"], ["InsNumeroInstall","int"], ["InsNom","varchar(255)"], ["EquipementId","int"], ["EquNom","varchar(255)"], ["EquGpsX","varchar(255)"],["EquGpsY","varchar(255)"]]
attributActivity = [["ComInsee","int"],["ComLib","varchar(255)"],["EquipementId","int"],["EquNbEquIdentique","varchar(255)"],["ActCode","int"],["ActLib","varchar(255)"]]
attributInstallation = [["Nom usuel de l'installation","varchar(255)"],["Numéro de l'installation","int"],["Nom de la commune","varchar(255)"],["Code INSEE","int"],["Code postal","int"],["Nom du lieu dit","varchar(255)"],["Numero de la voie","int"],["Nom de la voie","varchar(255)"],["location","varchar(255)"],["Longitude","varchar(255)"],["Latitude","varchar(255)"],["Aucun aménagement d'accessibilité","varchar(255)"]]

# Each object DataClass as the path to csv file corresponding, the name of the table in the database and the type of informations on it (name of each row for the table).
dataInstallation = DataClass("../../data/installations.csv", "installations", attributInstallation)
dataActivity = DataClass("../../data/activites.csv", "activity", attributActivity)
dataEquipement = DataClass("../../data/equipements.csv", "equipements", attributEquipement)

# we create an object of the ExtractCSV type which will be the actraction of each csv file.
# This object will also add the data in a dataBase by using the Dao class
csv = ExtractCSV()

csv.createTables(dataActivity)
csv.addDataBase(dataActivity)

csv.createTables(dataInstallation)
csv.addDataBase(dataInstallation)

csv.createTables(dataEquipement)
csv.addDataBase(dataEquipement)
