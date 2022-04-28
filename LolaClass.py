import random
tick = 0
def Tick(t):
    return t + 1
tick = Tick(tick)





Lapis = [[0,0,2,0,2],[0,0,4,0,5],[2,0,6,0,8],
         [2,0,8,0,11],[2,0,10,0,12],[4,2,11,0,12],
         [4,2,12,0,19],[4,6,18,2,26],[6,7,20,2,34]]
Irlis = [[4, 2, 0, 0, 0],[8, 2, 0, 0, 0],[9, 4, 0, 0, 2],
         [14, 6, 2, 0, 2],[19, 8, 2, 0, 2],[24, 8, 4, 2, 4],
         [34, 8, 4, 2, 4],[40, 8, 8, 2, 6],[48, 9, 8, 2, 8]]
Jaade_Vert = [[2, 10, 2, 0, 0],[2, 12, 2, 0, 0],[4, 14, 2, 0, 0],
              [5, 14, 2, 0, 0],[5, 16, 4, 0, 0],[6, 19, 4, 0, 4],
              [7, 24, 6, 0, 4],[9, 26, 6, 2, 4],[9, 29, 8, 2, 4]]
Jaade_Noir = [[0, 10, 2, 2, 0],[0, 12, 2, 2, 0],[0, 14, 2, 2, 0],
           [2, 16, 2, 4, 0],[2, 16, 4, 4, 0],[2, 19, 4, 6, 2],
           [4, 24, 4, 8, 2],[4, 26, 4, 8, 4],[8, 29, 6, 11, 4]]
Easthee = [[0, 4, 2, 2, 12],[0, 4, 2, 2, 12],[2, 4, 2, 2, 12],
           [2, 4, 2, 2, 12],[4, 6, 2, 2, 14],[4, 6, 2, 2, 14],
           [6, 8, 4, 4, 14],[6, 8, 4, 4, 18],[8, 9, 4, 4, 18]]
Normal_Categories = {"Lapis" : Lapis , "Irlis" : Irlis , "Jaade Vert" : Jaade_Vert , "Jaade Noir" : Jaade_Noir , "Easthee" : Easthee}
def attack(Competences : list , Statistiques : list , tick : int , Competence : int):
    if Competences[Competence][2][0] <= tick - Competences[Competence][2][1]:
        Competences[Competence][2][1] = tick
        return [int((Competences[Competence][0][0]*Statistiques[0])) + random.randint(0,Statistiques[4]) , int(Competences[Competence][0][1]*Statistiques[1]) , int(Competences[Competence][0][2]*Statistiques[3]) , False] , (tick+1) , "Competence utilisee"
    else:
        return [0,0,0,False] , (tick+1) , "Competence en Cooldown"
def useCompetence(Competences : list , tick : int , Competence : int):
    if Competences[Competence][2][0] <= tick - Competences[Competence][2][1]:
        Competences[Competence][2][1] = tick
        die = random.randint(0,100)
        return  [die <= Competences[Competence][0][0] , False] , (tick+1) , "Competence utilisee"
    else:
        return [False,False] , (tick+1) , "Competence en Cooldown"
def useMoveCompetence(Competences : list , tick : int , Competence : int):
    if Competences[Competence][2][0] <= tick - Competences[Competence][2][1]:
        Competences[Competence][2][1] = tick
        die = random.randint(0,100)
        return  [die <= Competences[Competence][0][0] , True] , (tick+1) , "Competence utilisee"
    else:
        return [False,False] , (tick+1) , "Competence en Cooldown"
def getCat(name : str , palier : int):
    """
    renvoie les stats de la categorie de l'arme en fonction de son palier.
    """
    if name == "Lapis":
        return Lapis[palier]
    elif name == "Irlis":
        return Irlis[palier]
    elif name == "Jaade_Vert" or "Jaade Vert":
        return Jaade_Vert[palier]
    elif name == "Jaade_Noir" or "Jaade Noir":
        return Jaade_Noir[palier]
    elif name == "Easthee":
        return Easthee[palier]
    else:
        return [0,0,0,0,0]
def getCatArm(name : str , palier : int):
    pass
def getAttackCompetenceIndice(name : str , Competences : list):
    for i in range(4):
        if name == Competences[i][1][0]:
            return i
    return 0
def getCompetenceIndice(name : str , Competences : list):
    for i in range(len(Competences)):
        if name == Competences[i][1][0]:
            return i
    return 0
class Weapon():
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list):
        self.name = Name
        self.catg = Categorie
        self.palier = Palier
        self.maitrise = Maitrise
        self.infusion = Infusion
        self.catg_stats = Normal_Categories[Categorie][Palier]
        self.notimage = "notimage.png"
    def setLevel(self, Palier : int):
        self.palier = Palier
        self.catg_stats = getCat(Categorie , Palier)
class SpeWeapon():
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list):
        self.name = Name
        self.catg = Categorie
        self.palier = Palier
        self.maitrise = Maitrise
        self.infusion = Infusion
        self.catg_stats = getCat(Categorie , Palier)
        self.notimage = "notimage.png"
    def setLevel(self, Palier : int):
        self.palier = Palier
        self.catg_stats = getCat(Categorie , Palier)
        
