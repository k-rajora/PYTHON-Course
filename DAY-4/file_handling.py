import os,glob
with open("newfile.txt","a+") as f:
    print( f.tell())
    
# os.remove("newfile.txt")
print (os.listdir("."))   


#glob module is used for using [* this wildcard ]
for file in glob.glob("*.txt"):
   os.remove(file)


