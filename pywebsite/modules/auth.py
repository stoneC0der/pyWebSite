from flask import session
def isLoggedIn() :
  if '_userId' in session :
    return True
  return False

# Store the logged user in the session for authentication purpose
def logInUser(_user) :
  # print(_user)
  session['_userId'] = _user['user_id']
  session['_username'] = _user['name']
  session['_role'] = _user['role']
  # print(session)

# Check if the user is admin
def isAdmin() :
  if '_role' in session and '_role' == 1:
    return True
  return False