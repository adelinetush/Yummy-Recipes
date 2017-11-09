import unittest

from app.models.Category import Category

class test_category(unittest.TestCase):
    
    def test_get_name(self):
        r = Category(1,"adelinetush@gmail.com","Yummy",'Yummy foods')
        self.assertEqual(r.set_name('Yummy'),r.get_name())

    def test_get_description(self):
        r = Category(1,"adelinetush@gmail.com","Yummy",'Yummy foods')
        self.assertEqual(r.set_description('Yummy foods'),r.get_description())
    
    def test_serialize(self):
        r = Category(1,"adelinetush@gmail.com","Yummy",'Yummy foods')
        self.assertIsInstance(r.serialize(),object)
        

if(__name__=='__main__'):
    unittest.main()