from user import account as ac
import unittest as unit

class TestUser (unit.TestCase):

    def setUp(self):
        '''
        This function creates a default user setUp
        '''
        self.new_account = ac("John","Doe","john@gmail.com","12johnDoes34",)

    def test_init(self):
        '''
        This function tests whether the users account has been initialized
        '''

        self.assertEqual(self.new_account.first_name,"John")
        self.assertEqual(self.new_account.last_name,"Doe")
        self.assertEqual(self.new_account.email,"john@gmail.com")
        self.assertEqual(self.new_account.password,"12johnDoes34")


if __name__ == '__main__':
    unit.main()
