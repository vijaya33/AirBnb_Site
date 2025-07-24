from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models import User, Property
from flask_login import login_user, logout_user, login_required

@app.route('/')
def home():
    properties = Property.query.all()
    return render_template('home.html', properties=properties)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Implement login form handling
    pass

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Implement user registration form
    pass

@app.route('/add_property', methods=['GET', 'POST'])
@login_required
def add_property():
    # Form for host to add a property
    pass

# Begin - Below code is exact same as code above this comment, it has been typed below as a practice code blocks. 


from flask import render_template, redirect, url_for, request, flash
from app import app, db 
from app.models import User, Property
from flask_login import login_user, logout_user, login_required

@app.route('/')
def home(): 
    properties = Property.query.all()
    return render_template('home.html', properties=properties)

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    #implement login from handling 
    pass 

@app.route('/register', methods=['GET','POST'])
def register(): 
    #Implement user registration form here in this method / function definition. 
    pass 

@app.route('/add_property', methods=['GET','POST'])

@login_required
def add_property(): 
    #Form for host to add a property - definition here. 
    pass 


# End - Below code is exact same as code above this comment, it has been typed below as a practice code blocks. 
