class ScanAction:

    env = None
    ARPmodel = None
    TCPmodel = None

    def __init__(self,Environement):
        self.env = Environement
        self.ARPmodel = self.env.getModel('ARP')
        self.TCPmodel = self.env.getModel('TCP')

    def run(self):
        print "[*] ScanAction Running, It will perform ARP ping scan, then for each host, it will scan range 1-1024 tcp ports (SYN_SCAN)";
        
        print "[*] ARP ping begin.."
        hosts = self.ARPmodel.ARP_Ping('eth0','10.75.1.0/22');
        
        print "[*] ARP ping done!, discovered %d host(s) !" % len(hosts)
        for host in hosts:
            print "[*] Found Host=%s, MAC=%s, Constructor=%s" % (host["ip"],host["mac"],host["const"])
        
        print "[*] IP ID Seq Scan begin.."
        for host in hosts:
            print "[*] Scanning host:%s" % host["ip"]
            
            if(self.TCPmodel.ipid_seq(host["ip"])):
                print "[*] IP ID Seq Incremental Detected!"
            
                ports = self.TCPmodel.TCP_Syn_Scan(host["ip"], range(1, 1025))
                openports = ''
                for openp in filter(lambda i: i[1] == True, ports):
                    openports += str(openp[0]) + ','
                    print "[*] Discover open port: {} in host: {}".format(openp[0],host["ip"])
                openports = openports[:-1]
            print "[*] Host:%s scan done!" % host["ip"]

        print "[*] IP ID Seq Scan done!"

        print "[*] ScanAction Finished! GoodBye Master!"