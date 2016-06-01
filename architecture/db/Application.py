from CreateFromCSV import CreateFromCSV
from Data import Data
#Application qui met en relation les différentes classes Data, CreateFromCSV et Dao

""" Création des différents Data
	ex : Pour enregistrer une installations
	- on va chercher les informations dans le fichier installations.csv
	- on stock les informations dans la table installations de la base de données
	- les différents attributs sont précisés dans attributsInstallation """


attributsEquipement = [["ComInsee","int"], ["ComLib","int"], ["InsNumeroInstall","int"], ["InsNom","varchar(255)"], ["EquipementId","int"], ["EquNom","varchar(255)"], ["EquGpsX","varchar(255)"],["EquGpsY","varchar(255)"]]
attributsActivite = [["ComInsee","int"],["ComLib","varchar(255)"],["EquipementId","int"],["EquNbEquIdentique","varchar(255)"],["ActCode","int"],["ActLib","varchar(255)"]]
attributsInstallation = [["Nom usuel de l'installation","varchar(255)"],["Numéro de l'installation","int"],["Nom de la commune","varchar(255)"],["Code INSEE","int"],["Code postal","int"],["Nom du lieu dit","varchar(255)"],["Numero de la voie","int"],["Nom de la voie","varchar(255)"],["location","varchar(255)"],["Longitude","varchar(255)"],["Latitude","varchar(255)"],["Aucun aménagement d'accessibilité","varchar(255)"]]

dataEquipement = Data("../../donnees/equipements.csv", "equipements", attributsEquipement)
dataActivite = Data("../../donnees/activites.csv", "activites", attributsActivite)
dataInstallation = Data("../../donnees/installations.csv", "installations", attributsInstallation)

csv = CreateFromCSV()
csv.createTables(dataEquipement)
csv.addDataBase(dataEquipement)

csv.createTables(dataActivite)
csv.addDataBase(dataActivite)

csv.createTables(dataInstallation)
csv.addDataBase(dataInstallation)
