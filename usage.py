import requests
import os
from werkzeug.security import generate_password_hash

api_base = 'http://127.0.0.1:5000'

username = 'roshnet' # To be obtained from request.form['username']
passwd = 'password123' # To be obtained from request.form['passwd']

passwd = generate_password_hash(passwd)

endpt = os.path.join(api_base, 'login')
headers = {'content-type': 'application/json'}
data = {
    "username": username,
    "passwd": passwd
}

login_response = requests.post(endpt, json=data, headers=headers)
if login_response.status_code == 200:
    login_response = login_response.json()
    print(login_response['status'])
else:
    print('Request failed: {}'.format(login_response.status_code))
