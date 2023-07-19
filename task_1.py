users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            },
            {
                "title": "Python basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan",
        "modules": [
            {
                "title": "Computer basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Luke",
        "type": "Student",
        "password": "skywalker",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            }
        ]
    },
    {
        "name": "Lora",
        "type": "Student",
        "password": "flash",
        "modules": [
            {
                "title": None,
                "completed": False
            }
        ]
    },{
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]

def check_user(name, password):
    for user in users:
        if user["name"] == name and user["password"] == password:
            return user
        elif user["name"].startswith('Anony')  and user["password"] == password:
            return user
    print("User not found")
    return None


def module_check(user, module_name):
    if user["type"] == "Student" and user.get('modules'):
        for module in user["modules"]:
            if module["title"] == module_name:
                print(module)
                return True
    print(f"You did not register to the module: {module_name}")
    return False


def show_registration():
    print("Welcome to the registration system")
    print("Please enter your name:")
    name = input()
    
    print(f"Please enter your password for {name}:")
    password = input()

    print(f"{name}, what module do you want to check")
    module_name = input()

    user=check_user(name, password)
    
    
    if user is not None and user["type"] == "Student" and user.get('modules') and module_check(user, module_name) == True:
        print("You are a student") 
        print(f"You are registered to the modules: {module_name}")
    
    elif user is not None and user["type"] != "Student":
        print("You are a teacher")

show_registration()


    # elif user[module_name] != users['modules']['"Computer basics"'] or user[module_name] != users['modules']['"Python basics"']:
    #     print("You are not registered to this module")
    # print(f"{name}, your registration status is {user['modules']['completed']}")


# my_items=[{'name': 'Bob', 'age': 25},{'name': 'Alice', 'age': 21},{'name': 'John', 'age': 20}]
# my_items.sort(key=lambda x: x['age'])
# print(my_items)

# my_list=['Mondays', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# my_list.sort(key=lambda x: x[0])
# print(my_list)


