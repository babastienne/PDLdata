import csv
from DataClass import DataClass
from Dao import Dao

class ExtractCSV:
    """
    Cette classe permet l'utilisation de la classe Dao : elle
    créé des tables dans la base de données, créé une base de données,
    et insert toutes les valuers présentes dans les fichiers CSV.
    Cette classe a pour but de lire les fichiers CSV contenants les
    données afin de les placer dans la base de données utilisée par
    le serveur.
    """

    def __init__(self):
       self.db = Dao ("PDLData","PDLData","PDLData")

    @staticmethod
    def create(data):
        """ Lis un fichier csv et retourne une liste de listes possédant chaque information.
        Les informations sont traitées par la méthode addDataBase. """
        dataFile = open(data.getFichier(), "r") # on ouvre le fichier csv en lecture seule
        parserDict = csv.DictReader(dataFile, escapechar='\\', doublequote=True)
        result = []
        for row in parserDict:
            array = []
            for i in data.getAttributs():
                try:
                    tmp = row[i[0]].strip()
                    array.append(tmp if tmp.isnumeric() else "\"" + tmp.replace("\"", " ") + "\"") # Cette ligne permet de créer une manière d'échaper les caractères " créant des erreurs lors de l'insertion dans une base de données
                except KeyError:
                    print ("La clé " + i + "n'existe pas")
            result.append(array)
        return result

    def addDataBase(self,data):
        """ Ajoute une ligne dans une table de la base de données. """
        array = ExtractCSV.create(data)
        for row in array:
            request = "Insert into " + data.getNomTable() + " values ("
            for value in row:
                request += value +", "
            request = request[:len(request)-2]
            request += ")"
            self.db.insert(request)
        self.db.commit()


    def createTables(self,data):
        """ Cette méthode créé une table dans la base de données """
        request = "Create table " + data.getNomTable() + "("
        for attributs in data.getAttributs():
            request += "`" + attributs[0].replace("\'", " ") + "` "+ attributs[1]+","
        request = request[:len(request)-1] # on enlève la dernière virgule de la requète
        request += ")"
        self.db.insert(request) # on insère la requete dans la base de données
        self.db.commit() # on commit la modification effectuée : la table est créée dans la abse de données
