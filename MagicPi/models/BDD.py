import sqlite3


class BDDModel:

    # Class constructor & BDD connection
    def __init__(self, Environement):
        self.env = Environement
        self.conn = sqlite3.connect('mpp.db')
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
    def checkSSID(self, ssid):

        c = self.c
        c.execute('SELECT count(*) FROM Networks WHERE SSID = "%s"' % ssid)
        nb = (c.fetchone()[0])
        if nb == 1:
            return True
        elif nb == 0:
            return False

    # Insert in Database outputs from Scan action
    def scanInsertBDD(self, ip, mac, const):

        c = self.c
        if self.checkIP(ip):
            c.execute('UPDATE Scan SET MAC="%s", CONST="%s" WHERE IP= "%s"' % (mac, const, ip))
            # print("   --> Updating Database...")
        else:
            c.execute('INSERT INTO Scan (IP, MAC, CONST) VALUES ("%s", "%s", "%s")' % (ip, mac, const))
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
