class SelectAction:

    env = None
    BDDmodel = None

    def __init__(self, Environement):
        self.env = Environement
        self.BDDmodel = self.env.getModel('BDD')

    def run(self):
        print('\033[1m' + '--------------------------------------------\n'
                          '[*] SelectAction running. It will print All zombies found.\n' + '\033[0m')
        for row in self.BDDmodel.selectFromBDD('scan').keys():
            ports = self.BDDmodel.selectFromBDD('scan')[row]['PORTS']
            zombie = self.BDDmodel.selectFromBDD('scan')[row]['ZOMBIE']
            if  ports != 'None' and zombie == 1:
                print('\033[1m' + "[*] Host: %s is a zombie - Open ports : %s\n" % (self.BDDmodel.selectFromBDD('scan')[row]['IP'], self.BDDmodel.selectFromBDD('scan')[row]['PORTS']) + '\033[1m')
