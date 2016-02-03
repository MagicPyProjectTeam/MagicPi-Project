class ARPModel:

    env = None;

    def __init__(self,Environement):
        self.env = Environement;

    def PerformArpPing(self, interface, range):
        # import scapy
        scap = self.env.getImport('scapy.all');
        
        # charge un tableau avec les prefix mac  de nmap
        filename = '/usr/share/nmap/nmap-mac-prefixes'
        # '/usr/local/share/nmap/nmap-mac-prefixes'
        vals = {}
        with open(filename) as myFile:
            for line in myFile.readlines():        
                vals[line[:6]] = line[7:-1]

        # On envoie les packets
        conf.verb = 0
        ans, unans = scap.srp(scap.Ether(dst="ff:ff:ff:ff:ff:ff")/scap.ARP(pdst = range), timeout = 2, iface=interface, inter=0.25)

        #initialise un tableau de retour
        array = []

        # Parsing des packets recus
        for snd,rcv in ans:
            mac = rcv.sprintf(r"%Ether.src%").replace(":", "")[:6].upper()
            dico = {}
            dico["ip"] = rcv.sprintf(r"%ARP.psrc%")
            dico["mac"] = rcv.sprintf(r"%ARP.psrc%")
            dico["const"] = "(%s)" % vals[mac] if mac in vals else 'not found'
            array.append(dico)
        return array