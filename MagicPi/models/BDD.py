import sqlite3
import os
import datetime


class BDDModel:

    # Class constructor & BDD connection
    def __init__(self, Environement):
        if not os.path.exists('databases'):
            os.mkdir('databases')
        self.env = Environement
        self.conn = sqlite3.connect('databases/mpp.db')
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()

    # Check if an IP address already exist in the Scan table
    def checkIP(self, ip):

        self.c.execute('SELECT count (*) from Scan WHERE IP = "%s"' % ip)
        nb = (self.c.fetchone()[0])
        if nb == 1:
            return True
        elif nb == 0:
            return False

    # Check if a Interface already exist in the HostInfo table
    def checkIface(self, iface):

        for row in self.selectFromBDD('HostInfo').keys():
            if self.selectFromBDD('HostInfo')[row]['INTERFACE']:
                return True
            else:
                return False
        '''
        c = self.c
        c.execute('SELECT count(*) FROM HostInfo WHERE INTERFACE = "%s"' % iface)
        nb = (c.fetchone()[0])
        if nb == 1:
            return True
        elif nb == 0:
            return False
        '''

    # Insert in Database outputs from Scan action
    def scanInsertBDD(self, ip, mac, const, iface):

        c = self.c
        if self.checkIP(ip):
            c.execute('UPDATE Scan SET MAC="%s", CONST="%s", INTERFACE="%s" WHERE IP= "%s"' % (mac, const, iface, ip))
            if (self.env.isDebug()) :
                print("   --> Updating Database...")
        else:
            c.execute('INSERT INTO Scan (IP, MAC, CONST, INTERFACE) VALUES ("%s", "%s", "%s", "%s")' % (ip, mac, const, iface))
            if (self.env.isDebug()) :
                print("   --> Adding to Database...")
        self.conn.commit()

    # Insert in Database open ports and Zombie status
    def portInsertBDD(self, openports, ip):

        c = self.c
        if openports == "":
            c.execute('UPDATE Scan SET PORTS="%s", ZOMBIE=1 WHERE IP="%s"' % ('None', ip))
        else:
            c.execute('UPDATE Scan SET PORTS="%s", ZOMBIE=1 WHERE IP="%s"' % (openports, ip))
        self.conn.commit()

    # Insert in Database information from HostInformation model
    def hostInsertBDD(self, iface, ip, netmask, cidr, subnet, broadcast, gateway, pubip):
        if self.checkIface(iface):
            self.c.execute('UPDATE HostInfo SET '
                           'SSID="None", SUBNET="%s", MASK="%s", CIDR="%s", BROADCAST="%s", GATEWAY="%s", PUBIP="%s" '
                           'WHERE INTERFACE="%s"' % (subnet, netmask, cidr, broadcast, gateway, pubip, iface))
        else:
            self.c.execute('INSERT INTO HostInfo (INTERFACE, SSID, SUBNET, MASK, CIDR, BROADCAST, GATEWAY, PUBIP)'
                           ' VALUES ("%s", "None", "%s", "%s", "%s", "%s", "%s", "%s")' % (iface, subnet, netmask, cidr, broadcast, gateway, pubip))
        self.conn.commit()

    '''
    Return Dictionary (with Primary key for Index) of dictionaries (With Column name for Index) with Table as parameter
    Calling example : macAddr = selectFromBDD('Scan')['192.168.1.1']['MAC']
    '''
    def selectFromBDD(self, table,):

        listSelectDict = dict()
        self.c.execute('select * from "%s"' % table)
        select = self.c.fetchall()
        for row in select:
            selectDict = dict()
            for field in row.keys():
                selectDict[field] = str(row[field])
            try:
                listSelectDict[str(row['IP'])] = selectDict
            except:
                listSelectDict[str(row['INTERFACE'])] = selectDict
        return listSelectDict

    # Return first active Interface (which has a Gateway)
    def activeInterface(self):

        self.c.execute('select INTERFACE from HostInfo where Gateway != "None"')
        return str(self.c.fetchone()[0])

    # If BDD already exist it will remove it and create a new one
    def createBDD(self):
        self.removeBDD('databases/mpp.db')
        self.conn = sqlite3.connect('databases/mpp.db')
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()
        self.c.execute("create table Scan(IP TEXT,MAC TEXT,CONST TEXT,PORTS TEXT,ZOMBIE BOOLEAN NOT NULL DEFAULT 0,INTERFACE TEXT,FOREIGN KEY (INTERFACE) REFERENCES HostInfo(INTERFACE),PRIMARY KEY (IP));")
        self.c.execute("create table HostInfo(INTERFACE TEXT,SSID TEXT,SUBNET TEXT,MASK TEXT ,CIDR TEXT,BROADCAST,GATEWAY TEXT,PUBIP,PRIMARY KEY(INTERFACE));")
        self.conn.commit()

        if (self.env.isDebug()) :
            print('[*] Creating Databse...\n')

    def exportBDD(self, sourceFile, outputFile):
        os.rename(sourceFile, outputFile)
        if (self.env.isDebug()) :
            print('[*] The database was exported to database folder')

    def removeBDD(self, path):
        if os.path.isfile(path):
            self.conn.close()
            os.remove(path)
            if (self.env.isDebug()) :
                print('[*] Removing old Database...')

    # Clean all entries of Database (not used yet)
    def cleanBDD(self):

        self.c.execute('DELETE FROM Scan')
        self.c.execute('DELETE FROM HostInfo')

