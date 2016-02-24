class SelectAction:

    env = None
    BDDmodel = None

    def __init__(self, Environement):
        self.env = Environement
        self.BDDmodel = self.env.getModel('BDD')

    def run(self):
        #select = self.BDDmodel.selectFromBDD('scan')
        print('\033[1m' + '--------------------------------------------\n'
                          '[*] SelectAction running. It will print All zombies found.\n' + '\033[0m')
        for row in self.BDDmodel.selectFromBDD('scan').keys():
            if self.BDDmodel.selectFromBDD('scan')[row]['PORTS'] != 'None':
                print("Host ; %s is a zombie. Open ports : %s" % (self.BDDmodel.selectFromBDD('scan')[row]['IP'], self.BDDmodel.selectFromBDD('scan')[row]['PORTS']))
        print('\n')