# Import sqlite3 module
import sqlite3 as sql
from sqlite3 import Error
# from werkzeug import generate_password_hash as password_hash, check_password_hash as check_hash

# con.execute('DROP TABLE pyweb_db.sqlite3')

# con.execute('CREATE TABLE `tbl_users` (user_id INT AUTO_INCREMENT, name TEXT, email TEXT, password TEXT, city TEXT, role BOOLEAN(1),PRIMARY KEY (`user_id`))')

# print("Table created successfully")

# _hashed_password = password_hash('123456')

# con.execute("INSERT INTO tbl_users (`name`,`email`,`password`,`city`,`role`) VALUES('johndoe','johndoe@gmail.com','123456','Accra','1')")

def getDB(_db_file) :
  """ create a database connection to the SQLite database
  specified by the db_file
  :param db_file: database file
  :return: Connection object or None
  """
  try :
    con = sql.connect(_db_file)
    print ("Opened database successfully")
    return con
  except Error as e :
    print(e)
  return None
# TODO:  Change the way user login, findUserByEmail should only be use to check if email is taken using ajax, so no need to retrieve id for login we'll just use email & passowrd
# data = {'email':'johndoe@gmail.com','password':'123456'}
def findUser(con,data) :
  cur = con.cursor()
  _email = data['email']
  # _hashed_password = password_hash(data['password'])
  _password = data['password']
  # print(_password)
  _id = findUserByEmail(con,_email)
  
  if _id :
    cur.execute('SELECT * FROM tbl_users WHERE `user_id`=? AND password=?', (_id[0],_password))
    _user = cur.fetchall()
    if _user :
      print('User exists!')
      return True
    else :
      print('Not Does not exists!')
      return False

def findUserByEmail(con,_email) :
  cur = con.cursor()
  
  if _email :
    # sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 17 supplied.
    # You need to pass in a sequence, but you forgot the comma to make your parameters a tuple:
    cur.execute('SELECT user_id FROM tbl_users WHERE email=?',(_email,))
    _id = cur.fetchall()
    if _id :
      for _user_id in _id :
        # print(_user_id[0])
        return _user_id
    else :
      return 0
  return 'Email not found'

# exit()
# findUser(con,data)

'''
Where you make your connection to the database add the following.

conn = sqlite3.connect('your.db', check_same_thread=False)

is this safe to use?
I don't see why not, as long as you do your own synchronization to ensure only one thread uses the object at the same time. 

Some additional info for future readers of this thread. Per docs.python.org/3/library/sqlite3.html: By default, check_same_thread is True and only the creating thread may use the connection. If set False, the returned connection may be shared across multiple threads. When using multiple threads with the same connection writing operations should be serialized by the user to avoid data corruption.
'''