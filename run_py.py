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
                li - Linked In          snap - SnapChat        gm - Gmail
                                        yh - Yahoo
                    """)
                    res = input()

                    if res == 'ig':
                        app="instagram"
                        username = input(" ... Username ... \n")
                        email = input(" ... Email ...\n")
                        pwd = input("Do you want a generated password or not\n (y/n)")
                        if pwd.lower() == "y":
                            length = int(input("specify lenght\n"))
                            print(f"Your Password is {generate_password(username,length)}")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")

                        else :
                            password =getpass.getpass(" ...Enter a Password ...\n")
                            save_cridentials(create_cridentials(username,email,password),app)
                            print(f"__________{app.capitalize()} cridentials added__________")
        else:
            print("________________________________invalid responce________________________________")
if __name__ == "__main__":
    main()
