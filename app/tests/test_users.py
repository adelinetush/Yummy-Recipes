import unittest
from app.models.User import User

class test_user(unittest.TestCase):
    
    def test_get_username(self):
        u = User("adeline","youwish")
        self.assertEqual("adeline", u.get_username())

    def test_get_password(self):
        u = User("adeline","youwish")
        self.assertEqual("youwish", u.get_password())

if(__name__=='__main__'):
    unittest.main()