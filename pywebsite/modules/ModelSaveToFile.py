data = {}
def saveToFile(data) :
  userFile = open("/Users/stonecoder/pywebsite/pywebsite/doc/User.txt", "a")
  # Loop through the dictionary and return the key->value
  # txt = ', '.join("{!s}={!r}".format(key,val) for key,val in data.items())
  '''
  One liner convert dictionary to string
  can be write in multiple lines to
  '''
  txt = ', '.join("{!s}".format(val) for val in data.values())
  userFile.write(txt + '\n')
  userFile.close()
  return True

def save(data) :
  if not saveToFile(data) :
    return False
  return True

def readFile() :
  # Getting a file not found because it's empty
  # f = open('/py../doc/User.txt', 'r')
  # NOTE:  Change Absolute path to a more dynamic one
  with open('/Users/stonecoder/pywebsite/pywebsite/doc/User.txt', 'r') as f :
    info = f.read().split('\n')
  f.close()
  return info