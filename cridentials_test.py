from cridentials import cridentials as cri
import unittest as unit
from user import Account as acc


class TestCridentials(unit.TestCase) :
    '''
    This class is used to test user cridentials
    '''
    def setUp(self):

        self.cridentials = cri("Steve Mitto","mitto@gmail.com","1234567")
        self.apps=['instagram','twitter','facebook','linkedin','snapchat','gmail','github','yahoo']
        self.new_account = acc("John","Doe","john@gmail.com","12johnDoes34","12johnDoes34")

    def test_init(self):
        '''
        This function tests for initialisation
        '''
        self.assertEqual(self.cridentials.username,"Steve Mitto")
        self.assertEqual(self.cridentials.email,"mitto@gmail.com")
        self.assertEqual(self.cridentials.password,"1234567")

    def test_save_cridentials(self):
        '''
        This function test for saving of cridentials and passwords
        '''
        for app in self.apps:
            self.cridentials.save_cridentials(app)
            self.assertEqual(len(cri.social_accounts[app]),1)

    def tearDown(self):
        '''
        '''
        for app in self.apps:
            cri.social_accounts[app]= []


    def test_delete_cridentials(self):
        '''
        This function tests whether a user can delete cridentials
        '''
        for app in self.apps:
            self.cridentials.save_cridentials(app)
            self.cridentials.delete_cridentials(app)
            self.assertEqual(len(cri.social_accounts[app]),0)

    def test_generate_password(self):
        '''
        This Function tests whether the app can generate a passwords
        '''
        self.cridentials.save_cridentials("instagram")
        self.assertNotEqual(cri.social_accounts["instagram"][0].password,cri.generate_password("John",9))

    def test_display_cridentials(self):
        '''
        This function tests for display of new_cridentials
        '''
        for app in self.apps:
            self.cridentials.save_cridentials(app)
            self.assertEqual(cri.social_accounts[app][0],cri.show_cridentials(app,0))
if __name__ == '__main__':
    unit.main()
