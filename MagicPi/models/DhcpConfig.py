class DhcpConfigModel:

    env = None

    def __init__(self, Environement):
        self.env = Environement
        self.BDDmodel = self.env.getModel('BDD')
        self.HostInformationModel = self.env.getStatic('HostInformation')


    def getFileConfig(self):

        iface = self.BDDmodel.activeInterface()
        infoHost = self.BDDmodel.selectFromBDD('HostInfo');
        subnet = infoHost[iface]['SUBNET']
        mask = infoHost[iface]['MASK'];
        broadcast = infoHost[iface]['BROADCAST']
        localIp = self.HostInformationModel.getInfoForInterface(iface)[0]['addr'];
        rangeAdress = self.getRange(localIp);

        fileDhcp = 'default-lease-time 600;\n' \
                   'max-lease-time 7200;\n' \
                   'option subnet-mask '+mask+';\n' \
                   'option broadcast-address '+broadcast+';\n' \
                   'option domain-name-servers 8.8.8.8, 8.8.4.4;\n' \
                   'option routers '+localIp+';\n\n' \
                   'subnet '+subnet+' netmask '+mask+' {\n' \
                   '    range '+rangeAdress+';\n' \
                   '}\n' \
                   ''
        return fileDhcp;

    def getRange(self,addr):
        listNum = str(addr).split('.');
        base = listNum[0]+'.'+listNum[1]+'.'+listNum[2]
        return base+'.2 '+base +'.253'
