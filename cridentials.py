import pyperclip

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
        
