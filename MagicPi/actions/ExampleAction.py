class ExampleAction:
    """Same ClassName as FileName.py"""

    env = None;

    def __init__(self,Environement):
        self.env = Environement;

    def run(self):
        print(self.env.getModel('ExampleModel').getHelloWorld());
