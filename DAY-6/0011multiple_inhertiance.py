#multiple inheritance 

class animal:
    def __init__(self,name,age) -> None:
        self.name=name 
        self.age=age
    
    def sound(self):
        print( f"the {self.name} says wooh wooh ")


class dog:
   
    def __init__(self,breed,weight) -> None:
    #    super().__init__(name,age=age)
       self.breed=breed
    #    self.age=age
       self.weight=weight
    
    def information(self):
       print(f" it's breed is {self.breed} \n it's weight is {self.weight}")



class brono(animal,dog):
    def __init__(self, name, age,breed,weight) -> None:
        animal.__init__(self,name, age)  #explicit call
        dog.__init__(self,breed,weight)
    
    def speciality(self):
        print("brono is very shy !!!")


brono=brono("brono",10,"german",42)

brono.information()
brono.speciality()
brono.sound()





#multiple inheritacne using super()
class Animal:
    def __init__(self, name, age, **kwargs) -> None:
        super().__init__(**kwargs)   # Pass remaining args up the chain
        self.name = name
        self.age = age
    
    def sound(self):
        print(f"The {self.name} says wooh wooh")


class Dog:
    def __init__(self, breed, weight,height, **kwargs) -> None:
        super().__init__(**kwargs)   # Pass remaining args up the chain
        self.breed = breed
        self.weight = weight
        self.height=height
    
    def information(self):
        print(f"Its breed is {self.breed} \nIts weight is {self.weight}")


class Brono(Animal, Dog):
    def __init__(self, name, age, breed, weight) -> None:
        super().__init__(name=name, age=age, breed=breed, weight=weight)
    
    def speciality(self):
        print("Brono is very shy !!!")


# Create object
brono_obj = Brono("brono", 10, "german", 42)

brono_obj.sound()         # From Animal
brono_obj.information()   # From Dog
brono_obj.speciality()    # From Brono
