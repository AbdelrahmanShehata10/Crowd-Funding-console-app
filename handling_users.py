import re
import json
login_status=False
def register_user(first_name,last_name,email,password,confirm_password,mobilephone):
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        print("This Email Is Not Valid")
        return False
    if password !=confirm_password:
        print("passwords doesn't match")
        return False
    if not re.match(r'^01[0-2]{1}[0-9]{8}$', mobilephone):
        print("Error: Invalid mobile number")
        return False

    users=[]
    user={
        'first_name':first_name,
        'last_name' :last_name,
        'email':email,
        'password':password,
        'confirm_password':confirm_password,
        'mobilephone':mobilephone

    }
    try:
        with open('users.json','r') as file:
            users=json.load(file)
            users.append(user)
            for user in users:
                if user['email'] == email:
                    print("this email already exists ----> But Continue ")


    except Exception as e:
        print(e)
    with open('users.json','w') as file:
            json.dump(users,file,indent=4)
            print("Registration done")
def login_user(email,password):
    global login_status
    users=[]
    try:
        with open('users.json','r') as file:
            users=json.load(file)
    except Exception as e:
        print(e)

    for user in users:
        if user['email'] ==email and user['password']==password :
            login_status=True
            print("Login successful")

        else:
            print("Login failed")
            login_status=False
def create_project(email,Title,Details, Total_target,starttime,endtime):
    global login_status
    users = []
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except Exception as e:
        print(e)
    project = {

        'title': Title,
        'details': Details,
        'total_target': Total_target,
        'start_time': starttime,
        'end_time': endtime
    }
    for user in users:
        if user['email'] ==email and login_status:
            if 'projects' not in user:
                user['projects']=[]
                print("Congratulatuins this is your first one")
            user['projects'].append(project)
        else:
            print("email Not Found or  login not happend")
            break

        try:
            with open("users.json","w") as file:
                json.dump(users,file,indent=4)
                print("projects added Successfully")
        except Exception as e:
            print(e)

def handling_projects(email,option):

    users = []
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except Exception as e:
        print(e)

    for user in users:
        global login_status
        if option==1 and user['email']==email and login_status:
            print(user['projects'])
        elif option==2 and user['email']==email and login_status:
            project=user['projects']
            what_to_edit=input("what do you want to edit --> choose one \n title details total_target")
            the_edition=input("edition: ")
            title_of_changed_book=input("title_of_changed_book")
            for p in project:
                if p['title']==title_of_changed_book:
                    p[what_to_edit]=the_edition
                else:
                    print("there is no book with this title")
                    break
            try:
                with open("users.json", "w") as file:
                    json.dump(users, file, indent=4)
                    print("projects updated Successfully")
            except Exception as e:
                print(e)
        elif   option==3 and user['email']==email and login_status:
            project = user['projects']
            title_of_deleted_book=input("title_of_deleted_book")
            for p in project:
                if p['title'] == title_of_deleted_book:
                    project.remove(p)
                    try:
                        with open("users.json", "w") as file:
                            json.dump(users, file, indent=4)
                            print("projects deleted Successfully")
                    except Exception as e:
                        print(e)
                else:
                    print("there is no book with this title")
                    break
        elif option==4 and user['email']==email and login_status :
            login_status=False
            print("You logged out successfully")
        else:
            print("loggin out not happend")











