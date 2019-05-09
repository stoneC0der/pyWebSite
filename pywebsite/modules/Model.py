from modules import db

_db_file = 'pyweb_db.sqlite'

def UserExists(_data) :
  con = db.getDB(_db_file)
  if db.findUser(con,_data) :
    con.close()
    print ("Database closed")
    return True
  else :
    print ("Error")
    return False