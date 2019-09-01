from cridentials import cridentials as cri
from user import Account as acc
import getpass
def create_account(fname,lname,email,password,c_password):
    '''
    This function allows creation of an account
    '''
    new_account= acc(fname,lname,email,password,c_password)
    return new_account

def save_account(account):
    '''
    This function allows users accounts to be saved
    '''
    account.save_account()

def create_cridentials(username,email,password):
    '''
    This function allows users to save a new cridentials
    '''
    new_cridentials = cri(username,email,password)
    return new_cridentials

def save_cridentials(cridential,app):
    '''
    This function allows users to save their cridentials
    '''
    cridential.save_cridentials(app)

def generate_password(name,length):
    '''
    This function allows auto generation of password
    '''
    pwd = cri.generate_password(name,length)
    return pwd[0:length]

def display_cridentials(app,lenght):
    '''
    This function displays cridentials
    '''
    res=cri.show_cridentials(app,len)
    return res

def main():
    '''
    This is the body of the function
    '''
    while True:
        print("\t\t\t!!Hey There!!\n Welcome to password locker. Briefly we allow you to create an account and save all your passwords here\n");
        responce=input("To get started type cc to create an account\n")

        if responce.lower() == "cc":
            fname = input("... First Name ...\n")
            lname = input("... Last Name ...\n")
            email = input("... Email ...\n")
            password = getpass.getpass("... Password ...\n")
            c_password = getpass.getpass("... Confirm Password ...\n")
            while password != c_password:
                print("Passwords don't match. \n Please confirm password")
                c_password = input("... Confirm Password ...\n")
            else:
                save_account(create_account(fname,lname,email,password,c_password))
                print("Hey "+acc.accounts_list[0].first_name + " your account was created")
                while True :
                    print(f"""Welcome {acc.accounts_list[0].first_name} please select the account cridentials that you want to fill by using the following keys
                ig - Instagram          twi - Twitter          fb - Facebook
                li - Linked In          snap - SnapChat        git - github
                            gm - Gmail                 yh - Yahoo
                    !!To show cridentials add 's' at the end of each initials!!
                            Example for Twiter type 'twits'
                    """)
                    res = input()

                    if res == 'ig':
                        app="instagram"
                        username = input(" ... Username ... \n")
                        email = input(" ... Email ...\n")
                        pwd = input("Do you want a generated password or not\n (y/n)")
                        if pwd.lower() == "y":
                            length = int(input("specify length\n"))
                            print(f"Your Password is {generate_password(username,length)}")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                        else :
                            password =getpass.getpass(" ...Enter a Password ...\n")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                    if res == 'twi':
                        app="twitter"
                        username = input(" ... Username ... \n")
                        email = input(" ... Email ...\n")
                        pwd = input("Do you want a generated password or not\n (y/n)")
                        if pwd.lower() == "y":
                            length = int(input("specify length\n"))
                            print(f"Your Password is {generate_password(username,length)}")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                        else :
                            password =getpass.getpass(" ...Enter a Password ...\n")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                    if res == 'fb':
                        app="facebook"
                        username = input(" ... Username ... \n")
                        email = input(" ... Email ...\n")
                        pwd = input("Do you want a generated password or not\n (y/n)")
                        if pwd.lower() == "y":
                            length = int(input("specify length\n"))
                            print(f"Your Password is {generate_password(username,length)}")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                        else :
                            password =getpass.getpass(" ...Enter a Password ...\n")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                    if res == 'li':
                        app="linkedin"
                        username = input(" ... Username ... \n")
                        email = input(" ... Email ...\n")
                        pwd = input("Do you want a generated password or not\n (y/n)")
                        if pwd.lower() == "y":
                            length = int(input("specify length\n"))
                            print(f"Your Password is {generate_password(username,length)}")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                        else :
                            password =getpass.getpass(" ...Enter a Password ...\n")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                    if res == 'snap':
                        app="snapchat"
                        username = input(" ... Username ... \n")
                        email = input(" ... Email ...\n")
                        pwd = input("Do you want a generated password or not\n (y/n)")
                        if pwd.lower() == "y":
                            length = int(input("specify length\n"))
                            print(f"Your Password is {generate_password(username,length)}")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                        else :
                            password =getpass.getpass(" ...Enter a Password ...\n")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                    if res == 'git':
                        app="github"
                        username = input(" ... Username ... \n")
                        email = input(" ... Email ...\n")
                        pwd = input("Do you want a generated password or not\n (y/n)")
                        if pwd.lower() == "y":
                            length = int(input("specify length\n"))
                            print(f"Your Password is {generate_password(username,length)}")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                        else :
                            password =getpass.getpass(" ...Enter a Password ...\n")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                    if res == 'gm':
                        app="gmail"
                        username = input(" ... Username ... \n")
                        email = input(" ... Email ...\n")
                        pwd = input("Do you want a generated password or not\n (y/n)")
                        if pwd.lower() == "y":
                            length = int(input("specify length\n"))
                            print(f"Your Password is {generate_password(username,length)}")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                        else :
                            password =getpass.getpass(" ...Enter a Password ...\n")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                    if res == 'yh':
                        app="yahoo"
                        username = input(" ... Username ... \n")
                        email = input(" ... Email ...\n")
                        pwd = input("Do you want a generated password or not\n (y/n)")
                        if pwd.lower() == "y":
                            length = int(input("specify length\n"))
                            print(f"Your Password is {generate_password(username,length)}")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                        else :
                            password =getpass.getpass(" ...Enter a Password ...\n")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                    if res == 'igs':
                        password = getpass.getpass("Please Enter your password to see cridentials\n")
                        if password != acc.accounts_list[0].password:
                            print("\n\n\t\t\tIncorrect Password Please try again\n\n")

                        else:
                            app = "instagram"
                            length = len(cri.social_accounts[app])
                            if length == 0:
                                print(f"\t\tYou have no {app.capitalize()} cridentials\n\n")
                            else :
                                print(f"\n\t\t {app.upper()} CRIDENTIALS\n")
                                for i in range(length):
                                    print(f"\t\tUsername ...{cri.social_accounts[app][int(i)-1].username}")
                                    print(f"\t\tEmail    ...{cri.social_accounts[app][int(i)-1].email}")
                                    print(f"\t\tPassword ...{cri.social_accounts[app][int(i)-1].password}\n")

                    if res == 'twis':
                        password = getpass.getpass("Please Enter your password to see cridentials\n")
                        if password != acc.accounts_list[0].password:
                            print("\n\n\t\t\tIncorrect Password Please try again\n\n")

                        else:
                            app = "twitter"
                            length = len(cri.social_accounts[app])
                            if length == 0:
                                print(f"\t\tYou have no {app.capitalize()} cridentials\n\n")
                            else :
                                print(f"\n\t\t {app.upper()} CRIDENTIALS\n")
                                for i in range(length):
                                    print(f"\t\tUsername ...{cri.social_accounts[app][int(i)-1].username}")
                                    print(f"\t\tEmail    ...{cri.social_accounts[app][int(i)-1].email}")
                                    print(f"\t\tPassword ...{cri.social_accounts[app][int(i)-1].password}\n")

                    if res == 'fbs':
                        password = getpass.getpass("Please Enter your password to see cridentials\n")
                        if password != acc.accounts_list[0].password:
                            print("\n\n\t\t\tIncorrect Password Please try again\n\n")

                        else:
                            app = "facebook"
                            length = len(cri.social_accounts[app])
                            if length == 0:
                                print(f"\t\tYou have no {app.capitalize()} cridentials\n\n")
                            else :
                                print(f"\n\t\t {app.upper()} CRIDENTIALS\n")
                                for i in range(length):
                                    print(f"\t\tUsername ...{cri.social_accounts[app][int(i)-1].username}")
                                    print(f"\t\tEmail    ...{cri.social_accounts[app][int(i)-1].email}")
                                    print(f"\t\tPassword ...{cri.social_accounts[app][int(i)-1].password}\n")

                    if res == 'lis':
                        password = getpass.getpass("Please Enter your password to see cridentials\n")
                        if password != acc.accounts_list[0].password:
                            print("\n\n\t\t\tIncorrect Password Please try again\n\n")

                        else:
                            app = "linkedin"
                            length = len(cri.social_accounts[app])
                            if length == 0:
                                print(f"\t\tYou have no {app.capitalize()} cridentials\n\n")
                            else :
                                print(f"\n\t\t {app.upper()} CRIDENTIALS\n")
                                for i in range(length):
                                    print(f"\t\tUsername ...{cri.social_accounts[app][int(i)-1].username}")
                                    print(f"\t\tEmail    ...{cri.social_accounts[app][int(i)-1].email}")
                                    print(f"\t\tPassword ...{cri.social_accounts[app][int(i)-1].password}\n")

                    if res == 'snaps':
                        password = getpass.getpass("Please Enter your password to see cridentials\n")
                        if password != acc.accounts_list[0].password:
                            print("\n\n\t\t\tIncorrect Password Please try again\n\n")

                        else:
                            app = "snapchat"
                            length = len(cri.social_accounts[app])
                            if length == 0:
                                print(f"\t\tYou have no {app.capitalize()} cridentials\n\n")
                            else :
                                print(f"\n\t\t {app.upper()} CRIDENTIALS\n")
                                for i in range(length):
                                    print(f"\t\tUsername ...{cri.social_accounts[app][int(i)-1].username}")
                                    print(f"\t\tEmail    ...{cri.social_accounts[app][int(i)-1].email}")
                                    print(f"\t\tPassword ...{cri.social_accounts[app][int(i)-1].password}\n")

                    if res == 'gits':
                        password = getpass.getpass("Please Enter your password to see cridentials\n")
                        if password != acc.accounts_list[0].password:
                            print("\n\n\t\t\tIncorrect Password Please try again\n\n")

                        else:
                            app = "github"
                            length = len(cri.social_accounts[app])
                            if length == 0:
                                print(f"\t\tYou have no {app.capitalize()} cridentials\n\n")
                            else :
                                print(f"\n\t\t {app.upper()} CRIDENTIALS\n")
                                for i in range(length):
                                    print(f"\t\tUsername ...{cri.social_accounts[app][int(i)-1].username}")
                                    print(f"\t\tEmail    ...{cri.social_accounts[app][int(i)-1].email}")
                                    print(f"\t\tPassword ...{cri.social_accounts[app][int(i)-1].password}\n")

                    if res == 'gms':
                        password = getpass.getpass("Please Enter your password to see cridentials\n")
                        if password != acc.accounts_list[0].password:
                            print("\n\n\t\t\tIncorrect Password Please try again\n\n")

                        else:
                            app = "gmail"
                            length = len(cri.social_accounts[app])
                            if length == 0:
                                print(f"\t\tYou have no {app.capitalize()} cridentials\n\n")
                            else :
                                print(f"\n\t\t {app.upper()} CRIDENTIALS\n")
                                for i in range(length):
                                    print(f"\t\tUsername ...{cri.social_accounts[app][int(i)-1].username}")
                                    print(f"\t\tEmail    ...{cri.social_accounts[app][int(i)-1].email}")
                                    print(f"\t\tPassword ...{cri.social_accounts[app][int(i)-1].password}\n")

                    if res == 'yhs':
                        password = getpass.getpass("Please Enter your password to see cridentials\n")
                        if password != acc.accounts_list[0].password:
                            print("\n\n\t\t\tIncorrect Password Please try again\n\n")

                        else:
                            app = "yahoo"
                            length = len(cri.social_accounts[app])
                            if length == 0:
                                print(f"\t\tYou have no {app.capitalize()} cridentials\n\n")
                            else :
                                print(f"\n\t\t {app.upper()} CRIDENTIALS\n")
                                for i in range(length):
                                    print(f"\t\tUsername ...{cri.social_accounts[app][int(i)-1].username}")
                                    print(f"\t\tEmail    ...{cri.social_accounts[app][int(i)-1].email}")
                                    print(f"\t\tPassword ...{cri.social_accounts[app][int(i)-1].password}\n")
            print("________________________________invalid responce________________________________")
if __name__ == "__main__":
    main()
