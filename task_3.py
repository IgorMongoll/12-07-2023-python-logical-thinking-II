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

modules = [
    {
        "name": "Computer basics"
    },
    {
        "name": "Python basics",
        "requirement": "Computer basics"
    },
    {
        "name": "Django",
        "requirement": "Python basics"
    }
]

def check_user(name, password):
    for user in users:
        if user["name"] == name and user["password"] == password:
            return user
    print("User not found")
    return None

def is_student(username):
    for user in users:
        if user["name"] == username and user["type"] == "Student":
            return True
    return False

def is_anonymous(username):
    return username.lower() == "anonymous"

def has_requirement(modulename):
    for module in modules:
        if module["name"] == modulename and "requirement" in module:
            return module["requirement"]
    return None

def is_registered(username, modulename):
    for user in users:
        if user["name"] == username and user["type"] == "Student":
            for module in user.get("modules", []):
                if module["title"] == modulename:
                    return True
    return False

def has_completed_requirement(username, modulename):
    requirement = has_requirement(modulename)
    if requirement:
        return is_registered(username, requirement) and is_completed(username, requirement)
    return False

def is_completed(username, modulename):
    for user in users:
        if user["name"] == username and user["type"] == "Student":
            for module in user.get("modules", []):
                if module["title"] == modulename:
                    return module["completed"]
    return False

def may_enroll(username, modulename):
    if is_anonymous(username) and not has_requirement(modulename):
        return True
    if is_student(username):
        if not is_registered(username, modulename):
            return has_completed_requirement(username, modulename)
    return False


def show_registration(username, password, modulename):
    user = check_user(username, password)
    if user is not None and user["type"] == "Student":
        if is_registered(username, modulename):
            print(f"You are registered to the module {modulename}.")
            if not is_completed(username, modulename):
                print(f"You did not complete the module {modulename}.")
            print(f"You may {'register to' if may_enroll(username, modulename) else 'not register to'} the module {modulename}.")
        else:
            print(f"You did not register to the module {modulename}.")
            print(f"You may {'register to' if may_enroll(username, modulename) else 'not register to'} the module {modulename}.")
    elif user is not None and user["type"] == "Teacher":
        print("You are a teacher.")
        print(f"You may not register to the module {modulename}.")
    else:
        print("User not found.")
        print(f"You may {'register to' if may_enroll(username, modulename) else 'not register to'} the module {modulename}.")

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")

show_registration(username, password, modulename)


username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")

show_registration(username, password, modulename)
