import pyperclip
import random
from user import Account as acc
class cridentials:
    '''
    This class
    '''
    social_accounts={'instagram':[],'twitter':[],'facebook':[],'linkedin':[],'snapchat':[],'gmail':[],'github':[],'yahoo':[]}

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
        number=random.randint(0,length)
        num=str(number)
        final = num.join(target)
        return final
    @classmethod
    def show_cridentials(cls,app,len):
        '''
        This function gets cridentials
        '''
        return cls.social_accounts[app][len].username
