import user as us
import unittest as unit

class TestUser (unit.TestCase):

    def setUp(self):
        '''
        This function creates a default user setUp
        '''
        us.account("John","Doe","john@gmail.com","12johnDoes34",)
