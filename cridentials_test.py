from cridentials import cridentials as cri
import unittest as unit

class TestCridentials(unit.TestCase) :
    '''
    This class is used to test user cridentials
    '''
    def setUp(self):

        self.cridentials = cri("Steve Mitto","mitto@gmail.com","1234567")
        self.apps=['instagram','twitter','facebook','linkedin','snapchat']


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
            return True


    def test_delete_cridentials(self):
        '''
        This function tests whether a user can delete cridentials
        '''
        for app in self.apps:
            self.cridentials.save_cridentials(app)
            self.cridentials.delete_cridentials(app)
            self.assertEqual(len(cri.social_accounts[app]),0)



if __name__ == '__main__':
    unit.main()
