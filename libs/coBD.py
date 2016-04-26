import csv
import sqlite3
import classeActivite
import classeEquipement
import classeInstallation


with open('../datas/activite.csv', 'r') as csvfile:
	conn = sqlite3.connect('ma_base.db') # Allow the creation of database
	cursor = conn.cursor()
	
	# Delete tables in database, allow us to do some test.
	cursor.execute("""
	DROP TABLE activite
	""")
	cursor.execute("""
	DROP TABLE equipement
	""")
	cursor.execute("""
	DROP TABLE installation
	""")
	conn.commit()	
	# End Delete tables

	# Table Creation
	cursor.execute("""
	CREATE TABLE activite(
	     equipementid INTEGER,
	     comLib TEXT,
	     actLib TEXT,
	     actCode INTEGER,
	     actNivLib TEXT
	)
	""")
	cursor.execute("""
	CREATE TABLE equipement(
	     equipementid INTEGER,
	     equNom TEXT,
	     comLib TEXT,
	     equipementTypeLib TEXT,
	     equipementFiche TEXT
	)
	""")
	cursor.execute("""
	CREATE TABLE installation(
	     nomInstallation TEXT,
	     numInstall TEXT,
	     nomCommune TEXT,
	     codeInsee TEXT,
	     codePostal TEXT
	)
	""")
	conn.commit()
	# End Table Creation

# Data import from activite.csv
	fieldnames = ['ComInsee','comLib', 'Equipementid', 'EqunbEquIdentique', 'ActCode', 'ActLib', 'EquActivitePraticable','EquActivitePratique', 'EquActiviteSalleSpe', 'ActNivLib'] # On associe chaque colonne à un nom
	myRead = csv.DictReader(csvfile, fieldnames=fieldnames)
	accumulator = 0
	for row in myRead:
		if accumulator > 0:	
			myActivity = classeActivite.activite(row['Equipementid'],row['comLib'],row['ActLib'],row['ActCode'],row['ActNivLib']) 
			if myActivity.actLib != "" and myActivity.equipementid and myActivity.comLib and myActivity.actCode and myActivity.actNivLib: 
				cursor.execute("INSERT INTO activite(equipementid,comLib,actLib,actCode,actNivLib) VALUES({0}, \"{1}\", \"{2}\", {3}, \"{4}\")".format(myActivity.equipementid,myActivity.comLib,myActivity.actLib,myActivity.actCode,myActivity.actNivLib))
		accumulator = accumulator + 1
	csvfile.close()
# End data import from activite.csv

# Data import from equipement.csv
with open('../datas/equipements.csv', 'r') as csvfile:
	conn = sqlite3.connect('ma_base.db') # Permet de créer la base de donnée
	cursor = conn.cursor()
	fieldnames2 = ['ComInsee','ComLib', 'InsNumeroInstall', 'InsNom', 'EquipementId', 'EquNom', 'EquNomBatiment','EquipementTypeLib', 'EquipementFiche'] # On associe chaque colonne à un nom
	myRead = csv.DictReader(csvfile, fieldnames=fieldnames2)
	accumulator = 0

	for row in myRead:
		if accumulator > 0:	
			myEquipement = classeEquipement.equipement(row['EquipementId'],row['EquNom'],row['ComLib'],row['EquipementTypeLib'],row['EquipementFiche']) 
			if myEquipement.equipementid != "" and myEquipement.equNom and myEquipement.comLib and myEquipement.equipementTypeLib and myEquipement.equipementFiche: 
				cursor.execute("INSERT INTO equipement(equipementid,equNom,comLib,equipementTypeLib,equipementFiche) VALUES(?, ?, ?, ?, ?)", (myEquipement.equipementid, myEquipement.equNom, myEquipement.comLib, myEquipement.equipementTypeLib,myEquipement.equipementFiche))
		accumulator = accumulator + 1
	csvfile.close()
# End data import from equipement.csv

# Data import from installation.csv
with open('../datas/installations.csv', 'r') as csvfile:
	conn = sqlite3.connect('ma_base.db') # Permet de créer la base de donnée
	cursor = conn.cursor()
	fieldnames3 = ['Nom usuel de l\'installation','Numero de l\'installation', 'Nom de la commune', 'Code INSEE', 'Code postal'] # On associe chaque colonne à un nom
	myRead = csv.DictReader(csvfile, fieldnames=fieldnames3)
	accumulator = 0
	for row in myRead:
		if accumulator > 0:	
			myInstallation = classeInstallation.installation(row['Nom usuel de l\'installation'],row['Numero de l\'installation'],row['Nom de la commune'],row['Code INSEE'],row['Code postal']) 
			if myInstallation.nomInstallation != "" and myInstallation.numInstall and myInstallation.nomCommune and myInstallation.codeInsee and myInstallation.codePostal: 
				cursor.execute("INSERT INTO installation(nomInstallation,numInstall,nomCommune,codeInsee,codePostal) VALUES(?, ?, ?, ?, ?)", (myInstallation.nomInstallation, myInstallation.numInstall, myInstallation.nomCommune, myInstallation.codeInsee,myInstallation.codePostal))
		accumulator = accumulator + 1
	csvfile.close()
# End fin gestion fichier installation


