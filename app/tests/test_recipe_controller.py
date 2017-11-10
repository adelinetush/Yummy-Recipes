import unittest

from flask import render_template
from flask import request
from flask import jsonify, abort, request, jsonify, g, url_for
import random

from app import app
from app.models import db
from app.models.model.Model import Recipe
from app.controller.RecipeController import RecipeController




recipe = RecipeController();

class test_category_controller(unittest.TestCase):
    
    def test_add_recipe_memory(self):
        r = dict()
        r['category'] = 1
        r['name'] = 'test'
        r['email'] = 'adelinetush@gmail.com'
        r['description'] = 'test description'
        r['ingredients'] = []
        response = recipe.add_recipe_memory(r)
        self.assertEqual(len(response),1)

    def test_get_recipe_memory(self):
        r = dict()
        r['category'] = 1
        r['name'] = 'test'
        r['email'] = 'adelinetush@gmail.com'
        r['description'] = 'test description'
        r['ingredients'] = []
        response = recipe.add_recipe_memory(r)
        response = recipe.get_recipe_memory('test')
        self.assertEqual(response[1]['name'], r['name'])

    def test_get_user_recipe_memory(self):
        r = dict()
        r['category'] = 1
        r['name'] = 'test'
        r['email'] = 'adelinetush@gmail.com'
        r['description'] = 'test description'
        r['ingredients'] = []
        t = random.randint(1,101)
        for x in range(t):
            response = recipe.add_recipe_memory(r)
        response = recipe.get_user_recipes_memory('adelinetush@gmail.com')
        self.assertEqual(len(response)-2, t)


    