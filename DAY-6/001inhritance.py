#single inheritance 

class animal:
    def __init__(self,name,age) -> None:
        self.name=name 
        self.age=age
    
    def sound(self):
        print( f"the {self.name} says wooh wooh ")


class dog(animal):
   
    def __init__(self, name,breed,age,weight) -> None:
       super().__init__(name,age=age)
       self.breed=breed
       self.age=age
       self.weight=weight
    
    def information(self):
       print(f"the {self.name} is a Dog \n it's age is {self.age}. \n it's breed is {self.breed} \n it's weight is {self.weight}")


dog=dog("puffy","german shepeard",10,40) 
dog.information()
dog.sound()    

