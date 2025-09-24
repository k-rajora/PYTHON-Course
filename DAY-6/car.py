class vechicle:       #-> this is a type hint [what type of date will the method /function return]
    def __init__(self,name : str,no_of_tyres : int) -> None:
        self.name : str = name
        self.no_of_tyres : int = no_of_tyres

    def start(self):
        print ( f"the engine of {self.name} is starting ......")
    
    def stop(self):
        print (f"turned off the {self.name} engine")
    
    def info(self):
        if self.no_of_tyres==1:
            print( " no such vechicle exists ")
        elif self.no_of_tyres==2:
            print (" the vechicle is a : BIKE 🏍")
        elif self.no_of_tyres==3:
            print (" the vechicle is a rickshaw 🛺")
        elif self.no_of_tyres==4:
            print ( " the vechicle is a car 🚗")
        else:
            print (" it's a big vechicle :  less info")
        
        def __add__(self,other):
            return f"{self.name} + {other.name}"


""" bike : vechicle #it's a type hint      where it tells that the bike1 is the object """


car1=vechicle("honda",4)
unknown=vechicle("motorcycle",2)

car1.info()
unknown.info()

car1.start()
unknown.start()

car1.stop()
unknown.stop()










        
    




