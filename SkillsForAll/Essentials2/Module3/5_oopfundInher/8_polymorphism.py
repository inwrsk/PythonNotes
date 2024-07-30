class One:
    def do_it(self):
        print("do_it from One")
    def doanything(self):
        self.do_it()

class Two(One):
    def do_it(self):
        print("do_it from Two")

two = Two()#subclass is able to change the superclass behaviour
two.doanything()#do_it from Two