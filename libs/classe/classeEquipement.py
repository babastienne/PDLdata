class equipement:
    """Classe définissant un équipement caractérisé par :
    - son equipementid 5
    - son EquNom 6
    - son comLib 2
    - son EquipementTypeLib 8
    - son EquipementFiche 9"""


    def __init__(self, equipementid,equNom, comLib,equipementTypeLib,equipementFiche ):
        """Constructeur de notre classe"""
        self.equipementid = equipementid
        self.equNom = equNom
        self.comLib = comLib
        self.equipementTypeLib = equipementTypeLib
        self.equipementFiche = equipementFiche

    def getNameClass(self):
        return "equipement"

    def getValues(self):
        ''' Return the values of each field of the class.
        The values are in a string because the method is used
        to import values in the database. '''
        values = str(self.equipementid) + ", \"" + str(self.equNom) + "\", \"" + str(self.comLib) + "\", " + str(self.equipementTypeLib) + ", \"" + str(self.equipementFiche) + "\""
        print(values)
        return values

    def getColumnsName(self):
        ''' Return the name of each field of the class.
        The name are in a string because the method is used
        to import values in the database. '''
        return "(equipementid, equNom, comLib, equipementTypeLib, equipementFiche)"
