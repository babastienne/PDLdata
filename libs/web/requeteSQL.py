import sqlite3

class requeteSQL:



    def __init__(self):
        """Constructeur de notre classe"""

    def activiteAccess(id, comLib):
        conn = sqlite3.connect('ma_base.db') # Allow the creation of database
        cursor = conn.cursor()
        cursor.execute("Select equipementid,comLib,actLib,actCode,actNivLib from activite where equipementid="+ id +" and comLib="+ comLib+"")
        activites = cursor.fetchall()
        for activites in act:
            print("Informations liées à l'activitées sont, son ID :  %s ; comLib : %s ; actLob : %s ; actCode : %s ; actNivLib : %s " % (act[0], act[2], act[1], act[3]))

    def installationAccess(nomInstallation,numInstall,nomCommune, codeInsee,codePostal):
        conn = sqlite3.connect('ma_base.db') # Allow the creation of database
        cursor = conn.cursor()
        cursor.execute("Select nomInstallation,numInstall,nomCommune, codeInsee,codePostal from activite where nomInstallation="+ nomInstallation +" and numInstall="+ numInstall+"")
        activites = cursor.fetchall()
        for activites in act:
            print("Informations liées à l'activitées sont, son nomInstallation :  %s ; numInstall : %s ; nomCommune : %s ; codeInsee : %s ; codePostal : %s " % (act[0], act[2], act[1], act[3],act[4]))

    def equipementAccess(equipementid,equNom, comLib,equipementTypeLib,equipementFiche):
        conn = sqlite3.connect('ma_base.db') # Allow the creation of database
        cursor = conn.cursor()
        cursor.execute("Select equipementid,equNom, comLib,equipementTypeLib,equipementFiche from activite where equipementid="+ id +" and comLib="+ comLib+"")
        activites = cursor.fetchall()
        for activites in act:
            print("Informations liées à l'activitées sont, son ID :  %s ; equNom : %s ; equNom : %s ; equipementTypeLib : %s ; equipementFiche : %s " % (act[0], act[2], act[1], act[3],act[4]))


	# Methode qui permet de récupérer les données de la table Installation
    def installationAccess(nomInstallation,numInstall,nomCommune, codeInsee,codePostal):
        conn = sqlite3.connect('ma_base.db') # Allow the creation of database
        cursor = conn.cursor()
        nomInstallation = []
        codeCommune = []
        for row in cursor.execute("Select nomInstallation from activite") :
            nomInstallation.append(row)
		for row in cursor.execute("Select comLib from activite"):
            codeCommune.append(row)
        return template("montemplate.tpl",nomInstallation =nomInstallation)
