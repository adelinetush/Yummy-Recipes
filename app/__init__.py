from flask import Flask

app = Flask(__name__)

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

from app import views
