class DataClass :
	""" Class wich contain the path to a csv file, his name and the attributs of his rows.
	Each table in the dataBase has a dataClass corresponding in the beginning """

	def __init__(self, file, table, attributs) :
		""" Contructor of the class"""
		self.attributs = attributs
		self.file = file
		self.table = table

	def getAttributs(self) :
		""" Getter for the list containing informations about
		the rows in the csv file (and the database) """
		return self.attributs

	def getFile(self) :
		""" Getter returning the path to the csv file """
		return self.file

	def getTableName(self) :
		""" Getter returning the name of the Table/Class """
		return self.table
