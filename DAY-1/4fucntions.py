def greet(greet):
   print (f"hello {greet} nice to meet you !! 😀😀")

greet("lailaa")

#Recursion
def factorial(num):
   if num==0:
      return 1
   else:
      return num*factorial(num-1)


print(factorial(5))


#postional arguements
def add(a,b):
   return a+b

add(1,2)

#keyword arugments    
def calling(signal):
   print (signal)

calling(signal="hello baby")


#*args when you don't know the number of arguments  , it stores all these arguemnts in the """ TUPLE """ immutable
def adding(*args):
   return sum(args)

print (adding(1,2,3,4,5,6,7,8,9,10))


#**kwargs variable length keyword arguments, key value pair
def show_student_infor(**kwargs):
   for key,value in kwargs.items():
      print ( f" {key} : {value}")

show_student_infor(name="kartik",age=25,born="25/12/2000")





#lamda functions

square= lambda x:x**2
print(square(5))