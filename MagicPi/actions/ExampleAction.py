class ExampleAction:
    """Same ClassName as FileName.py"""

    env = None;
    modelExample = None;

    def __init__(self,Environement):
        self.env = Environement;
        self.modelExample = self.env.getModel('ExampleModel');

    def run(self):
        print(self.modelExample.getHelloWorld());
        print 'On tente l\'import de scappy : ';
        self.modelExample.exmapleGetScapyAndSend();
