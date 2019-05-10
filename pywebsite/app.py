# First we imported the Flask class. An instance of this class will be our WSGI application.
from flask import Flask, render_template as render, url_for, request as req, redirect, json, Response as response, flash
# Login Controller module
from modules import ContactController as ConControl, LoginController as loginControl, auth
'''
Next we create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name will be different ('__main__' versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on. For more information have a look at the Flask documentation.
'''
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# We then use the route() decorator to tell Flask what URL should trigger our function.
# Home page
@app.route('/')
# The function is given a name which is also used to generate URLs for that particular function, and returns the page we want to display in the user’s browser.
def main() :
  return render('index.html')

@app.route('/')
def index() :
  return render('index.html')

# We can pass the accepted method in the route	
# @app.route('/about')
# def about() :
# 	return render('index.html')

# Show admin dashboard
@app.route('/admin', methods=['GET'])
def admin() :
  if auth.isLoggedIn() :
    return render('admin/index.html')
  return redirect(url_for('index'))

#  Login the user Ajax based
@app.route('/login', methods=['POST'])
def login() :
  _name = req.form['username']
  _password = req.form['password']
  _data = {"email" : _name, "password" : _password}

  # Validate the inpute values
  if _name  and _password:
    if loginControl.signIn(_data) :
      # _html = render('admin/index.html')
      # return json.dumps({'data' : _html})
      # return json.dumps({'html' : '<span class="bg-success">Welcome back' + _name + '!</span>'})
      # flash('You were successfully logged in')
      return response("{'html' : '<span class=\"bg-success\">Welcome back' + _name + '!</span>'}", status=200)
      # Without ajax
      # return redirect(url_for('admin', next='/admin'))
    else :
      return response("{'html' : '<span>Invalid email or password!</span>'}", status=409)
  else:
    return response("{'html' : '<span>Enter the required fields!</span>'}", status=400)
    # return json.dumps({'html':'<span>Enter the required fields</span>'})
#  logout
@app.route('/logout')
def logout() :
  if loginControl.logout() :
    return redirect(url_for('index'))

# Show profile Viewed by other users
@app.route('/user/<_username>', methods=['GET'])
def profile(_username) :
  return '{}\'s profile'.format(_username) # this is rendered as username's profile
  # return render('/auth/login.html', data=ConControl.getData())

# Show contact form
@app.route('/contact', methods=['POST','GET'])
def contact() :
  # error variable
  error = None
  if req.method == 'POST' :
    if "newsletter" in req.form :
      info = {
      'name' : req.form['name'],
      'email' : req.form['email'],
      'newsletter' : True,
      'message' : req.form['message']
      }
    else :
      info = {
        'name' : req.form['name'],
        'email' : req.form['email'],
        'newsletter' : False,
        'message' : req.form['message']
        }
    if ConControl.store(info) :
      return redirect(url_for('admin'))
    else :
      return redirect(url_for('contact'))
  else :
    return render('contact.html')

# @pp.route('/404', methods['GET'])
# def _404() :
  
# Next, check if the executed file is the main program and run the app
if __name__ == "__main__" :
  app.run()