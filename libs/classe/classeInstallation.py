class installation:
    """Classe définissant une installation caractérisée par :
    - son nomInstallation
    - son NumInstall
    - son nomCommune
    - son codeInsee
    - son codePostal """


    def __init__(self, nomInstallation,numInstall,nomCommune, codeInsee,codePostal ):
        """Constructeur de notre classe"""
        self.nomInstallation = nomInstallation
        self.numInstall = numInstall
        self.nomCommune = nomCommune
        self.codeInsee = codeInsee
        self.codePostal = codePostal

    def getNameClass(self):
        return "installation"

    def getValues(self):
        ''' Return the values of each field of the class.
        The values are in a string because the method is used
        to import values in the database. '''
        values = str(self.nomInstallation) + ", \"" + str(self.numInstall) + "\", \"" + str(self.nomCommune) + "\", " + str(self.codeInsee) + ", \"" + str(self.codePostal) + "\""
        print(values)
        return values

    def getColumnsName(self):
        ''' Return the name of each field of the class.
        The name are in a string because the method is used
        to import values in the database. '''
        return "(nomInstallation, numInstall, nomCommune, codeInsee, codePostal)"
