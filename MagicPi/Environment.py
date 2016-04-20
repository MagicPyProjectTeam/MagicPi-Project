import models
import inspect
from importlib import import_module

class Environment:

    # Classes statiques
    statics = {};

    # Imports
    importList = {};

    # Variables outil
    debug = False;

    def __init__(self):
        print ("\n[*] Environment loaded!\n")

    # initialise les classes statiques
    def initializeStatic(self,staticName):
        self.statics[staticName] = self.getModel(staticName)

    # Retourne la class static
    def getStatic(self,staticName):
        print ("Chargement de la class static : "+staticName)
        return self.statics[staticName]

    # Retourne un une instance du model voulu
    def getModel(self,modelName):
        if self.debug :
            print ("Chargement du model "+modelName)
            print(modelName);
        modelClass = inspect.getmembers(getattr(models, modelName))[0][1]
        return modelClass(self);

    def getImport(self,importName):
        if not importName in self.importList.keys() :
            self.importList[importName] = import_module(importName)
        return self.importList[importName]

    # Methods : Execute l'action run des classes du module
    def runActions(self, module):
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                if self.debug:
                    print("Run de :")
                    print (obj)
                actionClass = obj(self)
                actionClass.run()

    # Appel la methode runActions pour chaque module de l'import
    def launchApplication(self, import_name):
        memberDict = dict()
        for name, obj in inspect.getmembers(import_name):
            if inspect.ismodule(obj):
                if self.debug:
                    print ("Lancement de runActions pour :")
                    print(obj)
                print name
                memberDict[name] = obj
        list=['CreateBDDAction', 'HostAction', 'ScanAction', 'SelectAction', 'DeleteBDDAction']
        for module in list:
            self.runActions(memberDict[module])

    # On instancie une premiere fois les classes statiques
    def setStatics(self):
        list=['HostInformation', 'ARP', 'TCP', 'BDD']
        for model in list:
            self.initializeStatic(model)
