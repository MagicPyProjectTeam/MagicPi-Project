import sqlite3


class Bdd:

    conn = sqlite3.connect('mpp.db')
    c = conn.cursor()

    def __init__(self, Environement):
        self.env = Environement;

    def checkMAC(self, mac):

        c = self.c
        c.execute("SELECT count (*) from Hosts WHERE MAC = '{}'".format(mac))
        boolResult=(c.fetchone()[0])

        if boolResult == 1:
            return True
        elif boolResult ==0:
            return False

    def checkNET(self, ssid):

        c = self.c
        c.execute("SELECT count(*) FROM Networks WHERE SSID = '{}'".format(ssid))
        boolResult=(c.fetchone()[0])

        if boolResult == 1:
            return True
        elif boolResult == 0:
            return False

    def arpInsertBDD(self, ip, mac, const):

        c = self.c

        if self.checkMAC(mac):
            c.execute("UPDATE Hosts SET IP='{}'".format(ip))
            print("Updating {} device info".format(mac))
        else:
            c.execute("INSERT INTO Hosts VALUES ('{}', '{}', '{}')".format(mac, ip, const))
            print("Adding {} device info".format(mac))

obj = Bdd("arg a la con")
obj.arpInsertBDD("192.168.1.42", "ff:ff:ff:ff:ff", "Cisco")
Bdd.conn.commit()
Bdd.conn.close()
