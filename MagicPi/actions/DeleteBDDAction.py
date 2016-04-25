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
        name = ("databases/%s_%s-%s-%s.db" % (str(time.date()), str(time.hour), str(time.minute), str(time.second)))
        try:
            self.BDDmodel.exportBDD('databases/mpp.db', name)
        except:
            print('\033[1m' + '\033[91m' + '[x] Failed to export database...' + '\033[0m')

        try:
            self.BDDmodel.removeBDD('databases/mpp.db')
        except:
            print('\033[1m' + '\033[91m' + '[x] Failed to delete database...' + '\033[0m')

        #print('[*] Exporting data to remote server...')
        os.system('chown -R magicpi /home/magicpi/MagicPi-Project')
