from cridentials import cridentials as cri
from user import Account as acc

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
            password = input("... Password ...\n")
            c_password = input("... Confirm Password ...\n")
            while password != c_password:
                print("Passwords don't match. \n Please confirm password")
                c_password = input("... Confirm Password ...\n")
            else:
                save_account(create_account(fname,lname,email,password,c_password))
                print("Hey "+acc.accounts_list[0].first_name + " your account was created")

        else:
            print("________________________________invalid responce________________________________")
if __name__ == "__main__":
    main()
