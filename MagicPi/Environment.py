import models;
import inspect;

class Environment:

    # Classes statiques
    statics = [];
    # Variables outil
    debug = False;

    def __init__(self):
        print "Chargement de l'environement"

    # initialise les classes statiques
    def initializeStatic(self,staticName):
        self.statics[staticName] = self.getStatic(staticName);

    # Retourne la class static
    def getStatic(self,static):
        print "Chargement de la class static :"+static;

    # Retourne un une instance du model voulu
    def getModel(self,modelName):
        if(self.debug):
            print "Chargement du model "+modelName;
            print(modelName);
        modelClass = inspect.getmembers(getattr(models, modelName))[0][1]
        return modelClass(self);



    # Methods : Execute l'action run des classes du module
    def runActions(self,module):
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                if(self.debug):
                    print("Run de :")
                    print obj;
                actionClass = obj(self);
                actionClass.run();

    # Appel la methode runActions pour chaque module de l'import
    def launchApplication(self,import_name):
        for name, obj in inspect.getmembers(import_name):
            if inspect.ismodule(obj):
                if(self.debug):
                    print "Lancement de runActions pour :"
                    print(obj);
                self.runActions(obj);