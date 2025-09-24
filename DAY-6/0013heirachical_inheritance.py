class animal:
    def __init__(self,name) -> None:
        self.name=name
        print(f"I'm a {self.name} and I'm a Animal ")

    def eating(self):
        # 1. Check if the current object has a 'cat_name' attribute
        if hasattr(self, 'cat_name'):
            actual_name = self.cat_name
        # 2. If not, check if it has a 'dog_name' attribute
        elif hasattr(self, 'dog_name'):
            actual_name = self.dog_name
        # 3. If neither exists, use the default 'name' from the parent
        else:
            actual_name = self.name
        
        print(f"{actual_name} is eating...")

class dog(animal):
    def __init__(self, name,dog_name) -> None:
        super().__init__(name)
        self.dog_name=dog_name
        print(f"I'm a DOG and my name is {self.dog_name}")

class cat(animal):
    def __init__(self, name,cat_name) -> None:
        super().__init__(name)
        self.cat_name=cat_name
        print(f"I'm a CAT and my name is {self.cat_name}")

cat_1=cat("cat","syrine")
dog_1=dog("dog","brono")
dog_2=dog("dog","shera")

cat_1.eating()
dog_1.eating()
dog_2.eating()

    

        