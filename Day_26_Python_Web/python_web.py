# ------ Python For Web ------

#  In this section, we will see how we use Python for the web. There are many Python web frame works.
#  Django and Flask are the most popular ones.

# ------ Flask ------

# Flask is a web development framework written in Python. Flask uses Jinja2 template engine.
# Flask can be also used with other modern front libraries such as React.
# If you did not install the virtualenv package yet install it first.
# Virtual environment allows us to isolate project dependencies from the local machine dependencies.

# --- Setting Up Project Directory ---

# Follow the following steps to get started with Flask:

# Step 1: install virtualenv using the following command.
# >> pip install virtualenv

# Step 2:
# C:\Users\adams\PycharmProjects\30DaysOfPython> mkdir python_for_web
# C:\Users\adams\PycharmProjects\30DaysOfPython> cd python_for_web/
# C:\Users\adams\PycharmProjects\30DaysOfPython\python_for_web> python -m venv venv
# C:\Users\adams\PycharmProjects\30DaysOfPython\python_for_web> .\venv\Scripts\Activate
# (venv) PS C:\Users\adams\PycharmProjects\30DaysOfPython\python_for_web> pip freeze
# (venv) PS C:\Users\adams\PycharmProjects\30DaysOfPython\python_for_web> pip install Flask
# (venv) PS C:\Users\adams\PycharmProjects\30DaysOfPython\python_for_web> pip freeze
# blinker==1.9.0
# click==8.3.1
# colorama==0.4.6
# Flask==3.1.2
# itsdangerous==2.2.0
# Jinja2==3.1.6
# MarkupSafe==3.0.3
# Werkzeug==3.1.5
# (venv) PS C:\Users\adams\PycharmProjects\30DaysOfPython\python_for_web>

# We created a project directory named python_for_web. Inside the project we created a virtual environment venv.
# Then we activated the virtual environment. We used pip freeze to check the installed packages in the directory.
# The result of pip freeze was empty because a package was not installed yet.
# Now, let's create app.py file in the project directory and write the following code.
# The app.py file will be the main file in the project. The following code has flask module, os module.

# --- Creating Routes ---

# The Home route
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')  # this decorator creates the home route
def home ():
    return '<h1>Welcome!</h1>'

@app.route('/about')
def about ():
    return '<h1>About Us</h1>'

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

# To run the flask application, write python app.py in the main flask application directory.
# After you run python app.py check local host 5000.

# Now, we added the about route in the above code. How about if we want to render an HTML file instead of string?
# It is possible to render HTML file using the function render_template.
# Let us create a folder called templates and create home.html and about.html in the project directory.
# Let us also import the render_template function from flask.

# --- Creating Templates ---

# Create HTML files inside templates folder

# As you can see to go to different pages or to navigate we need a navigation.
# Let's add a link to each page or let's create a layout which we use to every page.

# --- Navigation ---

# <ul>
#   <li><a href="/">Home</a></li>
#   <li><a href="/about">About</a></li>
# </ul>

# Now, we can navigate between the pages using the above link. Let us create additional page which handle form data.
# You can call it any name, I like to call it post.html.
# We can inject data to the HTML files using Jinja2 template engine.

# --- Creating A Layout ---

# In the template files there is lots of repeated code. We can write a layout and remove the repetition.
# Let's create layout.html inside the templates folder. After we create the layout we will import to every file.

# --- Serving Static File ---

# Create a static folder in your project directory.
# Inside the static folder create CSS or styles folder and create a CSS stylesheet.
# We use the url_for module to serve the static file.

# Now, lets remove all the repeated code in the other template files and import the layout.html.
# The href is using url_for function with the name of the route function to connect each navigation route.

# There are different request methods(GET, POST, PUT, DELETE) are the common request methods
# which allow us to do CRUD(Create, Read, Update, Delete) operation.
# In the post route we will use GET and POST method alternative depending on the type of request,
# The request method is a function to handle request methods and also to access form data.

# So far, we have seen how to use templates and how to inject data to templates, how to do a common layout.
# Now, lets handle a static file. Create a folder called static in the project director and create a folder called css.
# Inside the css folder create main.css. Your main.css file will be linked to the layout.html.

# ------ Deployment ------

# --- Create Heroku Account ---

# Heroku provides a free deployment service for both front end and fullstack applications.
# Create an account on heroku and install the heroku CLI for you machine.
# After installing heroku write the following command:
# (venv) PS C:\Users\adams\PycharmProjects\30DaysOfPython\python_for_web> heroku login
# heroku: Press any key to open up the browser to login or q to exit:

# Let's see the result by clicking any key from the keyboard. When you press any key from you keyboard
# it will open the heroku login page and click the login page.
# Then you will local machine will be connected to the remote heroku server.
# If you are connected to remote server, you will see this:
# Logging in... done
# Logged in as adam.strahan@yahoo.com

# --- Create Requirements And Procfile ---

# Before we push our code to remote server, we need requirements.txt and Procfile.

# (venv) PS C:\Users\adams\PycharmProjects\30DaysOfPython\python_for_web> pip freeze
# blinker==1.9.0
# click==8.3.1
# colorama==0.4.6
# Flask==3.1.2
# itsdangerous==2.2.0
# Jinja2==3.1.6
# MarkupSafe==3.0.3
# Werkzeug==3.1.5
# (venv) PS C:\Users\adams\PycharmProjects\30DaysOfPython\python_for_web> pip freeze > requirements.txt
# (venv) PS C:\Users\adams\PycharmProjects\30DaysOfPython\python_for_web> ls
#     Directory: C:\Users\adams\PycharmProjects\30DaysOfPython\python_for_web
# Mode                 LastWriteTime         Length Name
# ----                 -------------         ------ ----
# d-----        10/02/2026     17:38                static
# d-----        11/02/2026     16:06                templates
# d-----        10/02/2026     16:10                venv
# -a----        11/02/2026     16:05           1244 app.py
# -a----        11/02/2026     16:57            268 requirements.txt
# (venv) PS C:\Users\adams\PycharmProjects\30DaysOfPython\python_for_web> New-Item Procfile

# NOTE: Procfile must NOT have .txt extension. If it does, use: Rename-Item Procfile.txt Procfile

# --- Push Project To Heroku ---

# Now, it is ready to be deployed. Steps to deploy the application on heroku:
# git init
# git add .
# git commit -m "commit message"
# heroku create 'name of the app as one word'
# git push heroku master
# heroku open(to launch the deployed application)