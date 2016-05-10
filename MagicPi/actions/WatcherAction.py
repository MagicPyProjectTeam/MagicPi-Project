import pathos.multiprocessing as mp
import os
import time

class WatcherAction:

    environement = None

    def __init__(self, Environement):
        self.environement = Environement

    def run(self):
        pool = mp.ProcessingPool(nodes=1)
        pool.amap(WatcherAction.asynchWatcher, [self])
        print "[*] Watcher is running in background..."

    def asynchWatcher(self):
        # On recupere une premiere fois les infos :
        modelHostInfo = self.environement.getStatic("HostInformation")
        networkRef = dict(modelHostInfo.interfaces) # dict pour faire une copie

        # On verifie toutes les 20 secondes que rien n'a change dans le network
        while (modelHostInfo.interfaces == networkRef) :
            time.sleep(20)
            modelHostInfo.loadInformation()
            if(self.environement.isDebug()) :
                print "[Background] Watcher is watching..."

        # Vu que ca a ete modifie, on relance l'appli
        print "\n\n\t<==================>\n\n Watcher : Les infos ont change, on relance l'application"
        cmd = "pkill -f '^python.*main.py$' && python " + self.environement.appDir + "main.py &"
        os.system(cmd)
