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