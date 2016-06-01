import dao as database
import extractcsv

# def __init__(self):


def initDataBase():
    dao = database.Dao("julien", "julien", "pdl.db") # creation of the dataBase
    dao.connexion() # connexion to the database

    dao.dropTables(["activite", "equipement", "installation"])
    dao.commit() # commit the modifications on the database

    activite = ["activite", ["equipementid", "comLib", "actLib", "actCode", "actNivLib"], ["INTEGER", "TEXT", "TEXT", "INTEGER", "TEXT"], "../datas/activite.csv"]
    equipement = ["equipement", ["equipementid", "equNom", "comLib", "equipementTypeLib", "equipementFiche"], ["INTEGER", "TEXT", "TEXT", "TEXT", "TEXT"], "../datas/equipements.csv"]
    installation = ["installation", ["nomInstallation", "numInstall", "nomCommune", "codeInsee", "codePostal"], ["TEXT", "TEXT", "TEXT", "TEXT", "TEXT"], "../datas/installations.csv"]

    listeOfTables = [activite, equipement, installation]

    for i in range(len(listeOfTables)):
        dao.createTable(listeOfTables[i][0], listeOfTables[i][1], listeOfTables[i][2])

    for i in range(len(listeOfTables)):
        for object in extractcsv.getDataFromCSV(listeOfTables[i][3], listeOfTables[i][1], listeOfTables[i][0]):
            dao.insertIntoTable(object)

    dao.commit() # commit the modifications on the database
    dao.deconnexion() # deconnexion of the database

# def extractFromCSV(pathToCSVFile):


initDataBase()
# extractFromCSV("../datas/activite.csv")
