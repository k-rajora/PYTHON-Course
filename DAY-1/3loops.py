my_list=[1,2,"let's go"]

#for accessing both index and the item we use the enumerate(iterable, start) or (item, index )
#   index  item      iterable{list}  starting point if not defined [0]    check at C:\Users\BENNY RHODE\Desktop\DEVOPS\Python\DAY-1\30loops.txt
for i,k in enumerate(my_list):
    # print (len(my_list))
    print (type(my_list))
    print(i,k)

my_tuple=(1,2,3,4,5,6)
for i,k in enumerate(my_tuple):
    print(type(my_tuple))
    print(i,k)


my_set={1,2,3,4,5,6,"hello body me "}

for i,k in enumerate(my_set):
    print(type(my_set))
    print("here is my index of undorder :", i,k)


Organisation={
    "buildingA":{
        "sectionA":{
            "TECH":{
                101:{
                    "name":"kartik",
                    "age":23,
                    "address":"bihar"

                },
                102:{},
                103:{},
            },
            "NonTech":{}
        },
        "sectionB":{
            "TECH":{},
            "NonTech":{}
        },
        "sectionC":{
            "TECH":{},
            "NonTech":{}
        }
    },
    "buildingB":{
        "sectionA":{
            "TECH":{},
            "NonTech":{}
        },
        "sectionB":{
            "TECH":{},
            "NonTech":{}
        },
        
        "sectionC":{
            "TECH":{},
            "NonTech":{}
        }
    },
    "buildingC":{
        "sectionA":{
            "TECH":{},
            "NonTech":{}
        },
        "sectionB":{
            "TECH":{},
            "NonTech":{}
        },
        "sectionC":{
            "TECH":{},
            "NonTech":{}
        }
    }
}
employee = Organisation.get("buildingA", {}) \
                       .get("sectionA", {}) \
                       .get("TECH", {}) \
                       .get(101, {})





for key, value in enumerate(Organisation):
    print(key ,value)
    continue
    print(Organisation["buildingA"]["sectionA"]["TECH"][101])
   

# Function to search for an employee by ID
def find_employee(org, emp_id):
    for building, sections in org.items():
        for section, departments in sections.items():
            for dept, employees in departments.items():
                if emp_id in employees:
                    return {
                        "building": building,
                        "section": section,
                        "department": dept,
                        "details": employees[emp_id]
                    }
    return None  # if not found

# Example usage
result = find_employee(Organisation, 1088)
if result:
    print("Employee found!")
    print("Building:", result["building"])
    print("Section:", result["section"])
    print("Department:", result["department"])
    print("Details:", result["details"])
else:
    print("Employee not found.")


# for key, value in Organisation.items:
#     print(key, value)