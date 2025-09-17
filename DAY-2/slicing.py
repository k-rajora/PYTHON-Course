my_list=list(["hellow","my","name","is","kartik","thankyou"])

#i wnat my name is kartik
for index,item in enumerate(my_list):
    if ( item =="my" ):
        flag1=index
    elif ( item == "kartik"):
        flag2=index


sub_list=my_list[flag1:flag2+1:]



print (sub_list)


my_tuple=tuple(("my",1,2,3,4,5,6,"end"))
# sub_tuple=my_tuple(1:2:)