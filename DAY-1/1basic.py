#python DATA TYPES
#primitive/basic      1)int 2)float  3)bool 4)Str 5)complex number a+bj
""" 
#collection data types   
ORDERED
list (odered : follow some specific sequences ) 
tuple ( ordered but immutable[meaning they can be modified once created])

UNORDERED
set ( they don't follow any specific sequences likes list :INDEX )   NO DUPLICATE ❌
frozenset ( IMMUTABLE )

KEY-VALUE PAIR 
DICT ( Dictonary )  ORDERED , MUTABLE , 

"""


mylist=[1,2,"hello",3.14,True,"Good"]
# mylist.append[2]
for i in range(len(mylist)):
    print(type(mylist[i]))
    if(mylist[i]=="Good"):
        
        print("yes we are Good")


my_tuple=(1,2,3,"GOOD", "BOYD",True)

my_set={1,2,3,3,4,4,3,43,43,4,343,343, "hello "}
print( my_set)
fz_set=frozenset([1,2,3,4,5,3,34,3,43,3,3,43,43,43,434343.3,7773737373])


print(fz_set)


student={
    "Name":"benny",
     "age": 25,
     "weight":42
}

print(student)



