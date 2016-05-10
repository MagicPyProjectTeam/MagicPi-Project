import os
import datetime

class DeleteBDDAction:

    priority = 5
    env = None
    BDDmodel = None

    def __init__(self, Environement):
        self.env = Environement
        self.BDDmodel = self.env.getModel('BDD')

    def run(self):
        print('\033[1m' + '--------------------------------------------\n'
                          '[*] DeleteBDDAction running. It will remove database after exported it.\n' + '\033[0m')

        time = datetime.datetime.now()
        name = (self.BDDmodel.dbDir + "%s_%s-%s-%s.db" % (str(time.date()), str(time.hour), str(time.minute), str(time.second)))
        try:
            self.BDDmodel.exportBDD(self.BDDmodel.db, name)
        except:
            print('\033[1m' + '\033[91m' + '[x] Failed to export database...' + '\033[0m')

        print self.BDDmodel.db
        try:
            self.BDDmodel.removeBDD(self.BDDmodel.db)
        except:
            print('\033[1m' + '\033[91m' + '[x] Failed to delete database...' + '\033[0m')

        os.system('chmod -R 777 ' + self.env.appDir + '../')
