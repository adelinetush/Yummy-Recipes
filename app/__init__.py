from flask import Flask

app = Flask(__name__)

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

from app.models import db




POSTGRES = {
    'user': 'postgres',
    'pw': 'root',
    'db': 'yummy',
    'host': 'localhost',
    'port': '5432',
}
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/yummy'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)

from app import views
