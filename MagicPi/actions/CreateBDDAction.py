import os

class createBDDAction:

    env = None
    BDDmodel = None

    def __init__(self, Environement):
        self.env = Environement
        self.BDDmodel = self.env.getModel('BDD')

    def run(self):
        print('\033[1m' + '--------------------------------------------\n'
                          '[*] CreateBDDAction running. It will create the database.\n' + '\033[0m')
        self.BDDmodel.createBDD()