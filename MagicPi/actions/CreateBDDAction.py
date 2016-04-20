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
        try:
            self.BDDmodel.createBDD()
        except:
            print('\033[1m' + '\033[91m' + '[x] Failed to create database...' + '\033[0m')
