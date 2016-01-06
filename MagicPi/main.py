# Imports
from tendo import singleton;
import inspect;
import actions;

# Singleton : will sys.exit(-1) if other instance is running
me = singleton.SingleInstance();

# Methods : Execute l'action run des classes du module
def runClasses(module):
    for name, obj in inspect.getmembers(module): # what do I do here?
        if inspect.isclass(obj):
            actionClass = obj();
            actionClass.run();

# Algo : Pour chaque modules dans actions, appel runClass
for name, obj in inspect.getmembers(actions):
    if inspect.ismodule(obj):
        runClasses(obj);