class parent:
    def __init__(self,fname,age) -> None:
        self.fname=fname 
        self.age=age
    def info(self):
        print( f" Myself {self.fname} and my age is {self.age}")

class child(parent):
    def __init__(self, fname, age,cname) -> None:
        super().__init__(fname, age)
        self.cname=cname
    
    def info2(self):
        print(f"my father name is {self.fname}, and {self.cname} is my name, ")

class grandchild(child):
    def __init__(self, fname, age, cname,name) -> None:
        super().__init__(fname, age, cname)
        self.name=name
    def info3(self):
        print(f"my grandfather is {self.fname} \n my father name is {self.cname} \n and my name is {self.name}")

    

grandchild1=grandchild("dhramveer",72,"sunny deol","ronak")
grandchild2=grandchild("dhramveer",72,"sunny deol","priya")

print( grandchild2.name )