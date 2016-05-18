import csv
from classe import classeActivite
from classe import classeEquipement
from classe import classeInstallation

def getDataFromCSV(pathToCSVFile, fieldNames, typeOfData):
    dataFile = open(pathToCSVFile, "r") # open the file in read mode
    datas = csv.DictReader(dataFile, escapechar='\\', doublequote=True) #
    for line in datas:
        if(typeOfData == "activite"):
            print(line.get(fieldNames[0]))
        elif(typeOfData == "equipement"):
            print(line)
        elif(typeOfData == "installation"):
            print(line)
        else:
            raise Exception("Impossible de créer des objets à partir du fichier CSV")
    print("bravo")
    dataFile.close() # close the file
