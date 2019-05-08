# First we imported the Flask class. An instance of this class will be our WSGI application.
from flask import Flask, render_template as render, url_for, request as req, redirect
import LoginController as lC
'''
 Next we create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name will be different ('__main__' versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on. For more information have a look at the Flask documentation.
 '''
app = Flask(__name__)
# We then use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
# The function is given a name which is also used to generate URLs for that particular function, and returns the page we want to display in the user’s browser.
def hello_world() :
	return render('index.html')
	
# We can pass the accepted method in the route	
@app.route('/#about', methods=['GET'])
def about() :
	return render('index.html')

@app.route('/login', methods=['GET'])
def login(data=None) :
    return render('login.html', data=lC.getData())
# url_for('static', filename='favicon.png')
	
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
        if lC.store(info) :
            return redirect(url_for('login'))
        else :
            return redirect(url_for('contact'))
    else :
	    return render('contact.html')