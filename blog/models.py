from blog import db,app
from datetime import datetime
from blog import login_manager
from flask_login import UserMixin
from flask_security import Security, SQLAlchemyUserDatastore,UserMixin, RoleMixin
from flask_security.forms import RegisterForm
from wtforms.validators import ValidationError
from wtforms import StringField



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#Roles And User Relationship
roles_users = db.Table('roles_users',db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image=db.Column(db.String(20),nullable=False,default='zero.jpg')
    password=db.Column(db.String(60),nullable=False)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,backref=db.backref('users', lazy='dynamic'))
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image}')"

class ExtendedRegisterForm(RegisterForm):
    username=StringField('username')
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('The Username Exist')
# Setup For Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore,register_form=ExtendedRegisterForm)

class Class(db.Model):
    id=db.Column(db.Integer,primary_key=True,unique=True)
    name=db.Column(db.String,nullable=False)

class Subject(db.Model):
    id=db.Column(db.Integer,primary_key=True,unique=True)
    name=db.Column(db.String(40),nullable=False)
    number=db.Column(db.Integer,nullable=False)
        

class Employee(db.Model):
    id=db.Column(db.Integer,primary_key=True,unique=True)
    name=db.Column(db.String(40),nullable=False)
    fathername=db.Column(db.String(40),nullable=False)
    position_id=db.Column(db.Integer,db.ForeignKey('position.id'))
    position=db.relationship('Position',backref=db.backref('positions',lazy=True))
    nic=db.Column(db.Integer,nullable=False)
    age=db.Column(db.Integer,nullable=False)
    salary=db.Column(db.Integer,default=0)
    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

class Position(db.Model):
    id=db.Column(db.Integer,primary_key=True,unique=True)
    name=db.Column(db.String(40),nullable=False)
    
class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True,unique=True)
    name=db.Column(db.String(40),nullable=False)
    fathername=db.Column(db.String(40),nullable=False)
    class_id=db.Column(db.Integer,db.ForeignKey('class.id'))
    clas=db.relationship('Class',backref=db.backref('classess',lazy=True))
    nic=db.Column(db.Integer,nullable=False)
    age=db.Column(db.Integer,nullable=False)
    fees=db.Column(db.Integer,default=0)
    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)



class Tools(db.Model):
    id=db.Column(db.Integer,primary_key=True,unique=True)
    tool_id=db.Column(db.Integer,db.ForeignKey('tool.id'))
    tool=db.relationship('Tool',backref=db.backref('tools',lazy=True))
    number=db.Column(db.Integer,default=0)
    money=db.Column(db.Integer,nullable=False)
    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

class FewTools(db.Model):
    id=db.Column(db.Integer,primary_key=True,unique=True)
    tool_id=db.Column(db.Integer,db.ForeignKey('tool.id'))
    tool=db.relationship('Tool',backref=db.backref('tool',lazy=True))
    number=db.Column(db.Integer,default=0)
    money=db.Column(db.Integer,nullable=False)
    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

class Tool(db.Model):
    id=db.Column(db.Integer,primary_key=True,unique=True)
    name=db.Column(db.String(40),nullable=False)

class Limit(db.Model):
    id=db.Column(db.Integer,primary_key=True,unique=True)
    student=db.Column(db.Integer,nullable=False)
    employee=db.Column(db.Integer,nullable=False)
    clas=db.Column(db.Integer,nullable=False)
