class DhcpConfigModel:

    env = None

    def __init__(self, Environement):
        self.env = Environement


    def createFileConfig(self,HostInformationModel):
        return "Hello World";