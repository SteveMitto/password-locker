from cridentials import cridentials as cri
import unittest as unit

class TestCridentials(unit.TestCase) :
    '''
    This class is used to test user cridentials
    '''
    def setUp(self):

        self.cridentials = cri("Steve Mitto","mitto@gmail.com","1234567")

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
        apps=['instagram','twitter','facebook','linkedin','snapchat']

        for app in apps:
            self.cridentials.save_cridentials(app)
            self.assertEqual(len(cri.social_accounts[app]),1)


if __name__ == '__main__':
    unit.main()
