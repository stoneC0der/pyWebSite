# Import sqlite3 module
import sqlite3 as sql
from sqlite3 import Error
# from werkzeug import generate_password_hash as password_hash, check_password_hash as check_hash

# con.execute('DROP TABLE pyweb_db.sqlite3')

# con.execute('CREATE TABLE `tbl_users` (user_id INT AUTO_INCREMENT, name TEXT, email TEXT, password TEXT, city TEXT, role BOOLEAN(1),PRIMARY KEY (`user_id`))')

# print("Table created successfully")

# _hashed_password = password_hash('123456')

# con.execute("INSERT INTO tbl_users (`name`,`email`,`password`,`city`,`role`) VALUES('johndoe','johndoe@gmail.com','123456','Accra','1')")

''''
Connect to the database
Return tuple _con
'''
def getDB(_db_file) :
  """ create a database connection to the SQLite database
  specified by the db_file
  :param db_file: database file
  :return: Connection object or None
  """
  try :
    _con = sql.connect(_db_file)
    print ("Opened database successfully")
    return _con
  except Error as _e :
    print(_e)
  return None

# Define a raw factory function to convert tuple as dictionary
def dict_factory(_cur,_row) :
  _dic = {}
  for _index, _col in enumerate(_cur.description) :
    _dic[_col[0]] = _row[_index]
  return _dic

# TODO:  Change the way user login, findUserByEmail should only be use to check if email is taken using ajax, so no need to retrieve id for login we'll just use email & passowrd
# data = {'email':'johndoe@gmail.com','password':'123456'}

''''
Check if the user info exists, if yes return True, False otherwise
Used for log in the user
return Boolean
'''
def findUser(_con,_data) :
  _con.row_factory = dict_factory
  _cur = _con.cursor()
  _email = _data['email']
  # _hashed_password = password_hash(data['password'])
  _password = _data['password']
  # print(_password)
  _id = findUserByEmail(_con,_email)
  
  if _id :
    _cur.execute('SELECT * FROM tbl_users WHERE `user_id`=? AND password=?', (_id,_password))
    _user = _cur.fetchall()
    if _user :
      print('User exists!')
      for _u in _user :
        return _u
    else :
      print('Not Does not exists!')
      return False

'''
Get userId by email
return Int _id the username
Used to check if email is already taken via ajax
'''
def findUserByEmail(_con,_email) :
  _con.row_factory = dict_factory
  _cur = _con.cursor()
  
  if _email :
    # sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 17 supplied.
    # You need to pass in a sequence, but you forgot the comma to make your parameters a tuple:
    _cur.execute('SELECT user_id FROM tbl_users WHERE email=?',(_email,))
    _id = _cur.fetchall()
    if _id :
      for _user_id in _id :
        # print(_user_id['user_id'])
        return _user_id['user_id']
    else :
      return 0
  return 'Email not found'

# exit()
# _data = {'email':'johndoe@gmail.com', 'password':'123456'}
# findUser(getDB('pyweb_db.sqlite'),_data)

'''
Where you make your connection to the database add the following.

conn = sqlite3.connect('your.db', check_same_thread=False)

is this safe to use?
I don't see why not, as long as you do your own synchronization to ensure only one thread uses the object at the same time. 

Some additional info for future readers of this thread. Per docs.python.org/3/library/sqlite3.html: By default, check_same_thread is True and only the creating thread may use the connection. If set False, the returned connection may be shared across multiple threads. When using multiple threads with the same connection writing operations should be serialized by the user to avoid data corruption.
'''