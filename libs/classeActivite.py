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