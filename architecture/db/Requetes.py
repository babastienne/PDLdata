from .Dao import Dao

class Requetes(object):

	def __init__(self):
		self.dao = Dao("PDLData", "PDLData", "PDLData")

	def getVilles(self):
		return self.dao.select("SELECT DISTINCT `Code INSEE`, `Nom de la commune` FROM installations ORDER BY `Nom de la commune`")

	def getInstallations(self, activite, ville):
		return self.dao.select("SELECT `Nom usuel de l installation`, `Numero de la voie`,`Nom de la voie`, `Code postal`, `Nom de la commune`, EquGpsX , EquGpsY from installations, (select InsNumeroInstall , EquGpsX, EquGpsY from equipements where equipements.EquipementId in (select EquipementId from activites where ActCode = "+activite+" and ComInsee = "+ville+"))  equ where installations.`Numéro de l installation` = equ.InsNumeroInstall")

	def getActivites(self):
		return self.dao.select("SELECT DISTINCT ActLib, ActCode FROM activites ORDER BY ActLib")
