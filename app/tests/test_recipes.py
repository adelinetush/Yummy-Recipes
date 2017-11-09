import unittest
import random

from app.models.Recipe import Recipe

class test_recipe(unittest.TestCase):
    
    def test_get_ingredient(self):
        r = Recipe(1,"Pumpkin Pie","adelinetush@gmail.com","Yummy",[])
        t = random.randint(1,101)
        for x in range(t):
            r.add_ingredient("Pumpkin x ");
        r.get_ingredients()
        self.assertEqual(len(r.ingredients),t)

    def test_add_recipe(self):
        r = Recipe(1,"Pumpkin Pie","adelinetush@gmail.com","Yummy",[])
        r.add_ingredient("flour")
        self.assertEqual((r.get_ingredients())[0],"flour")

    def test_get_ingredients_adds_value(self):
        r = Recipe(1,"Pumpkin Pie","adelinetush@gmail.com","Yummy",[])
        r.add_ingredient("Pumpkin");
        self.assertEqual(len(r.get_ingredients()),1)
    
    def test_set_category(self):
        r = Recipe(1,"Pumpkin Pie","adelinetush@gmail.com","Yummy",[])
        r.add_ingredient("Pumpkin");
        category = 2
        r.set_category(category)
        self.assertEqual(category,r.category)



    def test_remove_ingredient(self):
        r = Recipe(1,"Pumpkin Pie","adelinetush@gmail.com","Yummy",[])
        r.add_ingredient("Pumpkin");
        r.remove_ingredient("Pumpkin")
        self.assertEqual(len(r.ingredients),0)

    def test_serialize(self):
        r = Recipe(1,"Pumpkin Pie","adelinetush@gmail.com","Yummy",[])
        self.assertIsInstance(r.serialize(),object)
        

if(__name__=='__main__'):
    unittest.main()