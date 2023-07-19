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
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]

def check_user(name, password):
    '''Check if user exists'''
    for user in users:
        if user["name"] == name and user["password"] == password:
            return user

    if name.startswith("Anony"):
        return {
            "name": name,
            "type": "Student",
            "password": password,
            "modules": []
        }

    return None

def show_registration():
    '''Start of the registration'''
    print("Welcome to the registration:")

    print("What is your username?")
    name = input()
    
    print(f"Type the password for username {name}:")
    password = input()
    
    print(f"What module do you want to check, {name}?")
    module_name = input()

    user = check_user(name, password)
    if user is None:
        print("User not found")
    else:
        if user["type"] == "Student":
            module_found = False####
            for module in user.get("modules", []):
                if module["title"] == module_name:
                    module_found = True
                    if module.get("completed", False):
                        print(f"You have completed the module {module_name}.")
                    else:
                        print(f"You are registered to the module {module_name}.")
                        print(f"You did not complete the module {module_name}.")
                    break
            
            if not module_found:
                print(f"You did not register to the module {module_name}.")
        else:
            print(f"You are a {user['type']}.")

show_registration()
