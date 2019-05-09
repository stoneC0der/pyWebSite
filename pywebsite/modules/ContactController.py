import re, sys
from modules import ModelSaveToFile as message, Model

error = {}
'''
Validate user input
''' 
def validate(data) :
  # Validate name
  if not re.match("[a-zA-Z0-9]*", data['name'], re.I | re.M) :
    error['name_erro'] = 'Invalid Name'
  # Validate email
  if not re.match("^([a-zA-Z0-9])+@\\w+\\.\\w+[^\\s]", data['email'], re.I | re.M) :
    error['email_err'] = "Invalid email"
  # Validate message/textarea
  if not re.match("([a-zA-Z0-9_@\\?;'\",\\.:-])*", data['message'], re.I | re.M):
    error['message_erro'] = 'Invalid Name'

def store(request) :
  data = {}
  saved = None
  data['name'] = request['name']
  data['email'] = request['email']
  # if "newsletter" in request and request['newsletter'] != '' :
  data['newsletter'] = request['newsletter']
  data['message'] = request['message']
  # Validate data
  validate(data)
  # return True
  if not error :
    saved = message.save(data)
    if not saved :
      return False
    return True
  return False

def getData() :
  data = message.readFile()
  if len(data) < 1 :
    return data
  return []