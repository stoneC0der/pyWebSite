from modules import Model

def login(_data) :
  if Model.UserExists(_data) :
    return True
  return False