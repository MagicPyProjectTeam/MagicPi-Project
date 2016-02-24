import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import pathos.multiprocessing as mp
from functools import partial

class TCPModel:

    env = None

    def __init__(self,Environement):
        self.env = Environement

    # retourne un array avec le port et un bool sur l'etat du port, ex: arr = TCP_Syn_Scan(53), arr[0]=53, arr[1]=True
    def TCP_Syn_Scan(self, ip, ports):
        pool = mp.ProcessingPool(nodes=4)
        func = partial(self.syn_scan_port, ip)
        result = pool.map(func, ports)
        return result

    def syn_scan_port(self, ip, port):
        # import scapy
        scap = self.env.getImport('scapy.all')
        scap.conf.verb = 0

        # port source random
        src_port = scap.RandShort()

        # on build le packet
        p = scap.IP(dst=ip)/scap.TCP(sport=src_port, dport=port, flags='S')
        
        # on send
        resp = scap.sr1(p, timeout=1)
        
        if str(type(resp)) == "<type 'NoneType'>":
            return [port, False]
        elif resp.haslayer(scap.TCP):
            if resp.getlayer(scap.TCP).flags == 0x12:
                # send reset tcp flag
                send_rst = scap.sr(scap.IP(dst=ip)/scap.TCP(sport=src_port, dport=port, flags='AR'), timeout=1)
                return [port,True]
            elif resp.getlayer(scap.TCP).flags == 0x14:
                return [port, False]
        return [port, False]

    def TCP_idle_scan(self, ip, zombie, ports):
        pool =  mp.ProcessingPool(nodes=4)
        func = partial(self.syn_scan_port_spoof, ip, zombie)
        result = pool.map(func, ports)
        return result 

    def syn_scan_port_spoof(self, ip, zombie, port):
        scap = self.env.getImport('scapy.all')

        src_port = scap.RandShort()

        # get zombie's IP id with a SYN/ACK
        p1 = sr1(IP(dst=zombie)/TCP(sport=12345,dport=(1234),flags="SA"),verbose=0)
        initial_id = p1.id

        print '[+] Zombie initial IP id', initial_id

        # SYN to target with spoofed IP from zombie
        p2 = send(IP(dst=target,src=zombie)/TCP(sport=12345,dport=(port),flags="S"),verbose=0)

        # SYN/ACK to zombie to see if it heard back from the target
        p3 = sr1(IP(dst=zombie)/TCP(sport=12345,dport=(1234),flags="SA"),verbose=0)
        final_id = p3.id

        print '[+] Zombie final IP id', final_id

        if final_id - initial_id < 2:
            print '[+] Port %d : closed' % port
        else:
            print '[+] Port %d : open' % port

    # check l'ip id seq
    def ipid_seq(self, host):
        scap = self.env.getImport('scapy.all')

        src_port = scap.RandShort()

        # envoie 1st syn ack
        reply1 = scap.sr1(scap.IP(dst=host)/scap.TCP(sport=src_port,flags="SA"), timeout=2)

        # 2nd syn ack
        scap.send(scap.IP(dst=host)/scap.TCP(sport=src_port,flags="SA"))

        # 3rd syn ack
        reply2 = scap.sr1(scap.IP(dst=host)/scap.TCP(sport=src_port,flags="SA"),timeout=2)

        if str(type(reply1)) == "<type 'NoneType'>":
            return False

        if reply2.id - reply1.id < 2:
            return True
        else:
            return False