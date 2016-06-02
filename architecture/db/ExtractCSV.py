import csv
from DataClass import DataClass
from Dao import Dao

class ExtractCSV:
	"""
	This class call the Dao class and extract the data from csv file
	by using the DataClass. With this class we can create a database,
	create tables, insert data in tables.
	"""

	def __init__(self):
		""" Constructor of the class. Here we create a database. """
		self.db = Dao ("PDLData","PDLData","PDLData")

	def addDataBase(self,data):
		""" Extract data from a csv file and add data in the database line by line (one command for each line of data) """
		array = ExtractCSV.create(data)
		for row in array:
			request = "INSERT INTO " + data.getTableName() + " VALUES ("
			for value in row:
				request += value +", "
			request = request[:len(request)-2] # used for remove the last ", " which is useless
			request += ")"
			self.db.insert(request) # insert the line to the database (call of the Dao class)
		self.db.commit() # commit the modifications on the database

	def create(data):
		""" Read a csv file and return a list of lists including of the informations of the file.
		The informations are traited by the method addDataBase. """
		dataFile = open(data.getFile(), "r") # we open the csv file in read only
		Dict = csv.DictReader(dataFile, escapechar='\\', doublequote=True)
		resultArray = []
		for row in Dict:
			array = []
			for i in data.getAttributs():
				try:
					tmp = row[i[0]].strip()
					array.append(tmp if tmp.isnumeric() else "\"" + tmp.replace("\"", " ") + "\"")
				except KeyError:
					print("The key " + i + "doesn't exist")
			resultArray.append(array)
		return resultArray

	def createTables(self,data):
		""" This method create a table in the database """
		try:
			request = "CREATE TABLE " + data.getTableName() + "("
			for attributs in data.getAttributs():
				request += "`" + attributs[0].replace("\'", " ") + "` "+ attributs[1]+","
			request = request[:len(request)-1] # remove the last "," which is useless
			request += ")"
		except:
			raise("Error in the description of the table")
		self.db.insert(request) # insert the request in the database [create the table]
		self.db.commit() # commit the modification
