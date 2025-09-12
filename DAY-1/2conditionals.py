#if statment 

while True:
    print("hey user enter your name : ")
    name=input()
    if name =="kartik":
        print("success ✅")
        break
    elif name=="women":
        print("Caution ⚠")
    else:
        print("denied ❌")

age=int(input("enter your age : "))

match age:
    case 10:
        print("you can't vote ❌")
    case 15:
        print( "wait for 2 yrs ⭕")
    case 18:
        print( "VOTE ✅")
    case _:  #this is the deafault case
        print( " We need to check ❓")

    

    
       
