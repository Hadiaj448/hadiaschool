from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,IntegerField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from blog.models import User
from flask_login import current_user



class ClassForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    submit=SubmitField('Post')
   

class SubjectForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    number=IntegerField('Class Number',validators=[DataRequired()])
    submit=SubmitField('Post')



class EmployeeForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    fathername=StringField('FatherName',validators=[DataRequired()])
    nic=IntegerField('NIC',validators=[DataRequired()])
    age=IntegerField('Age',validators=[DataRequired()])
    salary=IntegerField('Salary',default=0)
    submit=SubmitField('Add')

class PositionForm(FlaskForm):
    name=StringField('Position Name',validators=[DataRequired()])
    submit=SubmitField('Add')   

class StudentForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    fathername=StringField('FatherName',validators=[DataRequired()])
    nic=IntegerField('NIC',validators=[DataRequired()])
    age=IntegerField('Age',validators=[DataRequired()])
    fees=IntegerField('Fees',default=0)
    submit=SubmitField('Add')

class ToolsForm(FlaskForm):
    number=IntegerField('How Many',default=0)
    money=IntegerField('How Much',default=0)
    submit=SubmitField('Add')

class FewToolsForm(FlaskForm):
    number=IntegerField('How Many',default=0)
    money=IntegerField('How Much',default=0)
    submit=SubmitField('Add')

class ToolForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    submit=SubmitField('Add')
class LimitForm(FlaskForm):
    student=IntegerField('Student Limit',validators=[DataRequired()])
    employee=IntegerField('Employee LImit',validators=[DataRequired()])
    clas=IntegerField('Class LImit',validators=[DataRequired()])
    submit=SubmitField('Add')