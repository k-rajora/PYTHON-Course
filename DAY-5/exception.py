#syntax
try:      #this block handles the error
  ...
except Exception as e:   #this catches it and performs some fucntion , we can have multiple except for different types of error
  ...
except ValueError:
  ...
except TypeError:
  ...
except ValueError:
  ...
else:   #this blocks runs only whne the try block succesfully runs
  ...
finally:   #this block always runs
  ...

num=input("enter you number")

try:
    for i in range(1,11):
     print(f" {int(num)} X {i} = {int(num)*i}")
except Exception as e:
 print(e)
else :
  print("Everything run okk!! ")
finally :
  print("this blocks always runs !!")