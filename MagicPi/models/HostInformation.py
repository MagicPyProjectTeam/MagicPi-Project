class HostInformation:
    env = None;
    interfaces = {};
    netIfaces = None;

    #Constructeur de la classe, on appel loadInformation
    def __init__(self,Environement):
        self.env = Environement;
        self.netIfaces = Environement.getImport("netifaces");
        self.loadInformation();

    # Methode appele a la construction, instancie les parametres de l'interface
    def loadInformation(self):
        for interface_en_cours in self.netIfaces.interfaces() :
            self.interfaces[interface_en_cours] = self.netIfaces.ifaddresses(interface_en_cours);

    # Retourne la liste des interfaces
    def getInterfaces(self):
        return self.interfaces.keys();

    # Retourne les informations de l'interface
    def getInfoForInterface(self,interface):
        try:
            return self.interfaces[interface][self.netIfaces.AF_INET];
        except:
            return False

    #retourne le CIDR
    def getCidrFromIp(self,ip):
        return '/'+str('.'.join([bin(int(x)+256)[3:] for x in ip.split('.')]).count('1'));

    # Retourne le gateWay de l'interface si possible, false sinon (default est une valeur possible)
    def getGateWayForInterface(self,interface):
        for gateway_ip, network_card, is_default in self.netIfaces.gateways()[self.netIfaces.AF_INET]:
            if network_card == interface:
                return gateway_ip
        return False;