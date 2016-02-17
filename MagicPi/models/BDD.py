import sqlite3


class BDD:

    # Initialization of connection to Database
    conn = sqlite3.connect('mpp.db')
    c = conn.cursor()

    def __init__(self, Environement):
        self.env = Environement;

    # Check if a MAC address already exist in the Scan table
    def checkIP(self, ip):

        c = self.c
        c.execute("SELECT count (*) from Scan WHERE IP = '{}'".format(ip))
        nb=(c.fetchone()[0])

        if nb == 1:
            return True
        elif nb == 0:
            return False

    # Check if a SSID address already exist in the Networks table
    def checkSSID(self, ssid):

        c = self.c
        c.execute("SELECT count(*) FROM Networks WHERE SSID = '{}'".format(ssid))
        nb=(c.fetchone()[0])

        if nb == 1:
            return True
        elif nb == 0:
            return False

    # Insert in Database outputs from ARP action
    def arpInsertBDD(self, ip, mac, const):

        c = self.c

        if self.checkIP(ip):
            c.execute("UPDATE Scan SET IP='{}', MAC='{}', CONST='{}'".format(ip, mac, const))
            print("Updating {} device info".format(ip))
        else:
            c.execute("INSERT INTO Scan (IP, MAC, CONST) VALUES ('{}', '{}', '{}')".format(ip, mac, const))
            print("Adding {} device info".format(ip))

    def portInsertBDD(self, openports):

        if openports == "":
            self.c.execute("UPDATE Scan SET PORTS='{}' ZOMBIE='{}'".format('None', True))
        else:
            self.c.execute("UPDATE Scan SET PORTS='{}' ZOMBIE='{}'".format(openports, True))

obj = Bdd('')
Bdd.conn.commit()
Bdd.conn.close()