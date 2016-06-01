import sqlite3
import os.path

class Dao :

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
        self.connexion.close()
        self.connexion = None

    def insert(self,request):
        if self.connexion == None:
            self.connexionDb()
        cursor = self.connexion.cursor()
        cursor.execute(request)

    def commit(self):
        self.connexion.commit()
        self.deconnexion()

    def select(self,request):
        if self.connexion == None:
            self.connexionDb()
        cursor = self.connexion.cursor()
        print(request)
        cursor.execute(request)
        return cursor.fetchall()
