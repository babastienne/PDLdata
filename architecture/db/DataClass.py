class DataClass :
	""" Classe qui permet de lier un file csv à une table sql
	et définir les attributs que l'on souhaite insérer dans la table
	Chaque table dans la base de données correspond à une classe de type DataClass """

	def __init__(self, file, table, attributs) :

		self.file = file
		self.table = table
		self.attributs = attributs

	def getFichier(self) :
		return self.file

	def getNomTable(self) :
		return self.table

	def getAttributs(self) :
		return self.attributs
