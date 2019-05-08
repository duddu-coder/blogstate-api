from flask import Flask
from flask import request
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
# from flaskext.mysql import MySQL
import os
import json
# from database.config import db


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(10)

ACTUAL_USERNAME = 'roshnet'
# ACTUAL_PASSWORD = generate_password_hash('password123')

# app.config['MYSQL_DATABASE_HOST'] = db['host']
# app.config['MYSQL_DATABASE_USER'] = db['user']
# app.config['MYSQL_DATABASE_PASSWORD'] = db['password']
# app.config['MYSQL_DATABASE_DB'] = db['name']

# mysql = MySQL()
# mysql.init_app(app)

# conn = mysql.connect()
# cur = conn.cursor()


@app.route('/')
def index():
    return 'This is an API for BlogState'


@app.route('/login', methods=['POST'])
def verify_login():
    username = request.get_json('username')
    passwd = request.get_json('passwd')

    if username == ACTUAL_USERNAME:
            return json.dumps({"status": "1"})
    else:
        return json.dumps({"status": "0"})

if __name__ == '__main__':
    app.run(debug=True)