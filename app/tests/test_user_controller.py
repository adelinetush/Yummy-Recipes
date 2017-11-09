import unittest

from flask import render_template
from flask import request
from flask import jsonify, abort, request, jsonify, g, url_for

from app import app
from app.models import db
from app.models.model.Model import Category
from app.controller.UserController import UserController


user  = UserController();
class test_user_controller(unittest.TestCase):
    
    def test_register_memory(self):
        total = len(user.users)
        u = user.register_memory('adetush', 'adelinetush@gmail.com', 'ade123')
        self.assertEqual(len(user.users),total+1)
    

