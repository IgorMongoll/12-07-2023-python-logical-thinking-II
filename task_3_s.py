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

def check_User_exist(username, password,modulename):
    ''' if user in DB returne User
       check for occurence and compaire with [list of dictinaries] '''
    for user in users:
        if username == user['name'] and password == user['password']:
            return user
    if username.startswith('Anonym'):
        is_Anonymus(modulename)
        return False
    else: 
        print("User not found in functon check_User_exist")# debag exta output
        #return False
    return False

def find_user_by_name(name):
    '''find user by name'''
    for user in users:
        if user['name'] == name:
            return user

def find_module_by_name(modulename):
    '''find module by name'''
    for module in modules:
        if module['name'] == modulename:
            return module

def is_student(user):
    if user["type"] == "Student":
        return True
    return False



def is_ModuleComplieted(user, modulename):
    '''check if module is complieted'''
    for module in user['modules']:
        if modulename == module['title'] and module['completed'] == True:
                #print('This modlue is complieted',module['completed'])
                return True

def get_user_type_Teacher(user):
    '''get user type'''
    return user['type'] == 'Teacher'



def check_a_Module(modulename, modules):
    ''' module to check in modulename if it is in the list of modules'''
    if modulename in modules:
        # print('What module do you want to check')
        return True

def is_Anonymus(modulename):
    '''This function is to check module only for Anonymous'''
    module = find_module_by_name(modulename)
    if modulename == 'Computer basics': #if input Cpmputer basics
         print(f'You did not register to the module {modulename}')
         print(f'You did not complete the module {modulename}')
         print(f'You may register to the module {modulename}')
         return None
    elif  module:
        print(f'You did not register to the module {modulename}')
        print(f'You did not complete the module {modulename}')
        print(f'You may not register to the module {modulename}')
        return None
    print(f'There is not such module {modulename}')
    print('But in accordence to task output it has to be written\nnot complete and may not register')
    return None

def is_registered(user,modulename):
    'if the user ist registered for module returne Truh'
    for module in user.get('modules',[]):
        if module ['title']==modulename:
            return True
    return False

def can_registered(user, modulename):
    '''Check if the student can register for the next module'''
    if find_module_by_name(modulename):
        # get list with compel modulen for student
        completed_modules = [module['title'] for module in user.get('modules', []) if module.get('completed', False)]

        # get list must module, depending from previous
        required_modules = [module['name'] for module in modules if 'requirement' in module]

        # 
        # ckeck if all module with previous completed 
       
        for required_module in required_modules:
            if required_module not in completed_modules:
                print(f"You did not complete the module {modulename}.")
                return False

        # if all previous/must module comlpeted, student may register
        print(f"You may register for the module {modulename}.")
        return True
    else:
        print("Module not found in functon can_registered")# debag exta output



def show_registration(user, modulename):
    #user = check_User_exist(username, password, modulename) # check user exist in DB
    if user:

        if get_user_type_Teacher(user):
            print(f'You are a Teacher')
            print(f'You may not register to the module {modulename}')
            return False

        if is_student(user):
            if is_registered(user, modulename):
                print(f'You are registered to the module {modulename}')
            else:
                print(f'You did not register to the module {modulename}')

            is_module_completed = is_ModuleComplieted(user, modulename)
            if is_module_completed:
                print(f'You completed the module {modulename}')
            # else:
            #     print(f'You did not complete the module {modulename}')

            elif not can_registered(user, modulename):
                #    print(f'You may register to the module {modulename}')
                # else:
                    print(f'You may not register to the module {modulename}')

   
def start():
    '''Takes inPut'''
    username = input("What is your username? ")
    password = input(f"Type the password for username {username}: ")
    modulename = input("What module do you want to check? ")
    # check user exist in DB
    user=check_User_exist(username, password, modulename)
    if user:
        
        show_registration(user, modulename)
    return False
 
start()
