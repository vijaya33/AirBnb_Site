from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(200))
    is_host = db.Column(db.Boolean, default=False)

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Begin - This code below is typed as a test practice code. 


    from app import db 
    from flask_login import UserMixin 

    class User(db.Model, UserMixin) : 
        id = db.Column(db.Integer, primary_ley = True)
        username = db.Column(db.String(80), unique=True)
        email = db.Column(db.String(120), unique=True)
        password = db.Column(db.String(200))
        is_host = db.Column(db.Boolean, default=False)

    class Property(db.Model): 
        id=db.Column(db.Integer, primary_key = True)
        title = db.Column(db.String(120))
        description = db.Column(db.Text)
        price=db.Column(db.Float)
        host_id = db.Column(db.Integer, db.ForeignKey('user.id'))


 # End - This code below is typed as a test practice code. 