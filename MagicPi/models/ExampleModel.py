class ExampleModel:

    env = None;

    def __init__(self,Environement):
        self.env = Environement;

    def getHelloWorld(self):
        return "Hello World !";

    def exmapleGetScapyAndSend(self):
        scapytest = self.env.getImport('scapy.all');
        return scapytest.srp(scapytest.Ether(dst="ff:ff:ff:ff:ff:ff")/scapytest.ARP(pdst = '127.0.0.1'), timeout = 2, iface='eth0',inter=0.25);