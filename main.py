import handling_users
from  handling_users import register_user
from  handling_users import login_user
from  handling_users import create_project
from  handling_users import handling_projects
choice=input("register or login")
if choice=="register":

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    mobilephone = input("Enter your mobile phone number: ")
    register_user(first_name, last_name, email, password, confirm_password, mobilephone)


    register_user(first_name, last_name, email, password, confirm_password, mobilephone)

else:
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    login_user(email,password)
    choice2=input("Create Project or handling already projects")
    if choice2== "Create Project":
        title = input("Enter the project title: ")
        details = input("Enter project details: ")
        total_target = input("Enter total target amount: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        create_project(email, title, details, total_target, start_date, end_date)
    else:
        print("1. View all projects")
        print("2. Edit project")
        print("3. Delete project")
        print("4. Logout")
        option=(int)(input("enter the option"))
        handling_projects(email,option)