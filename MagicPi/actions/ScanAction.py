class ScanAction:

    env = None
    ARPmodel = None
    TCPmodel = None
    BDDmodel = None

    def __init__(self,Environement):
        self.env = Environement
        self.ARPmodel = self.env.getModel('ARP')
        self.TCPmodel = self.env.getModel('TCP')
        self.BDDmodel = self.env.getModel('BDD')

    def run(self):

        print('\033[1m' + "--------------------------------------------\n"
                          "[*] ScanAction Running, It will perform ARP ping scan, then for each host,"
                          " it will scan range 1-1024 tcp ports (SYN_SCAN)\n" + '\033[0m')
        
        print("[*] ARP ping begin..")
        iface = self.BDDmodel.activeInterface()
        subCIDR = self.BDDmodel.selectFromBDD('HostInfo')[iface]['SUBNET']+self.BDDmodel.selectFromBDD('HostInfo')[iface]['CIDR']
        hosts = self.ARPmodel.ARP_Ping(iface, subCIDR)

        print ("[*] ARP ping done!, discovered %d host(s) !" % len(hosts))
        for host in hosts:
            print ("\n[*] Found Host=%s, MAC=%s, Constructor=%s" % (host["ip"],host["mac"],host["const"]))
            try:
                self.BDDmodel.scanInsertBDD(str(host["ip"]), str(host["mac"]), str(host["const"]), iface)
            except:
                print('\033[1m' + '\033[91m' + '[x] Failed to insert into BDD...' + '\033[0m')
        
        print ("\n\n[*] IP ID Seq Scan begin..")
        for host in hosts:
            print("\n[*] Scanning host:%s" % host["ip"])
            
            if self.TCPmodel.ipid_seq(host["ip"]):

                print("[*] IP ID Seq Incremental Detected!")
            
                ports = self.TCPmodel.TCP_Syn_Scan(host["ip"], range(1, 1025))
                openports = ''
                for openp in filter(lambda i: i[1] == True, ports):
                    openports += str(openp[0]) + ','
                    print("[*] Discover open port: {} in host: {}".format(openp[0], host["ip"]))
                openports = openports[:-1]
                try:
                    self.BDDmodel.portInsertBDD(openports, host["ip"])
                except:
                    print('\033[1m' + '\033[91m' + '[x] Failed to insert into BDD...' + '\033[0m')

            print("[*] Host:%s scan done!" % host["ip"])

        print("[*] IP ID Seq Scan done!")

        print("[*] ScanAction Finished! GoodBye Master!\n")
