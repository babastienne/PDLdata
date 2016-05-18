import dao

def __init__(self):
    #TODO

def initDataBase():
    dao = coBD.Dao("julien", "julien", "pdl.db") # creation of the dataBase
    dao.connexion() # connexion to the database

    dao.dropTables(["activite", "equipement", "installation"])
    dao.commit() # commit the modifications on the database

    activite = ["activite", ["equipementid", "comLib", "actLib", "actCode", "actNivLib"], ["INTEGER", "TEXT", "TEXT", "INTEGER", "TEXT"]]
    equipement = ["equipement", ["equipementid", "equNom", "comLib", "equipementTypeLib", "equipementFiche"], ["INTEGER", "TEXT", "TEXT", "TEXT", "TEXT"]]
    installation = ["installation", ["nomInstallation", "numInstall", "nomCommune", "codeInsee", "codePostal"], ["TEXT", "TEXT", "TEXT", "TEXT", "TEXT"]]

    dao.createTable(activite[0], activite[1], activite[2])
    dao.createTable(equipement[0], equipement[1], equipement[2])
    dao.createTable(installation[0], installation[1], installation[2])

    dao.insertIntoTable(firstactivity)

    dao.commit() # commit the modifications on the database
    dao.deconnexion() # deconnexion of the database

initDataBase()
