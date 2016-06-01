import sqlite3
import os.path

class Dao :
	"""
	La classe Dao est la classe permettant d'effectuer les différentes opérations
	sur la base de données : ouvrir une connexion, créer une base de données, select
	insert, deconnexion ...
	Cette classe est appelée par la classe extractCSV et Requetes
	"""

	def __init__(self, user, pwd, pathToDatabaseFile) :
		""" Constructeur de la classe Dao """
		self.user = user
		self.pwd = pwd
		BASE_DIR = os.path.dirname(os.path.abspath(__file__))
		db_path = os.path.join(BASE_DIR, pathToDatabaseFile + ".db")
		print(db_path)
		self.database = db_path
		self.connexion = None

	def connexionDb(self) :
		""" Permet la connexion à la base de données """
		try :
			self.connexion = sqlite3.connect(self.database)
		except sqlite3.connector.Error as err :
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR :
				print("Something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR :
				print("Database does not exist")
			else :
				print(err)

	def deconnexion(self):
		""" Deconnecte la base de données """
		self.connexion.close()
		self.connexion = None

	def insert(self,request):
		""" Permet l'insertion de données dans la base de données """
		if self.connexion == None:
			self.connexionDb()
		cursor = self.connexion.cursor()
		cursor.execute(request)

	def commit(self):
		""" Commit (valide) les modifications dans la base de données """
		self.connexion.commit()
		self.deconnexion()

	def select(self,request):
		""" Permet une requète de type select. On renvoi les données récupérées via le curseur. """
		if self.connexion == None:
			self.connexionDb()
		cursor = self.connexion.cursor()
		print(request)
		cursor.execute(request)
		return cursor.fetchall()
