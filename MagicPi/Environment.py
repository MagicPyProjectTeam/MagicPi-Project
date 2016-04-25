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

    # List of actions in the rifht order
    actionsList=['WatcherAction','CreateBDDAction', 'HostAction', 'SshAction', 'ScanAction', 'SelectAction', 'dhcpConfigAction', 'DeleteBDDAction']

    def __init__(self):
        print ("\n[*] Environment loaded !\n")

    # initialise les classes statiques
    def initializeStatic(self,staticName):
        self.statics[staticName] = self.getModel(staticName)

    # Retourne la class static
    def getStatic(self,staticName):
        if self.debug :
            print ("[Env] Fetching static : "+staticName)
        return self.statics[staticName]

    # Retourne un une instance du model voulu
    def getModel(self,modelName):
        modelClass = inspect.getmembers(getattr(models, modelName))[0][1]
        if self.debug :
            print ("[Env] Model loaded : "+modelName)
        return modelClass(self);

    def getImport(self,importName):
        if not importName in self.importList.keys() :
            self.importList[importName] = import_module(importName)
        if(self.isDebug()) :
            print "[Env] Importing : "+str(importName)
        return self.importList[importName]

    # Methods : Execute l'action run des classes du module
    def runActions(self, module):
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                actionClass = obj(self)
                actionClass.run()

    # Appel la methode runActions pour chaque module de l'import
    def launchApplication(self, import_name):
        memberDict = dict()
        for name, obj in inspect.getmembers(import_name):
            if inspect.ismodule(obj):
                memberDict[name] = obj
        for module in self.actionsList:
            print ("\n\t\t#########################################################################")
            print ("\t\t## [Env] Launching : " + str(module))
            print ("\t\t#########################################################################\n")
            self.runActions(memberDict[module])

    # On instancie une premiere fois les classes statiques
    def setStatics(self):
        list=['HostInformation', 'ARP', 'TCP', 'BDD']
        for model in list:
            self.initializeStatic(model)

    def isDebug(self):
        return self.debug
