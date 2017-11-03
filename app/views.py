from flask import render_template
from flask import request
from flask import jsonify, abort, request, jsonify, g, url_for
from flask_httpauth import HTTPBasicAuth

from app import app
from app.controller.UserController import UserController
from app.controller.RecipeController import RecipeController
from app.controller.CategoryController import CategoryController

user = UserController()
recipe = RecipeController()
category = CategoryController();
auth = HTTPBasicAuth()
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
 

@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(name=username_or_token).first()
        if not user:
            return False
    g.user = user
    return True

email = "adelinetush@gmail.com"

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Adeline','email':email} 
    return render_template('index.html', title='Home', user=user)

@app.route('/')
@app.route('/signup')
def signup():
    return render_template('signup.html', title='SignUp')

@app.route('/categories')
def categories():
    user = {'username': 'Adeline','email':email} 
    return render_template('categories.html', title='Categories', user=user)

@app.route('/recipes')
def recipes():
    user = {'username':'Adeline', 'email': email}
    return render_template('recipes.html', title='Recipes', user=user)

@app.route('/createrecipe')
def createrecipe():
    user = {'username': 'Adeline','email':email} 
    return render_template('createrecipe.html', title='CreateRecipe',user=user)

@app.route('/createcategory')
def createcategory():
    user = {'username': 'Adeline','email':email} 
    return render_template('createcategory.html', title='CreateCategory', user=user)


#Saving and retrieving
@app.route("/auth/register")
def register():
    name = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')
    if email is None or password is None:
        abort(400)
    response = user.register(name, email, password)
    print(response)
    return jsonify(response)

@app.route("/auth/login")
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    response = user.login(email, password)
    return jsonify(response)

#Sample auth functions
@app.route("/api/resource")
@auth.login_required
def get_resource():
    return jsonify({'data':'Hello there, %s' % g.user.name})

@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


#Recipe Functions
@app.route("/qu")
def listUserRecipes():
    username = request.args.get("username")
    response = recipe.get_user_recipes(username)
    return jsonify(response)

@app.route("/q")
def listRecipes():
    name = request.args.get("name")
    response = recipe.get_recipe(name);
    return jsonify(response)

@app.route("/ar",methods=['POST'])
def addRecipes():
    r = request.get_json()
    response = recipe.add_recipe(r)
    return jsonify(response)

#Category Functions
@app.route("/ac",methods=['POST'])
def addCategory():
    r = request.get_json()
    response = category.add_category(r)
    return jsonify(response)


@app.route("/guc")
def get_user_category():
    email = request.args.get('email')
    res = category.get_user_category(email)
    return jsonify(res)

@app.route("/gac")
def get_all_category():
    res = category.get_all_category()
    return jsonify(res)

@app.route("/dc")
def delete_category():
    id = request.args.get('id')
    ir = int(id)
    res = category.delete_category(ir)
    return jsonify(res)