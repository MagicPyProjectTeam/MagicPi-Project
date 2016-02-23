class HostInformation:
    env = None
    interfaces = {}
    netIfaces = None
    ifaceUsed = None

    # Constructeur de la classe, on appel loadInformation
    def __init__(self,Environement):
        self.env = Environement;
        self.netIfaces = Environement.getImport("netifaces");
        self.loadInformation();

    # Recupere, si possible, l'ip publique lie a l'interface donnee
    def getPublicIp(self, interface):
        # On recupere les import
        PyCurl = self.env.getImport('pycurl');
        stringIo = self.env.getImport('StringIO')
        # stringIO permettra a curl de stocker le resultat plutot que de l'afficher
        tmpStorage = stringIo.StringIO()

        # On intialise curl
        curlConn = PyCurl.Curl();
        curlConn.setopt(PyCurl.URL, '52.28.249.93/ip'); # retourne l'ip publique (ipinfo.io)
        curlConn.setopt(PyCurl.CONNECTTIMEOUT, 5) # On met un timeout de 5 secondes
        curlConn.setopt(PyCurl.INTERFACE, interface) # On map avec l'interface
        curlConn.setopt(PyCurl.WRITEFUNCTION, tmpStorage.write) # On redirige le flux vers stringIO
        try :
            # On execute et on recupere le retour
            curlConn.perform();
            retour = tmpStorage.getvalue();
        except:
            # Sinon le retour est False
            retour = False;
        # On ferme la connexion, et on fais le retour
        curlConn.close();
        return retour;

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
    def getCidrFromIp(self, ip):
        return '/'+str('.'.join([bin(int(x)+256)[3:] for x in ip.split('.')]).count('1'));

    def getSubnet(self, ip, cidr):
        ipCalc = self.env.getImport('ipcalc')
        return str(ipCalc.Network('%s%s' % (ip, cidr)).network())

    # Retourne le gateWay de l'interface si possible, false sinon (default est une valeur possible)
    def getGateWayForInterface(self,interface):
        for gateway_ip, network_card, is_default in self.netIfaces.gateways()[self.netIfaces.AF_INET]:
            if network_card == interface:
                return gateway_ip
