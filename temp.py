
name_list = [
    "Traci Peters","Tanya Padilla","Tabitha Reid","Tasha Todd","Tommie Hunter","Tyler Mitchell","Tommie Dixon","Toby Beck","ACracy Mendez"
]

def filter_first_names():
    letter = input("What letter does the first name begin with? ").upper()
    result = list(filter(lambda x: x.startswith(letter), name_list))
    if len(result) <= 0:
        print("\nNo first names were found starting with the letter " + letter )
    printArray(result)


def filter_last_names():
    letter = input("What letter does the last name begin with? ").upper()
    result = list(filter(lambda x: x.split(" ")[1].startswith(letter), name_list))
    if len(result) <= 0:
        print("\nNo last names were found starting with the letter " + letter)
    printArray(result)

def add_a_name():
    first_name = input("Enter new First name ")
    last_name = input("Enter new Last name ")
    name = " ".join([first_name, last_name])
    name = name.title()
    name_list.append(name)
    print(name + " has been added. ")


def delete_a_name():
    try:
        name = input("Enter the full name to delete ").title()
        name_list.remove(name)
        if name not in name_list:
            print(name + " has been removed. ")
    except:
        print("That name was not found.")
    

def printArray(arr):
    for value in arr:
        print(value)

menu = """ -----------------------------------------------
please select from the following options: \n
1. List all first names beginning with a chosen letter
2. List all last names beginning with a chosen letterfilter
3. Add a name
4. Delete a name
5. Exit \n
"""
choice2Function = {
    "1": filter_first_names,
    "2": filter_last_names,
    "3": add_a_name,
    "4": delete_a_name,
    "5": exit
}

while True:
    print(menu)
    choice = input("Option# : ")
    if choice in choice2Function:
        invocation = choice2Function[choice]()



