
class Account:
    '''
    This is the main class for the users accounts
    '''
    accounts_list = []
    def __init__(self,first_name,last_name,email,password,c_password):
        '''
        This function is the blue print of users accounts
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.c_password = c_password

    def save_account(self):
        '''
        This function allows users accounts to be saved
        '''
        Account.accounts_list.append(self)
