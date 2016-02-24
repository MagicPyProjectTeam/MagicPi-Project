class HostAction:

    env = None
    HostInformation = None
    BDDmodel = None

    def __init__(self, Environement):
        self.env = Environement
        self.HostInformation = self.env.getModel('HostInformation')
        self.BDDmodel = self.env.getModel('BDD')

    def run(self):
        print('\033[1m' + '--------------------------------------------\n'
                          '[*] HostAction running. It will get All interfaces information.\n' + '\033[0m')

        for i in self.HostInformation.interfaces:
            if self.HostInformation.getGateWayForInterface(i):
                for j in self.HostInformation.getInfoForInterface(i):

                    iface = i
                    ip = j['addr']
                    netmask =j['netmask']
                    cidr = self.HostInformation.getCidrFromIp(netmask)
                    subnet = self.HostInformation.getSubnet(j['addr'], cidr)
                    broadcast = j['broadcast']
                    gateway = self.HostInformation.getGateWayForInterface(i)
                    pubip = self.HostInformation.getPublicIp(i)
                    print('[*] Interface : %s' % iface)
                    print('[*] Addresse IP : %s' % ip)
                    print('[*] Netmask : %s - CIDR : %s' % (netmask, cidr))
                    print('[*] Subnet : %s' % subnet)
                    print('[*] Broadcast : %s' % broadcast)
                    print('[*] Gateway : %s' % gateway)
                    print('[*] Public IP : %s' % pubip)

                    self.BDDmodel.hostInsertBDD(iface, ip, netmask, cidr, subnet, broadcast, gateway, pubip)




