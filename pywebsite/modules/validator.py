import re, sys

# Store errors
error = {}
'''
Validate user input
''' 
def validate(data) :
    # Validate name
  if data['name'] :
    if not re.match("[a-zA-Z0-9]*", data['name'], re.I | re.M) :
      error['name_erro'] = 'Invalid Name'
    # Validate email
  if data['email'] :
    if not re.match("^([a-zA-Z0-9])+@\\w+\\.\\w+[^\\s]", data['email'], re.I | re.M) :
      error['email_err'] = "Invalid email"
    # Validate message/textarea
  if data['message'] :
    if not re.match("([a-zA-Z0-9_@\\?;'\",\\.:-])*", data['message'], re.I | re.M):
      error['message_erro'] = 'Invalid Name'