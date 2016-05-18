import csv
import sqlite3
import classeActivite
import classeEquipement
import classeInstallation

class Dao:

	def __init__(self, user, pwd, pathToDatabaseFile) :
	        """ Constructeur de la classe coBD """
	        self.user = user
	        self.pwd = pwd
	        self.database = pathToDatabaseFile
	        self.connected = None

	def connexion(self) :
	    try :
	        self.connected = sqlite3.connect(self.database)
	    except sqlite3.connector.Error as err :
	        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR :
	            print("Something is wrong with your user name or password")
	        elif err.errno == errorcode.ER_BAD_DB_ERROR :
	            print("Database does not exist")
	        else :
	            print(err)

	def deconnexion(self):
		self.connected.close()
		self.connected = None

	def execute(self, command):
		if(self.connected == None):
			self.connected.connexion()
		cursor = self.connected.cursor()
		cursor.execute(command)

	def dropTables(self, listOfTables):
		for table in listOfTables:
			self.connected.execute("""DROP TABLE """ + table)

	def commit(self):
		if(self.connected == None):
			self.connected.connexion()
		self.connected.commit()

	def createTable(self, tableName, listOfColumns, listTypeOfColumns):
		if(len(listOfColumns) != len(listTypeOfColumns)):
			raise Exception("Pas le même nombre de type de colonnes que de colonnes à créer")
		else:
			request = "CREATE TABLE " + tableName + "("
			for i in range(0, len(listOfColumns)):
				request = request + listOfColumns[i] + " " + listTypeOfColumns[i] + ", "
			resquest = request[:-2] + ")"
			self.connected.execute(resquest)

	def insertIntoTable(self, object):
		request = "INSERT INTO " + object.getNameClass() + object.getColumnsName() + " VALUES(" + object.getValues() + ")"
		print(request)
		self.connected.execute(request)


	############################## OLD STUFF ###############################

	def importDataInTable(pathToCsvFile, fieldnames):
		with open(pathToCsvFile, 'r') as csvfile:
			myRead = csv.DictReader(csvfile, fieldnames=fieldnames)
			for row in myRead:
				boolean = true
				for i in row:
					if not i:
						boolean = false
				myActivity = classeActivite.activite(row[fieldnames[0]],row[fieldnames[1]],row[fieldnames[2]],row[fieldnames[3]],row[fieldnames[4]])
				if myActivity.actLib != "" and myActivity.equipementid and myActivity.comLib and myActivity.actCode and myActivity.actNivLib:
					cursor.execute("INSERT INTO activite VALUES(?, ?, ?, ?, ? )", (myActivity.equipementid,myActivity.comLib,myActivity.actLib,myActivity.actCode,myActivity.actNivLib))
		csvfile.close()


	################################################################# OLD ##########################
	with open('../datas/activite.csv', 'r') as csvfile:


	# Data import from activite.csv
		fieldnames = ['ComInsee','comLib', 'Equipementid', 'EqunbEquIdentique', 'ActCode', 'ActLib', 'EquActivitePraticable','EquActivitePratique', 'EquActiviteSalleSpe', 'ActNivLib'] # On associe chaque colonne à un nom
		myRead = csv.DictReader(csvfile, fieldnames=fieldnames)
		accumulator = 0
		for row in myRead:
			if accumulator > 0:
				myActivity = classeActivite.activite(row['Equipementid'],row['comLib'],row['ActLib'],row['ActCode'],row['ActNivLib'])
				if myActivity.actLib != "" and myActivity.equipementid and myActivity.comLib and myActivity.actCode and myActivity.actNivLib:
					cursor.execute("INSERT INTO activite(equipementid,comLib,actLib,actCode,actNivLib) VALUES(?, ?, ?, ?, ?)", (myActivity.equipementid,myActivity.comLib,myActivity.actLib,myActivity.actCode,myActivity.actNivLib))
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
