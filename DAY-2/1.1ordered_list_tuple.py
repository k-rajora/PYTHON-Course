#number list

number_list=[-1,1,2,3,4,5]

for index, item in enumerate(number_list):
    print ( f" the number at  [{index}] : {item} ")

number_list[0]=23
number_list.append(42)
number_list.insert(0,200)
number_list.remove(4)
print (min(number_list))
number_list.sort()
print(number_list)


#EASy lvl 
#1)
natural_number=[]

for item in range(1,11):
    natural_number=natural_number+[item]

print ( natural_number )

"""
natural_numbers=list(range(1,11))
print(natural_numbers)
"""
#2) easy lvl
"""print (natural_number[0],natural_number[len(natural_number)-1])"""
print (natural_number[0],natural_number[-1])               #python allows negative indexing  


# 3) easy lvl  print the list in the reverse order using slicing {what is slicing ? carving out certain portion of the list }
               # starting index: ending index: steps
print (natural_number[len(natural_number): 2:-2])


# INTERMEDIATE list 

for item in natural_number:
    if item%2==0:
        print(item)

nums=[1,20,2,3,3,4,5,6]
count=0
for index, item in enumerate(nums):
    if item==3 :
        count+=1
        print (f" the {count} : at index [{index}]")
    
print (sorted(nums))

""" 
Feature	            list.sort()	                           sorted(iterable)
Type	       1)  Method of the list class	              1) Built-in function
Object	       1)  Only works on lists	                  2) Works on any iterable
Behavior	   3)  Modifies the original list in-place	  3) Returns a new sorted list
Return Value   4)  None	                                  4)  The new sorted list
Memory	       5)  More memory efficient for              5)  Requires more memory to create and store the new list
                 large lists as it doesn't create a copy	
"""
# numgs=[1,20,2,3,3,4,5,6]
# print ( numgs.sort(reverse=True)
#Merging two lists 
list1=[1,2,3] 
list2=[4,5,6]
# list1.extend(list2) 
list2.extend(list1)
#pointer approach






# createing a sublist form a given list
list_BIG=[1,2,3,4,5,6,7,8,9]
list_small=list_BIG[2:7]      #slicing 
# for index,item in enumerate(list_BIG):
#     if ( 1< index<8 ):
#         list_small+=[item]

print (list_small)

