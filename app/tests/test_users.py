import unittest
from app.models.User import User

class test_user(unittest.TestCase):
    
    def test_get_username(self):
        u = User("adeline","adelinetush@gmail.com","youwish")
        self.assertEqual("adeline", u.get_username())

    def test_get_password(self):
        u = User("adeline","adelinetush@gmail.com","youwish")
        self.assertEqual("youwish", u.get_password())
        
    def test_get_email(self):
        u = User("adeline","adelinetush@gmail.com","youwish")
        self.assertEqual("adelinetush@gmail.com", u.get_email())
    
    def test_serialize(self):
        u = User("adeline","adelinetush@gmail.com","youwish")
        self.assertIsInstance(u.serialize(),object)

if(__name__=='__main__'):
    unittest.main()