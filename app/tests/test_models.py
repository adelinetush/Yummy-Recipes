import unittest

from flask import render_template
from flask import request
from flask import jsonify, abort, request, jsonify, g, url_for

from app import app
from app.models import db
from app.models.model.Model import Category
from app.models.model.Model import Recipe
from app.models.model.Model import User

class test_category_model(unittest.TestCase):

        def test_serialize(self):
            r = Category("adelinetush@gmail.com","Yummy",'Yummy foods')
            self.assertIsInstance(r.serialize(),object)

class test_recipe_model(unittest.TestCase):
    
        def test_serialize(self):
            r = Recipe(1,"Pumpkin Pie","adelinetush@gmail.com","Yummy",'')
            self.assertIsInstance(r.serialize(),object)

class test_user_model(unittest.TestCase):
    
        def test_serialize(self):
            u = User("adeline","adelinetush@gmail.com","youwish")
            self.assertIsInstance(u.serialize(),object)