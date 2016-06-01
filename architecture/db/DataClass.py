class Data :
	""" Classe qui permet de lier un fichier csv à une table sql 
	et définir les attributs que l'on souhaite insérer dans la table """

	def __init__(self, fichier, nomTable, attributs) :

		self.fichier = fichier
		self.nomTable = nomTable
		self.attributs = attributs


	def getFichier(self) :
		return self.fichier

	def getNomTable(self) :
		return self.nomTable

	def getAttributs(self) :
		return self.attributs
