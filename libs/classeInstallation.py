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