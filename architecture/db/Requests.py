from .Dao import Dao

class Requests(object):
	""" This class contain all the requests to the database
	    from the server for the website """

	def __init__(self):
		""" Start a connexion with the database (initialize Dao object) """
		self.dao = Dao("PDLData", "PDLData", "PDLData")

	def getInstallations(self, activity, city):
		""" Select request which return the installations corresponding to the city and the activity checked by the user """
		if(activity == "" and city != ""):
			return self.dao.select("SELECT `ActLib`, `Numero de la voie`,`Nom de la voie`, `Code postal`, `Nom usuel de l installation`, EquGpsX , EquGpsY from installations, (select EquipementId, InsNumeroInstall , EquGpsX, EquGpsY from equipements where equipements.EquipementId in (select EquipementId from activity where ComInsee = "+ city +"))  equ, activity act where installations.`Numéro de l installation` = equ.InsNumeroInstall and act.`EquipementId` = equ.`EquipementId` ORDER BY `ActLib`")
		if(activity != "" and city == ""):
			return self.dao.select("SELECT `Nom usuel de l installation`, `Numero de la voie`,`Nom de la voie`, `Code postal`, `Nom de la commune`, EquGpsX , EquGpsY from installations, (select EquipementId, InsNumeroInstall , EquGpsX, EquGpsY from equipements where equipements.EquipementId in (select EquipementId from activity where ActCode = "+ activity +"))  equ, activity act where installations.`Numéro de l installation` = equ.InsNumeroInstall and act.`EquipementId` = equ.`EquipementId` ORDER BY `ActLib`")
		else:
			return self.dao.select("SELECT `Nom usuel de l installation`, `Numero de la voie`,`Nom de la voie`, `Code postal`, `Nom de la commune`, EquGpsX , EquGpsY from installations, (select InsNumeroInstall , EquGpsX, EquGpsY from equipements where equipements.EquipementId in (select EquipementId from activity where ActCode = "+ activity +" and ComInsee = "+ city +"))  equ where installations.`Numéro de l installation` = equ.InsNumeroInstall")

	def getActivity(self):
		""" Select request which return all the activity in the database """
		return self.dao.select("SELECT DISTINCT ActLib, ActCode FROM activity ORDER BY ActLib")

	def getCity(self):
		""" Select request which return all the city in the database """
		return self.dao.select("SELECT DISTINCT `Code INSEE`, `Nom de la commune` FROM installations ORDER BY `Nom de la commune`")
