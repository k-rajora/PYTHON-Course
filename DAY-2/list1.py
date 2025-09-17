mylist=["study","play","sleep","exercise","eating","sleepin"]
# print (mylist)

def task_add(task):
   mylist.append(task)


def task_remove(index):
    mylist.remove(index)


def task_list():
    print("__________________________________________")
    print (mylist)
    print("__________________________________________")



while True:
    print ("=========================================================")
    print("welcom to the todo : add ; remove ; list , quit")
    option=input("choose you desired option :  ")
    if ( option=="add"):
        todo=input("enter your todo that you want add: ")
        task_add(todo)
    elif ( option=="remove"):
         task_list
         remov_task=input("enter the task to be removed : ")
         task_remove(remov_task)
    elif ( option=="list" ):
          task_list()
    else :
       break



    
