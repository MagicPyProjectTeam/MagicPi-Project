class dhcpConfigAction:

    env = None

    def __init__(self, Environement):
        self.env = Environement

    # Cree le fichier de configuration DHCP
    def run(self):
        modelDhcpConfig = self.env.getModel('DhcpConfig');
        HostInformation = self.env.getStatic('HostInformation');
        fileContent = modelDhcpConfig.createFileConfig(HostInformation);
        print (fileContent);
        exit(42);