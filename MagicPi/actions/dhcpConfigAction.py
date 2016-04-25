class dhcpConfigAction:

    env = None
    os = None

    def __init__(self, Environement):
        self.env = Environement
        self.os = self.env.getImport('os')

    # Cree le fichier de configuration DHCP
    # Attention, le fichier dhcpd.conf dois exister (initialise a l'installation de isc-dhcp-server)
    def run(self):
        print('\033[1m' + "--------------------------------------------\n"
                  "[*] Dhcp configuration is running\n" + '\033[0m')
        modelDhcpConfig = self.env.getModel('DhcpConfig');

        ### En travail
        #
        # On recupere le fichier
        fileContent = modelDhcpConfig.getFileConfig();
        # On ecris sur le disque apres avoir fais une copie
        cmd = 'find /etc/ -name dhcpd.conf -exec mv {} {}.bak \; -exec bash -c "echo \''+fileContent+'\' > {}" \;'
        self.os.system(cmd);
