import csv
from Data import Data
from Dao import Dao

class CreateFromCSV:

    def __init__(self):
       self.db = Dao ("PDLData","PDLData","PDLData")

    @staticmethod
    def create(data):
        dataFile = open(data.getFichier(), "r")
        parserDict = csv.DictReader(dataFile, escapechar='\\', doublequote=True)
        result = []
        for row in parserDict:
            array = []
            for i in data.getAttributs():
                try:
                    tmp = row[i[0]].strip()
                    array.append(tmp if tmp.isnumeric() else "\"" + tmp.replace("\"", " ") + "\"")
                except KeyError:
                    print ("La clé " + i + "n'existe pas")
            result.append(array)
        return result

    def addDataBase(self,data):
        array = CreateFromCSV.create(data)
        for row in array:
            request = "Insert into " + data.getNomTable() + " values ("
            for value in row:
                request += value +", "
            request = request[:len(request)-2]
            request += ")"
            self.db.insert(request)
        self.db.commit()


    def createTables(self,data):
        request = "Create table " + data.getNomTable() + "("
        for attributs in data.getAttributs():
            request += "`" + attributs[0].replace("\'", " ") + "` "+ attributs[1]+","
        request = request[:len(request)-1]
        request += ")"
        self.db.insert(request)
        self.db.commit()
