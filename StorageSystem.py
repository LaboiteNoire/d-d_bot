import pickle
import io
import os

def saveDict(Dictionnaire : dict):
    fileIn = open(b"databaseDictionnary.obj","wb")
    pickle.dump(Dictionnaire,fileIn)
    fileIn.close()
def loadDict():
    fileout = open("databaseDictionnary.obj","rb")
    Load = pickle.load(fileout)
    fileout.close()
    return Load

def updateValue(Dictionnaire : dict , display_name : str , value):
    if os.path.getsize("databaseDictionnary.obj") == 0:
        Dictionnaire[display_name] = value
    else:
        Dictionnaire = loadDict()
        Dictionnaire[display_name] = value
        saveDict(Dictionnaire)
def addUser(Dictionnaire : dict , display_name : str , value):
    if (display_name in Dictionnaire):
        pass
    else:
        Dictionnaire[display_name] = value
def deleteUser(Dictionnaire : dict , display_name : str):
    del Dictionnaire[display_name]
def researchUser(Dictionnaire : dict , display_name : str):
    return display_name in Dictionnaire
def dirUser(Dictionnaire : dict , display_name : str):
    return Dictionnaire.get(display_name , 'none')




