from modules import db

_db_file = 'pyweb_db.sqlite'
#  For test
_data = {'email':'johndoe@gmail.com', 'password':'123456'}
def UserExists(_data) :
  _con = db.getDB(_db_file)
  _user = db.findUser(_con,_data)
  if _user :
    _con.close()
    # print(_user['user_id'])
    print ("Database closed")
    return _user
  else :
    print ("Error")
    return False

# UserExists(_data)