class Dovoke(Weapon):
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list , stats : list):
        super().__init__(Name , Categorie , Palier , Infusion , Maitrise)
        self.type_stats = [14, 0, 2, 0, 0]
        self.depo = self.catg_stats[4] + self.type_stats[4] + stats[4]
        self.po = self.catg_stats[0] + self.type_stats[0] + stats[0] + self.maitrise[0]
        self.ppr = self.catg_stats[1] + self.type_stats[1] + stats[1] + self.maitrise[1]
        self.pst = self.catg_stats[2] + self.type_stats[2] + stats[2] + self.maitrise[2]
        self.pp = self.catg_stats[3] + self.type_stats[3] + stats[3] + self.maitrise[3]
        self.statistiques = [self.po,self.ppr,self.pst,self.pp,self.depo]
        self.Competences = ([[0.4,1,0.1],["tranchant","attaque basique a la Dovoke"],[1,-1],[False,0]],
              [[1.7,0.8,1],["Celestial","Coup circulaire"],[9,-9],[False,0]],
              [[1.2,1.4,1.2],["couperet","coup vertical"],[6,-6],[False,0]],
              [[0.8,1.2,0.4],["apostat","coup direct"],[2,-2],[False,0]])
        self.image = "https://cdn.discordapp.com/attachments/837490345486712840/966809356790300693/Dovoke.png"
    def Attack(self , tick : int , competence : str):
        at = attack(self.Competences , self.statistiques , tick , getAttackCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
    def help(self):
        return self.Competences[0][1][0] + " : " + self.Competences[0][1][1] + " , " + self.Competences[1][1][0] + " : " + self.Competences[1][1][1] + " , " + self.Competences[2][1][0] + " : " + self.Competences[2][1][1] + " , " + self.Competences[3][1][0] + " : " + self.Competences[3][1][1] + "."
    def helpCompetence(self , Competence : str):
        indice = getAttackCompetenceIndice(Competence , self.Competences)
        txt = ["--"+Competence+"--" + ":" , " Po:" + str(self.Competences[indice][0][0]*100) + " ," , " Ppr:" + str(self.Competences[indice][0][1]*100) + " ," , " Pp:" + str(self.Competences[indice][0][2]*100) , " ;" + " Cd:" + str(self.Competences[indice][2][0])]
        return txt[0] , txt[1] , txt[2] , txt[3] , txt[4]
        
        
class Hirokami(Weapon):
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list , stats : list):
        super().__init__(Name , Categorie , Palier , Infusion , Maitrise)
        self.type_stats = [10, 4, 1, 0, 0]
        self.depo = self.catg_stats[4] + self.type_stats[4] + stats[4]
        self.po = self.catg_stats[0] + self.type_stats[0] + stats[0] + self.maitrise[0]
        self.ppr = self.catg_stats[1] + self.type_stats[1] + stats[1] + self.maitrise[1]
        self.pst = self.catg_stats[2] + self.type_stats[2] + stats[2] + self.maitrise[2]
        self.pp = self.catg_stats[3] + self.type_stats[3] + stats[3] + self.maitrise[3]
        self.statistiques = [self.po,self.ppr,self.pst,self.pp,self.depo]
        self.Competences = ([[0.4,1,0.1],["Pique","attaque basique a l'Hirokami"],[2,-2],[False,0]],
              [[1.9,0.9,0.2],["Hlyly","Coup porté avec une lame affutée par la magie"],[9,-9],[False,0]],
              [[1.3,0.7,1.4],["Siyssa","coup lateral"],[6,-6],[False,0]],
              [[2,0.4,0.3],["Giliviya","Coup circulaire"],[7,-7],[False,0]])
        self.image = "https://cdn.discordapp.com/attachments/837490345486712840/966809441343262760/Hirokami.png"
    def Attack(self , tick : int , competence : str):
        at = attack(self.Competences , self.statistiques , tick , getAttackCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
    def help(self):
        return self.Competences[0][1][0] + " : " + self.Competences[0][1][1] + " , " + self.Competences[1][1][0] + " : " + self.Competences[1][1][1] + " , " + self.Competences[2][1][0] + " : " + self.Competences[2][1][1] + " , " + self.Competences[3][1][0] + " : " + self.Competences[3][1][1] + "."
    def helpCompetence(self , Competence : str):
        indice = getAttackCompetenceIndice(Competence , self.Competences)
        txt = ["--"+Competence+"--" + ":" , " Po:" + str(self.Competences[indice][0][0]*100) + " ," , " Ppr:" + str(self.Competences[indice][0][1]*100) + " ," , " Pp:" + str(self.Competences[indice][0][2]*100) , " ;" + " Cd:" + str(self.Competences[indice][2][0])]
        return txt[0] , txt[1] , txt[2] , txt[3] , txt[4]


class Kataro(Weapon):
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list , stats : list):
        super().__init__(Name , Categorie , Palier , Infusion , Maitrise)
        self.type_stats = [9, 4, 0, 2, 0]
        self.depo = self.catg_stats[4] + self.type_stats[4] + stats[4]
        self.po = self.catg_stats[0] + self.type_stats[0] + stats[0] + self.maitrise[0]
        self.ppr = self.catg_stats[1] + self.type_stats[1] + stats[1] + self.maitrise[1]
        self.pst = self.catg_stats[2] + self.type_stats[2] + stats[2] + self.maitrise[2]
        self.pp = self.catg_stats[3] + self.type_stats[3] + stats[3] + self.maitrise[3]
        self.statistiques = [self.po,self.ppr,self.pst,self.pp,self.depo]
        self.Competences = ([[0.2,1.2,1.6],["Espadon","attaque basique a la Kataro"],[2,-2],[False,0]],
              [[1.1,1.8,1.9],["Vif Air","Tranche l'air autour de soit"],[9,-9],[False,0]],
              [[0.8,2,1.1],["Nymphe","coup vertical"],[6,-6],[False,0]],
              [[0.8,1.2,0.4],["Kier","coup direct"],[2,-2],[False,0]])
        self.image = "https://cdn.discordapp.com/attachments/837490345486712840/966809505365123072/Kataro.png"
    def Attack(self , tick : int , competence : str):
        at = attack(self.Competences , self.statistiques , tick , getAttackCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
    def help(self):
        return self.Competences[0][1][0] + " : " + self.Competences[0][1][1] + " , " + self.Competences[1][1][0] + " : " + self.Competences[1][1][1] + " , " + self.Competences[2][1][0] + " : " + self.Competences[2][1][1] + " , " + self.Competences[3][1][0] + " : " + self.Competences[3][1][1] + "."
    def helpCompetence(self , Competence : str):
        indice = getAttackCompetenceIndice(Competence , self.Competences)
        txt = ["--"+Competence+"--" + ":" , " Po:" + str(self.Competences[indice][0][0]*100) + " ," , " Ppr:" + str(self.Competences[indice][0][1]*100) + " ," , " Pp:" + str(self.Competences[indice][0][2]*100) , " ;" + " Cd:" + str(self.Competences[indice][2][0])]
        return txt[0] , txt[1] , txt[2] , txt[3] , txt[4]


class Korechika(Weapon):
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list , stats : list):
        super().__init__(Name , Categorie , Palier , Infusion , Maitrise)
        self.type_stats = [12, 2, 1, 0, 0]
        self.depo = self.catg_stats[4] + self.type_stats[4] + stats[4]
        self.po = self.catg_stats[0] + self.type_stats[0] + stats[0] + self.maitrise[0]
        self.ppr = self.catg_stats[1] + self.type_stats[1] + stats[1] + self.maitrise[1]
        self.pst = self.catg_stats[2] + self.type_stats[2] + stats[2] + self.maitrise[2]
        self.pp = self.catg_stats[3] + self.type_stats[3] + stats[3] + self.maitrise[3]
        self.statistiques = [self.po,self.ppr,self.pst,self.pp,self.depo]
        self.Competences = ([[0.8,1,0.3],["Coupure","attaque basique a la Korechika"],[2,-2],[False,0]],
              [[1.8,0.9,1],["Croissant","Coup circulaire"],[9,-9],[False,0]],
              [[0.4,1.7,2.8],["Decapitation","Coup circulaire a Dégats internes"],[9,-9],[False,0]],
              [[0.6,0.8,0.4],["Ethé","coup direct"],[2,-2],[False,0]])
        self.image = "https://cdn.discordapp.com/attachments/837490345486712840/966809563707879434/Korechika.png"
    def Attack(self , tick : int , competence : str):
        at = attack(self.Competences , self.statistiques , tick , getAttackCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
    def help(self):
        return self.Competences[0][1][0] + " : " + self.Competences[0][1][1] + " , " + self.Competences[1][1][0] + " : " + self.Competences[1][1][1] + " , " + self.Competences[2][1][0] + " : " + self.Competences[2][1][1] + " , " + self.Competences[3][1][0] + " : " + self.Competences[3][1][1] + "."
    def helpCompetence(self , Competence : str):
        indice = getAttackCompetenceIndice(Competence , self.Competences)
        txt = ["--"+Competence+"--" + ":" , " Po:" + str(self.Competences[indice][0][0]*100) + " ," , " Ppr:" + str(self.Competences[indice][0][1]*100) + " ," , " Pp:" + str(self.Competences[indice][0][2]*100) , " ;" + " Cd:" + str(self.Competences[indice][2][0])]
        return txt[0] , txt[1] , txt[2] , txt[3] , txt[4]


class Riini(Weapon):
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list , stats : list):
        super().__init__(Name , Categorie , Palier , Infusion , Maitrise)
        self.type_stats = [11, 1, 2, 0, 0]
        self.depo = self.catg_stats[4] + self.type_stats[4] + stats[4]
        self.po = self.catg_stats[0] + self.type_stats[0] + stats[0] + self.maitrise[0]
        self.ppr = self.catg_stats[1] + self.type_stats[1] + stats[1] + self.maitrise[1]
        self.pst = self.catg_stats[2] + self.type_stats[2] + stats[2] + self.maitrise[2]
        self.pp = self.catg_stats[3] + self.type_stats[3] + stats[3] + self.maitrise[3]
        self.statistiques = [self.po,self.ppr,self.pst,self.pp,self.depo]
        self.Competences = ([[0.2,1.2,0.2],["L'hypha","attaque basique a la Riini"],[1,-1],[False,0]],
              [[1.7,0.8,1],["Olathy","Coup porté et projeté par la foudre"],[9,-9],[False,0]],
              [[1.5,1.4,1.2],["Eathalyss","coup vertical"],[8,-8],[False,0]],
              [[0.8,0.8,0.8],["Najakir","coup direct"],[4,-4],[False,0]])
        self.image = "https://cdn.discordapp.com/attachments/837490345486712840/966809632515457064/Riini.png"
    def Attack(self , tick : int , competence : str):
        at = attack(self.Competences , self.statistiques , tick , getAttackCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
    def help(self):
        return self.Competences[0][1][0] + " : " + self.Competences[0][1][1] + " , " + self.Competences[1][1][0] + " : " + self.Competences[1][1][1] + " , " + self.Competences[2][1][0] + " : " + self.Competences[2][1][1] + " , " + self.Competences[3][1][0] + " : " + self.Competences[3][1][1] + "."
    def helpCompetence(self , Competence : str):
        indice = getAttackCompetenceIndice(Competence , self.Competences)
        txt = ["--"+Competence+"--" + ":" , " Po:" + str(self.Competences[indice][0][0]*100) + " ," , " Ppr:" + str(self.Competences[indice][0][1]*100) + " ," , " Pp:" + str(self.Competences[indice][0][2]*100) , " ;" + " Cd:" + str(self.Competences[indice][2][0])]
        return txt[0] , txt[1] , txt[2] , txt[3] , txt[4]


class Sekina(Weapon):
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list , stats : list):
        super().__init__(Name , Categorie , Palier , Infusion , Maitrise)
        self.type_stats = [12, 1, 3, 0, 0]
        self.depo = self.catg_stats[4] + self.type_stats[4] + stats[4]
        self.po = self.catg_stats[0] + self.type_stats[0] + stats[0] + self.maitrise[0]
        self.ppr = self.catg_stats[1] + self.type_stats[1] + stats[1] + self.maitrise[1]
        self.pst = self.catg_stats[2] + self.type_stats[2] + stats[2] + self.maitrise[2]
        self.pp = self.catg_stats[3] + self.type_stats[3] + stats[3] + self.maitrise[3]
        self.statistiques = [self.po,self.ppr,self.pst,self.pp,self.depo]
        self.Competences = ([[0.6,0.9,0.1],["Piquier","attaque basique a la Sekina"],[2,-2],[False,0]],
              [[1.9,0.9,0.2],["Hlyly","Coup porté avec une lame affutée par la magie"],[9,-9],[False,0]],
              [[0.7,0.7,0.7],["Sayada","coup lateral projettant de la glace sur son sillage"],[4,-4],[False,0]],
              [[2,0.4,0.3],["Giliviya","Coup circulaire"],[7,-7],[False,0]])
        self.image = "https://cdn.discordapp.com/attachments/837490345486712840/966809708725932092/Sekina.png"
    def Attack(self , tick : int , competence : str):
        at = attack(self.Competences , self.statistiques , tick , getAttackCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
    def help(self):
        return self.Competences[0][1][0] + " : " + self.Competences[0][1][1] + " , " + self.Competences[1][1][0] + " : " + self.Competences[1][1][1] + " , " + self.Competences[2][1][0] + " : " + self.Competences[2][1][1] + " , " + self.Competences[3][1][0] + " : " + self.Competences[3][1][1] + "."
    def helpCompetence(self , Competence : str):
        indice = getAttackCompetenceIndice(Competence , self.Competences)
        txt = ["--"+Competence+"--" + ":" , " Po:" + str(self.Competences[indice][0][0]*100) + " ," , " Ppr:" + str(self.Competences[indice][0][1]*100) + " ," , " Pp:" + str(self.Competences[indice][0][2]*100) , " ;" + " Cd:" + str(self.Competences[indice][2][0])]
        return txt[0] , txt[1] , txt[2] , txt[3] , txt[4]


class Sekriyina(Weapon):
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list , stats : list):
        super().__init__(Name , Categorie , Palier , Infusion , Maitrise)
        self.type_stats = [14, 2, 1, 1, 0]
        self.depo = self.catg_stats[4] + self.type_stats[4] + stats[4]
        self.po = self.catg_stats[0] + self.type_stats[0] + stats[0] + self.maitrise[0]
        self.ppr = self.catg_stats[1] + self.type_stats[1] + stats[1] + self.maitrise[1]
        self.pst = self.catg_stats[2] + self.type_stats[2] + stats[2] + self.maitrise[2]
        self.pp = self.catg_stats[3] + self.type_stats[3] + stats[3] + self.maitrise[3]
        self.statistiques = [self.po,self.ppr,self.pst,self.pp,self.depo]
        self.Competences = ([[0.4,1.3,1.8],["Lunae","attaque basique a la Sekriyina"],[4,-4],[False,0]],
              [[1.1,1.2,2.9],["Vent du Desert","Coup circulaire"],[9,-9],[False,0]],
              [[0.6,1.8,2.4],["Analita","coup vertical"],[4,-4],[False,0]],
              [[0.4,2.1,0.8],["Renegat","coup direct"],[2,-2],[False,0]])
        self.image = "https://cdn.discordapp.com/attachments/837490345486712840/966809772429041704/Sekriyina.png"
    def Attack(self , tick : int , competence : str):
        at = attack(self.Competences , self.statistiques , tick , getAttackCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
    def help(self):
        return self.Competences[0][1][0] + " : " + self.Competences[0][1][1] + " , " + self.Competences[1][1][0] + " : " + self.Competences[1][1][1] + " , " + self.Competences[2][1][0] + " : " + self.Competences[2][1][1] + " , " + self.Competences[3][1][0] + " : " + self.Competences[3][1][1] + "."
    def helpCompetence(self , Competence : str):
        indice = getAttackCompetenceIndice(Competence , self.Competences)
        txt = ["--"+Competence+"--" + ":" , " Po:" + str(self.Competences[indice][0][0]*100) + " ," , " Ppr:" + str(self.Competences[indice][0][1]*100) + " ," , " Pp:" + str(self.Competences[indice][0][2]*100) , " ;" + " Cd:" + str(self.Competences[indice][2][0])]
        return txt[0] , txt[1] , txt[2] , txt[3] , txt[4]


class Taviris(Weapon):
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list , stats : list):
        super().__init__(Name , Categorie , Palier , Infusion , Maitrise)
        self.type_stats = [10, 1, 4, 0, 0]
        self.depo = self.catg_stats[4] + self.type_stats[4] + stats[4]
        self.po = self.catg_stats[0] + self.type_stats[0] + stats[0] + self.maitrise[0]
        self.ppr = self.catg_stats[1] + self.type_stats[1] + stats[1] + self.maitrise[1]
        self.pst = self.catg_stats[2] + self.type_stats[2] + stats[2] + self.maitrise[2]
        self.pp = self.catg_stats[3] + self.type_stats[3] + stats[3] + self.maitrise[3]
        self.statistiques = [self.po,self.ppr,self.pst,self.pp,self.depo]
        self.Competences = ([[0.4,1,0.1],["tranchant","attaque basique a la Dovoke"],[1,-1],[False,0]],
              [[1.7,0.8,1],["Celestial","Coup circulaire"],[9,-9],[False,0]],
              [[1.2,1.4,1.2],["couperet","coup vertical"],[6,-6],[False,0]],
              [[0.8,1.2,0.4],["apostat","coup direct"],[2,-2],[False,0]])
        self.image = "https://cdn.discordapp.com/attachments/837490345486712840/966809868528930906/Taviris.png"
    def Attack(self , tick : int , competence : str):
        at = attack(self.Competences , self.statistiques , tick , getAttackCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
    def help(self):
        return self.Competences[0][1][0] + " : " + self.Competences[0][1][1] + " , " + self.Competences[1][1][0] + " : " + self.Competences[1][1][1] + " , " + self.Competences[2][1][0] + " : " + self.Competences[2][1][1] + " , " + self.Competences[3][1][0] + " : " + self.Competences[3][1][1] + "."
    def helpCompetence(self , Competence : str):
        indice = getAttackCompetenceIndice(Competence , self.Competences)
        txt = ["--"+Competence+"--" + ":" , " Po:" + str(self.Competences[indice][0][0]*100) + " ," , " Ppr:" + str(self.Competences[indice][0][1]*100) + " ," , " Pp:" + str(self.Competences[indice][0][2]*100) , " ;" + " Cd:" + str(self.Competences[indice][2][0])]
        return txt[0] , txt[1] , txt[2] , txt[3] , txt[4]


class Thriallis(Weapon):
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list , stats : list):
        super().__init__(Name , Categorie , Palier , Infusion , Maitrise)
        self.type_stats = [12, 1, 1, 0, 0]
        self.depo = self.catg_stats[4] + self.type_stats[4] + stats[4]
        self.po = self.catg_stats[0] + self.type_stats[0] + stats[0] + self.maitrise[0]
        self.ppr = self.catg_stats[1] + self.type_stats[1] + stats[1] + self.maitrise[1]
        self.pst = self.catg_stats[2] + self.type_stats[2] + stats[2] + self.maitrise[2]
        self.pp = self.catg_stats[3] + self.type_stats[3] + stats[3] + self.maitrise[3]
        self.statistiques = [self.po,self.ppr,self.pst,self.pp,self.depo]
        self.Competences = ([[0.4,1,0.1],["tranchant","attaque basique a la Dovoke"],[1,-1],[False,0]],
              [[1.7,0.8,1],["Celestial","Coup circulaire"],[9,-9],[False,0]],
              [[1.2,1.4,1.2],["couperet","coup vertical"],[6,-6],[False,0]],
              [[0.8,1.2,0.4],["apostat","coup direct"],[2,-2],[False,0]])
        self.image = "https://cdn.discordapp.com/attachments/837490345486712840/966810067141791834/Thriallis.png"
    def Attack(self , tick : int , competence : str):
        at = attack(self.Competences , self.statistiques , tick , getAttackCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
    def help(self):
        return self.Competences[0][1][0] + " : " + self.Competences[0][1][1] + " , " + self.Competences[1][1][0] + " : " + self.Competences[1][1][1] + " , " + self.Competences[2][1][0] + " : " + self.Competences[2][1][1] + " , " + self.Competences[3][1][0] + " : " + self.Competences[3][1][1] + "."
    def helpCompetence(self , Competence : str):
        indice = getAttackCompetenceIndice(Competence , self.Competences)
        txt = ["--"+Competence+"--" + ":" , " Po:" + str(self.Competences[indice][0][0]*100) + " ," , " Ppr:" + str(self.Competences[indice][0][1]*100) + " ," , " Pp:" + str(self.Competences[indice][0][2]*100) , " ;" + " Cd:" + str(self.Competences[indice][2][0])]
        return txt[0] , txt[1] , txt[2] , txt[3] , txt[4]


class Tlallassa(Weapon):
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list , stats : list):
        super().__init__(Name , Categorie , Palier , Infusion , Maitrise)
        self.type_stats = [13, 3, 1, 1, 0]
        self.depo = self.catg_stats[4] + self.type_stats[4] + stats[4]
        self.po = self.catg_stats[0] + self.type_stats[0] + stats[0] + self.maitrise[0]
        self.ppr = self.catg_stats[1] + self.type_stats[1] + stats[1] + self.maitrise[1]
        self.pst = self.catg_stats[2] + self.type_stats[2] + stats[2] + self.maitrise[2]
        self.pp = self.catg_stats[3] + self.type_stats[3] + stats[3] + self.maitrise[3]
        self.statistiques = [self.po,self.ppr,self.pst,self.pp,self.depo]
        self.Competences = ([[0.4,1,0.1],["tranchant","attaque basique a la Dovoke"],[1,-1],[False,0]],
              [[1.7,0.8,1],["Celestial","Coup circulaire"],[9,-9],[False,0]],
              [[1.2,1.4,1.2],["couperet","coup vertical"],[6,-6],[False,0]],
              [[0.8,1.2,0.4],["apostat","coup direct"],[2,-2],[False,0]])
        self.image = "https://cdn.discordapp.com/attachments/837490345486712840/966810133562789888/Tlallassa.png"
    def Attack(self , tick : int , competence : str):
        at = attack(self.Competences , self.statistiques , tick , getAttackCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
    def help(self):
        return self.Competences[0][1][0] + " : " + self.Competences[0][1][1] + " , " + self.Competences[1][1][0] + " : " + self.Competences[1][1][1] + " , " + self.Competences[2][1][0] + " : " + self.Competences[2][1][1] + " , " + self.Competences[3][1][0] + " : " + self.Competences[3][1][1] + "."
    def helpCompetence(self , Competence : str):
        indice = getAttackCompetenceIndice(Competence , self.Competences)
        txt = ["--"+Competence+"--" + ":" , " Po:" + str(self.Competences[indice][0][0]*100) + " ," , " Ppr:" + str(self.Competences[indice][0][1]*100) + " ," , " Pp:" + str(self.Competences[indice][0][2]*100) , " ;" + " Cd:" + str(self.Competences[indice][2][0])]
        return txt[0] , txt[1] , txt[2] , txt[3] , txt[4]


class Triiana(Weapon):
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list , stats : list):
        super().__init__(Name , Categorie , Palier , Infusion , Maitrise)
        self.type_stats = [13, 0, 5, 0, 0]
        self.depo = self.catg_stats[4] + self.type_stats[4] + stats[4]
        self.po = self.catg_stats[0] + self.type_stats[0] + stats[0] + self.maitrise[0]
        self.ppr = self.catg_stats[1] + self.type_stats[1] + stats[1] + self.maitrise[1]
        self.pst = self.catg_stats[2] + self.type_stats[2] + stats[2] + self.maitrise[2]
        self.pp = self.catg_stats[3] + self.type_stats[3] + stats[3] + self.maitrise[3]
        self.statistiques = [self.po,self.ppr,self.pst,self.pp,self.depo]
        self.Competences = ([[0.4,1,0.1],["tranchant","attaque basique a la Dovoke"],[1,-1],[False,0]],
              [[1.7,0.8,1],["Celestial","Coup circulaire"],[9,-9],[False,0]],
              [[1.2,1.4,1.2],["couperet","coup vertical"],[6,-6],[False,0]],
              [[0.8,1.2,0.4],["apostat","coup direct"],[2,-2],[False,0]])
        self.image = "https://cdn.discordapp.com/attachments/837490345486712840/966810200457748505/Triiana.png"
    def Attack(self , tick : int , competence : str):
        at = attack(self.Competences , self.statistiques , tick , getAttackCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
    def help(self):
        return self.Competences[0][1][0] + " : " + self.Competences[0][1][1] + " , " + self.Competences[1][1][0] + " : " + self.Competences[1][1][1] + " , " + self.Competences[2][1][0] + " : " + self.Competences[2][1][1] + " , " + self.Competences[3][1][0] + " : " + self.Competences[3][1][1] + "."
    def helpCompetence(self , Competence : str):
        indice = getAttackCompetenceIndice(Competence , self.Competences)
        txt = ["--"+Competence+"--" + ":" , " Po:" + str(self.Competences[indice][0][0]*100) + " ," , " Ppr:" + str(self.Competences[indice][0][1]*100) + " ," , " Pp:" + str(self.Competences[indice][0][2]*100) , " ;" + " Cd:" + str(self.Competences[indice][2][0])]
        return txt[0] , txt[1] , txt[2] , txt[3] , txt[4]


class Easthee(Weapon):
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list , stats : list):
        super().__init__(Name , Categorie , Palier , Infusion , Maitrise)
        self.type_stats = [0, 4, 2, 2, 0]
        self.depo = self.catg_stats[4] + self.type_stats[4] + stats[4]
        self.po = self.catg_stats[0] + self.type_stats[0] + stats[0] + self.maitrise[0]
        self.ppr = self.catg_stats[1] + self.type_stats[1] + stats[1] + self.maitrise[1]
        self.pst = self.catg_stats[2] + self.type_stats[2] + stats[2] + self.maitrise[2]
        self.pp = self.catg_stats[3] + self.type_stats[3] + stats[3] + self.maitrise[3]
        self.statistiques = [self.po,self.ppr,self.pst,self.pp,self.depo]
        self.Competences = ([[0.4,1,0.1],["tranchant","attaque basique a la Dovoke"],[1,-1],[False,0]],
              [[1.7,0.8,1],["Celestial","Coup circulaire"],[9,-9],[False,0]],
              [[1.2,1.4,1.2],["couperet","coup vertical"],[6,-6],[False,0]],
              [[0.8,1.2,0.4],["apostat","coup direct"],[2,-2],[False,0]])
        self.image = "https://cdn.discordapp.com/attachments/837490345486712840/968514012960653322/Collier_dEasthee.png"
    def Attack(self , tick : int , competence : str):
        at = attack(self.Competences , self.statistiques , tick , getAttackCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
    def help(self):
        return self.Competences[0][1][0] + " : " + self.Competences[0][1][1] + " , " + self.Competences[1][1][0] + " : " + self.Competences[1][1][1] + " , " + self.Competences[2][1][0] + " : " + self.Competences[2][1][1] + " , " + self.Competences[3][1][0] + " : " + self.Competences[3][1][1] + "."
    def helpCompetence(self , Competence : str):
        indice = getAttackCompetenceIndice(Competence , self.Competences)
        txt = ["--"+Competence+"--" + ":" , " Po:" + str(self.Competences[indice][0][0]*100) + " ," , " Ppr:" + str(self.Competences[indice][0][1]*100) + " ," , " Pp:" + str(self.Competences[indice][0][2]*100) , " ;" + " Cd:" + str(self.Competences[indice][2][0])]
        return txt[0] , txt[1] , txt[2] , txt[3] , txt[4]


class Ehara(Weapon):
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list , stats : list):
        super().__init__(Name , Categorie , Palier , Infusion , Maitrise)
        self.type_stats = [4, 11, 0, 2, 0]
        self.depo = self.catg_stats[4] + self.type_stats[4] + stats[4]
        self.po = self.catg_stats[0] + self.type_stats[0] + stats[0] + self.maitrise[0]
        self.ppr = self.catg_stats[1] + self.type_stats[1] + stats[1] + self.maitrise[1]
        self.pst = self.catg_stats[2] + self.type_stats[2] + stats[2] + self.maitrise[2]
        self.pp = self.catg_stats[3] + self.type_stats[3] + stats[3] + self.maitrise[3]
        self.statistiques = [self.po,self.ppr,self.pst,self.pp,self.depo]
        self.Competences = ([[0.4,1,0.1],["tranchant","attaque basique a la Dovoke"],[1,-1],[False,0]],
              [[1.7,0.8,1],["Celestial","Coup circulaire"],[9,-9],[False,0]],
              [[1.2,1.4,1.2],["couperet","coup vertical"],[6,-6],[False,0]],
              [[0.8,1.2,0.4],["apostat","coup direct"],[2,-2],[False,0]])
        self.image = "https://cdn.discordapp.com/attachments/837490345486712840/966810661696974918/Ehara.png"
    def Attack(self , tick : int , competence : str):
        at = attack(self.Competences , self.statistiques , tick , getAttackCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
    def help(self):
        return self.Competences[0][1][0] + " : " + self.Competences[0][1][1] + " , " + self.Competences[1][1][0] + " : " + self.Competences[1][1][1] + " , " + self.Competences[2][1][0] + " : " + self.Competences[2][1][1] + " , " + self.Competences[3][1][0] + " : " + self.Competences[3][1][1] + "."
    def helpCompetence(self , Competence : str):
        indice = getAttackCompetenceIndice(Competence , self.Competences)
        txt = ["--"+Competence+"--" + ":" , " Po:" + str(self.Competences[indice][0][0]*100) + " ," , " Ppr:" + str(self.Competences[indice][0][1]*100) + " ," , " Pp:" + str(self.Competences[indice][0][2]*100) , " ;" + " Cd:" + str(self.Competences[indice][2][0])]
        return txt[0] , txt[1] , txt[2] , txt[3] , txt[4]


class Yagi(Weapon):
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list , stats : list):
        super().__init__(Name , Categorie , Palier , Infusion , Maitrise)
        self.type_stats = [4, 5, 2, 6, 0]
        self.depo = self.catg_stats[4] + self.type_stats[4] + stats[4]
        self.po = self.catg_stats[0] + self.type_stats[0] + stats[0] + self.maitrise[0]
        self.ppr = self.catg_stats[1] + self.type_stats[1] + stats[1] + self.maitrise[1]
        self.pst = self.catg_stats[2] + self.type_stats[2] + stats[2] + self.maitrise[2]
        self.pp = self.catg_stats[3] + self.type_stats[3] + stats[3] + self.maitrise[3]
        self.statistiques = [self.po,self.ppr,self.pst,self.pp,self.depo]
        self.Competences = ([[0.4,1,0.1],["tranchant","attaque basique a la Dovoke"],[1,-1],[False,0]],
              [[1.7,0.8,1],["Celestial","Coup circulaire"],[9,-9],[False,0]],
              [[1.2,1.4,1.2],["couperet","coup vertical"],[6,-6],[False,0]],
              [[0.8,1.2,0.4],["apostat","coup direct"],[2,-2],[False,0]])
        self.image = "https://cdn.discordapp.com/attachments/837490345486712840/925844398305071134/Inconnu.png"
    def Attack(self , tick : int , competence : str):
        at = attack(self.Competences , self.statistiques , tick , getAttackCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
    def help(self):
        return self.Competences[0][1][0] + " : " + self.Competences[0][1][1] + " , " + self.Competences[1][1][0] + " : " + self.Competences[1][1][1] + " , " + self.Competences[2][1][0] + " : " + self.Competences[2][1][1] + " , " + self.Competences[3][1][0] + " : " + self.Competences[3][1][1] + "."
    def helpCompetence(self , Competence : str):
        indice = getAttackCompetenceIndice(Competence , self.Competences)
        txt = ["--"+Competence+"--" + ":" , " Po:" + str(self.Competences[indice][0][0]*100) + " ," , " Ppr:" + str(self.Competences[indice][0][1]*100) + " ," , " Pp:" + str(self.Competences[indice][0][2]*100) , " ;" + " Cd:" + str(self.Competences[indice][2][0])]
        return txt[0] , txt[1] , txt[2] , txt[3] , txt[4]


class Hassan(Weapon):
    def __init__(self, Name : str , Categorie : str , Palier : int , Infusion : str , Maitrise : list , stats : list):
        super().__init__(Name , Categorie , Palier , Infusion , Maitrise)
        self.type_stats = [6, 7, 0, 4, 2]
        self.depo = self.catg_stats[4] + self.type_stats[4] + stats[4]
        self.po = self.catg_stats[0] + self.type_stats[0] + stats[0] + self.maitrise[0]
        self.ppr = self.catg_stats[1] + self.type_stats[1] + stats[1] + self.maitrise[1]
        self.pst = self.catg_stats[2] + self.type_stats[2] + stats[2] + self.maitrise[2]
        self.pp = self.catg_stats[3] + self.type_stats[3] + stats[3] + self.maitrise[3]
        self.statistiques = [self.po,self.ppr,self.pst,self.pp,self.depo]
        self.Competences = ([[0.4,1,0.1],["tranchant","attaque basique a la Dovoke"],[1,-1],[False,0]],
              [[1.7,0.8,1],["Celestial","Coup circulaire"],[9,-9],[False,0]],
              [[1.2,1.4,1.2],["couperet","coup vertical"],[6,-6],[False,0]],
              [[0.8,1.2,0.4],["apostat","coup direct"],[2,-2],[False,0]])
        self.image = "https://cdn.discordapp.com/attachments/837490345486712840/966810746010861628/Hassan.png"
    def Attack(self , tick : int , competence : str):
        at = attack(self.Competences , self.statistiques , tick , getAttackCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
    def help(self):
        return self.Competences[0][1][0] + " : " + self.Competences[0][1][1] + " , " + self.Competences[1][1][0] + " : " + self.Competences[1][1][1] + " , " + self.Competences[2][1][0] + " : " + self.Competences[2][1][1] + " , " + self.Competences[3][1][0] + " : " + self.Competences[3][1][1] + "."
    def helpCompetence(self , Competence : str):
        indice = getAttackCompetenceIndice(Competence , self.Competences)
        txt = ["--"+Competence+"--" + ":" , " Po:" + str(self.Competences[indice][0][0]*100) + " ," , " Ppr:" + str(self.Competences[indice][0][1]*100) + " ," , " Pp:" + str(self.Competences[indice][0][2]*100) , " ;" + " Cd:" + str(self.Competences[indice][2][0])]
        return txt[0] , txt[1] , txt[2] , txt[3] , txt[4]




class Armor():
    def __init__(self, Palier : int , Categorie : str):
        self.palier = Palier
        self.categorie = Categorie
        self.catg_stat = getCatArm(Categorie , Palier)
    def setLevel(self, Palier : int):
        self.palier = Palier
        self.catg_stat = getCatArm(self.categorie , Palier)


class User():
    def __init__(self, name : str , maxhp : int , Level : int , Palier : str):
        self.name = name
        self.hp = maxhp
        self.maxhp = maxhp
        self.lv = Level
        self.pal = Palier
        self.Competences = ([[1],["parade","parade"],[6,-6],[False,0]],
              [[0.4],["reset cd","reset cd"],[0,0],[False,0]],
              [[1],["drill","drill"],[8,-8],[False,0]],
              [[1],["a buff , e buff","buff"],[22,-22],[False,0]])
        self.moveCompetences = ([[1],["dash","dash"],[6,-6],[True,0]],
              [[1],["destrier de poussiere","invoque un destrier de poussiere"],[0,0],[True,0]])
    def use(self , tick : int , competence : str):
        at = useMoveCompetence(self.Competences , tick , getCompetenceIndice(competence , self.Competences))
        return at[0] , at[1] , at[2]
        



def createNewWeapon(Type : str , Name : str , Categorie : str , Palier : int , stats : list ):
    if Type == "Dovoke":
        return Dovoke(Name , Categorie , Palier , "none" , [0,0,0,0,0] , stats)
    if Type == "Hirokami":
        return Hirokami(Name , Categorie , Palier , "none" , [0,0,0,0,0] , stats)
    if Type == "Kataro":
        return Kataro(Name , Categorie , Palier , "none" , [0,0,0,0,0] , stats)
    if Type == "Korechika":
        return Korechika(Name , Categorie , Palier , "none" , [0,0,0,0,0] , stats)
    if Type == "Riini":
        return Riini(Name , Categorie , Palier , "none" , [0,0,0,0,0] , stats)
    if Type == "Sekina":
        return Sekina(Name , Categorie , Palier , "none" , [0,0,0,0,0] , stats)
    if Type == "Sekriyina":
        return Sekriyina(Name , Categorie , Palier , "none" , [0,0,0,0,0] , stats)
    if Type == "Taviris":
        return Taviris(Name , Categorie , Palier , "none" , [0,0,0,0,0] , stats)
    if Type == "Thriallis":
        return Thriallis(Name , Categorie , Palier , "none" , [0,0,0,0,0] , stats)
    if Type == "Tlallassa":
        return Tlallassa(Name , Categorie , Palier , "none" , [0,0,0,0,0] , stats)
    if Type == "Triiana":
        return Triiana(Name , Categorie , Palier , "none" , [0,0,0,0,0] , stats)
    if Type == "Easthee":
        return Easthee(Name , Categorie , Palier , "none" , [0,0,0,0,0] , stats)
    if Type == "Ehara":
        return Ehara(Name , Categorie , Palier , "none" , [0,0,0,0,0] , stats)
    if Type == "Yagi":
        return Yagi(Name , Categorie , Palier , "none" , [0,0,0,0,0] , stats)
    if Type == "Hassan":
        return Hassan(Name , Categorie , Palier , "none" , [0,0,0,0,0] , stats)
