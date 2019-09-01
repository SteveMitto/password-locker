import pyperclip
import random
from user import Account as acc
class cridentials:
    '''
    This class
    '''
    social_accounts={'instagram':[],'twitter':[],'facebook':[],'linkedin':[],'snapchat':[]}

    def __init__(self,username,email,password):
        '''
        This function creates the initialization
        '''
        self.username = username
        self.email = email
        self.password = password

    def save_cridentials(self,app):
        '''
        This function allows saving of cridentials
        '''
        cridentials.social_accounts[app].append(self)

    def delete_cridentials(self,app):
        '''
        This function allows deletion of cridentials
        '''
        cridentials.social_accounts[app].remove(self)

    def generate_password(names,length):
        '''
        This function generates a password
        '''
        target =list(names)
        random.shuffle(target)
        number=random.randint(0,length+1)
        num=str(number)
        final = num.join(target)
        while len(final) < length :
            number=random.randint(0,length+1)
            num=str(number)
            final = num.join(target)
        else:
            return final
