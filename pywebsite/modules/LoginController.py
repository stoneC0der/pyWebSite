from modules import Model, auth
from flask import session, url_for, redirect, Flask

# app = Flask(__name__)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
def signIn(_data) :
  _user = Model.UserExists(_data)
  if _user :
    auth.logInUser(_user)
    return True
  return False

def logout() :
  session.pop('_userId',None)
  session.pop('_username',None)
  session.pop('_role',None)
  return True

# for texting 
# _data = {'email':'johndoe@gmail.com', 'password':'123456'}
# with app.test_request_context():
#   login(_data)