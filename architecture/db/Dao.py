import sqlite3
import os.path

class Dao :
	"""
	The class Dao execute many operations on the database for administrate it.
	For example, methods can do : open connexion, create table, select,
	insert, deconnexion ...
	This class is called by ExtractCSV and Requests.
	"""

	def __init__(self, user, pwd, pathToDatabaseFile) :
		""" Constructor of Dao """
		self.user = user
		self.pwd = pwd
		BASE_DIR = os.path.dirname(os.path.abspath(__file__))
		db_path = os.path.join(BASE_DIR, pathToDatabaseFile + ".db") # SQLite3 need to have the exact path to the database (error if not, can't find the database and create another)
		self.database = db_path
		self.connexion = None # by default the connexion is null

	def connexionDb(self) :
		""" Create a connexion to the database (stock in the connexion attribut of the class) """
		try :
			self.connexion = sqlite3.connect(self.database)
		except sqlite3.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR :
				print("Something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR :
				print("Database does not exist")
			else:
				print(err)

	def deconnexion(self):
		""" Deconnexion of the database. The attribut connexion return to null """
		self.connexion.close()
		self.connexion = None

	def insert(self,request):
		""" Insert a command in the database (need an open connexion or create a connexion if not) """
		if self.connexion == None:
			self.connexionDb()
		command = self.connexion.cursor()
		command.execute(request)

	def commit(self):
		""" Commit the modification on the database and set the connexion attribut to null """
		self.connexion.commit()
		self.deconnexion()

	def select(self,request):
		""" Just like an insert command but return the content of the request """
		if self.connexion == None:
			self.connexionDb()
		command = self.connexion.cursor()
		command.execute(request)
		return command.fetchall()
