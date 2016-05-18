class activite:
    """Classe définissant une activité caractérisée par :
    - son equipementid
    - son actLib
    - son comLib
    - son actCode
    - son actNivLib"""


    def __init__(self, equipementid, comLib,actLib,actCode,actNivLib ):
        """Constructeur de notre classe"""
        self.equipementid = equipementid
        self.comLib = comLib
        self.actLib = actLib
        self.actCode = actCode
        self.actNivLib = actNivLib

    def getNameClass(self):
        return "activite"

    def getValues(self):
        ''' Return the values of each field of the class.
        The values are in a string because the method is used
        to import values in the database. '''
        values = str(self.equipementid) + ", \"" + str(self.comLib) + "\", \"" + str(self.actLib) + "\", " + str(self.actCode) + ", \"" + str(self.actNivLib) + "\""
        print(values)
        return values

    def getColumnsName(self):
        ''' Return the name of each field of the class.
        The name are in a string because the method is used
        to import values in the database. '''
        return "(equipementid, comLib, actLib, actCode, actNivLib)"
