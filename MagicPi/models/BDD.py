import sqlite3
class BDDModel:

    # Class constructor & BDD connection
    def __init__(self, Environement):
        self.env = Environement
        self.conn = sqlite3.connect('mpp.db')
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()


    # Check if an address already exist in the Scan table
    def checkIP(self, ip):

        self.c.execute('SELECT count (*) from Scan WHERE IP = "%s"' % ip)
        nb = (self.c.fetchone()[0])


        if nb == 1:
            return True
        elif nb == 0:
            return False

    # Check if a SSID address already exist in the Networks table
    def checkIface(self, iface):

        c = self.c
        c.execute('SELECT count(*) FROM HostInfo WHERE INTERFACE = "%s"' % iface)
        nb = (c.fetchone()[0])
        if nb == 1:
            return True
        elif nb == 0:
            return False

    # Insert in Database outputs from Scan action
    def scanInsertBDD(self, ip, mac, const, iface):

        c = self.c
        if self.checkIP(ip):
            c.execute('UPDATE Scan SET MAC="%s", CONST="%s" WHERE IP= "%s", INTERFACE="%s"' % (mac, const, ip, iface))
            # print("   --> Updating Database...")
        else:
            c.execute('INSERT INTO Scan (IP, MAC, CONST, INTERFACE) VALUES ("%s", "%s", "%s", "%s")' % (ip, mac, const, iface))
            # print("   --> Adding to Database...")
        self.conn.commit()

    # Insert in Database open ports and Zombie status
    def portInsertBDD(self, openports, ip):

        c = self.c
        if openports == "":
            c.execute('UPDATE Scan SET PORTS="%s", ZOMBIE=1 WHERE IP="%s"' % ('None', ip))
        else:
            c.execute('UPDATE Scan SET PORTS="%s", ZOMBIE=1 WHERE IP="%s"' % (openports, ip))
        self.conn.commit()

    def hostInsertBDD(self, iface, ip, netmask, cidr, subnet, broadcast, gateway, pubip):
        if self.checkIface(iface):
            self.c.execute('UPDATE HostInfo SET '
                           'SSID="None", SUBNET="%s", MASK="%s", CIDR="%s", BROADCAST="%s", GATEWAY="%s", PUBIP="%s" '
                           'WHERE INTERFACE="%s"' % (subnet, netmask, cidr, broadcast, gateway, pubip, iface))
        else:
            self.c.execute('INSERT INTO HostInfo (INTERFACE, SSID, SUBNET, MASK, CIDR, BROADCAST, GATEWAY, PUBIP)'
                           ' VALUES ("%s", "None", "%s", "%s", "%s", "%s", "%s", "%s")' % (iface, subnet, netmask, cidr, broadcast, gateway, pubip))
        self.conn.commit()

    def selectFromBDD(self, table,):
        scanList = list()
        hostList = list()
        self.c.execute('select * from scan')
        scan = self.c.fetchall()
        for i in scan:
            dict = {'IP', 'MAC', 'CONST', 'PORTS', 'ZOMBIE', 'INTERFACE'}



        return obj[item]

    def cleanBDD(self):

        self.c.execute('DELETE FROM Scan')
        self.c.execute('DELETE FROM HostInfo')

