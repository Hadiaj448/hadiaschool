from blog import app,db,photos
from flask import render_template,redirect,flash,url_for,request,Response,session,current_app,jsonify
from flask_login import login_user,logout_user
from flask_security import  login_required,roles_accepted,current_user
from blog.models import User,user_datastore,Class,Subject,Student,Employee,Position,Tool,Tools,FewTools,Limit
from blog.forms import ClassForm,SubjectForm,StudentForm,EmployeeForm,PositionForm,ToolForm,ToolsForm,FewToolsForm,LimitForm
import secrets,os

    
@app.route('/')
def index():
    limit=Limit.query.first()
    x=Student.query.count()
    y=Employee.query.count()
    c=Class.query.count()
    employees=Employee.query.all()
    z=0
    for employee in employees:
        z+=employee.salary
    students=Student.query.all()
    w=0
    for student in students:
        w+=student.fees
    tools=Tools.query.all()
    r=0
    for tool in tools:
        r+=tool.money
    tool=FewTools.query.all()   
    e=0
    for t in tool:
        e+=t.money
    o=(w+r)-(z+e)
    return render_template('index.html',x=x,y=y,o=o,c=c,limit=limit)


#add position
@app.route('/addposition',methods=['GET','POST'])
def addposition():
    form=PositionForm()
    if form.validate_on_submit():
        addposition=Position(name=form.name.data)
        db.session.add(addposition)
        db.session.commit()
        flash('Your Position Added Succefully','success')
        return redirect(url_for('index'))
    return render_template('addposition.html',title='Add Position',form=form)

#add employee
@app.route('/addemployee',methods=['GET','POST'])
def addemployee():
    positions=Position.query.all()
    form=EmployeeForm()
    if form.validate_on_submit():
        name=form.name.data
        fathername=form.fathername.data
        nic=form.nic.data
        age=form.age.data
        salary=form.salary.data
        position=request.form.get('position')
        add=Employee(name=name,fathername=fathername,position_id=position,nic=nic,age=age,salary=salary)
        db.session.add(add)
        db.session.commit()
        flash(f'Employee Created Successfully','success')
        return redirect(url_for('index'))
    return render_template('addemployee.html',form=form,title='Add employee',positions=positions)

#add limit
@app.route('/addlimit',methods=['GET','POST'])
def addlimit():
    form=LimitForm()
    lmt=Limit.query.all()
    if form.validate_on_submit():
        student=form.student.data
        employee=form.employee.data
        clas=form.clas.data
        add=Limit(student=student,employee=employee,clas=clas)
        db.session.add(add)
        db.session.commit()
        flash(f'LImit Created Successfully','success')
        return redirect(url_for('addlimit'))
    return render_template('addlimit.html',form=form,title='Add Limit',lmt=lmt)

#add class
@app.route('/addclass',methods=['GET','POST'])
def addclass():
    form=ClassForm()
    if form.validate_on_submit():
        addclass=Class(name=form.name.data)
        db.session.add(addclass)
        db.session.commit()
        flash('Your Class Added Succefully','success')
        return redirect(url_for('index'))
    return render_template('addclass.html',title='Add Class',form=form)

#add student
@app.route('/addstudent',methods=['GET','POST'])
def addstudent():
    classess=Class.query.all()
    form=StudentForm()
    if form.validate_on_submit():
        name=form.name.data
        fathername=form.fathername.data
        clas=request.form.get('clas')
        nic=form.nic.data
        age=form.age.data
        fees=form.fees.data
        add=Student(name=name,fathername=fathername,class_id=clas,nic=nic,age=age,fees=fees)
        db.session.add(add)
        db.session.commit()
        flash(f'Student Created Successfully','success')
        return redirect(url_for('index'))
    return render_template('addstudent.html',form=form,title='Add Student',classess=classess)

#add Subject
@app.route('/addsubject',methods=['GET','POST'])
def addsubject():
    form=SubjectForm()
    if form.validate_on_submit():
        addsubject=Subject(name=form.name.data,number=form.number.data)
        db.session.add(addsubject)
        db.session.commit()
        flash('Your Subject Added Succefully','success')
        return redirect(url_for('index'))
    return render_template('addsubject.html',title='Add Subject',form=form)
#add Tool
@app.route('/addtool',methods=['GET','POST'])
def addtool():
    form=ToolForm()
    if form.validate_on_submit():
        addtool=Tool(name=form.name.data)
        db.session.add(addtool)
        db.session.commit()
        flash('Your Tool Added Succefully','success')
        return redirect(url_for('index'))
    return render_template('addtool.html',title='Add Tool',form=form)

#add Tools
@app.route('/addtools',methods=['GET','POST'])
def addtools():
    tools=Tool.query.all()
    form=ToolsForm()
    if form.validate_on_submit():
        number=form.number.data
        money=form.money.data
        tool=request.form.get('tool')
        add=Tools(number=number,money=money,tool_id=tool)
        db.session.add(add)
        db.session.commit()
        flash(f'Tools Created Successfully','success')
        return redirect(url_for('index'))
    return render_template('addtools.html',form=form,title='Add Tools',tools=tools)

#few tools
@app.route('/addfewtools',methods=['GET','POST'])
def addfewtools():
    tools=Tool.query.all()
    form=FewToolsForm()
    if form.validate_on_submit():
        number=form.number.data
        money=form.money.data
        tool=request.form.get('tool')
        add=FewTools(number=number,money=money,tool_id=tool)
        db.session.add(add)
        db.session.commit()
        flash(f'FewTools Created Successfully','success')
        return redirect(url_for('index'))
    return render_template('addfewtools.html',form=form,title='Add few Tools',tools=tools)

    
#show employee
@app.route('/showemployees',methods=['GET',"POST"])
def showemployees():
    employees=Employee.query.all()
    x=0
    for emp in employees:
        x+=emp.salary
    return render_template('showemployees.html',employees=employees,title='All employees',x=x)
#show classess
@app.route('/showclassess',methods=['GET',"POST"])
def showclassess():
    classess=Class.query.all()                                                               
    return render_template('showclassess.html',classess=classess,title='All Classess')
#show Tools
@app.route('/showtool',methods=['GET',"POST"])
def showtool():
    tools=Tool.query.all()                                                               
    return render_template('showtool.html',tools=tools,title='All Tools')
#show Positions
@app.route('/showpositions',methods=['GET',"POST"])
def showpositions():
    positions=Position.query.all()                                                               
    return render_template('showpositions.html',positions=positions,title='All positions') 

#show students
@app.route('/showstudents',methods=['GET',"POST"])
def showstudents():
    students=Student.query.all()
    x=0
    for fee in students:
        x+=fee.fees
    return render_template('showstudents.html',students=students,title='All students',x=x)
#show Subjects
@app.route('/showsubjects',methods=['GET',"POST"])
def showsubjects():
    subjects=Subject.query.all()
    return render_template('showsubjects.html',subjects=subjects,title='All subjects')


# show Tools
@app.route('/showtools',methods=['GET',"POST"])
def showtools():
    tools=Tools.query.all()
    x=0
    for t in tools:
        x+=t.money
    return render_template('showtools.html',tools=tools,title='All Tools',x=x)


#show Few Tools
@app.route('/showfewtools',methods=['GET',"POST"])
def showfewtools():
    tools=FewTools.query.all()
    x=0
    for t in tools:
        x+=t.money
    return render_template('showfewtools.html',tools=tools,title='All Tools',x=x)


#Edit Employee

@app.route('/editemployee/<int:id>',methods=['GET','POST'])
def editemployee(id):
    employee=Employee.query.get_or_404(id)
    positions=Position.query.all()
    form=EmployeeForm()
    if form.validate_on_submit():
        employee.name=form.name.data
        employee.fathername=form.fathername.data
        employee.nic=form.nic.data
        employee.age=form.age.data
        employee.salary=form.salary.data
        flash(f'Employee Successfully Updated','success')
        db.session.commit()
        return redirect(url_for('showemployees',employee_id=employee.id))
    elif request.method=='GET':
        form.name.data=employee.name
        form.fathername.data=employee.fathername
        form.nic.data=employee.nic
        form.age.data=employee.age
        form.salary.data=employee.salary
    return render_template('editemployee.html',form=form ,positions=positions,title="edit Employee")

#edit classess


@app.route('/editclass/<int:id>',methods=['GET','POST'])
def editclass(id):
    clas=Class.query.get_or_404(id)
    form=ClassForm()
    if form.validate_on_submit():
        clas.name=form.name.data
        flash(f'Class Successfully Updated','success')
        db.session.commit()
        return redirect(url_for('showclassess',clas_id=clas.id))
    elif request.method=='GET':
        form.name.data=clas.name
    return render_template('editclass.html',form=form,title="edit Class" )


#edit limit
@app.route('/editlimit/<int:id>',methods=['GET','POST'])
def editlimit(id):
    limit=Limit.query.get_or_404(id)
    form=LimitForm()
    if form.validate_on_submit():
        limit.student=form.student.data
        limit.employee=form.employee.data
        limit.clas=form.clas.data
        flash(f'limit Successfully Updated','success')
        db.session.commit()
        return redirect(url_for('addlimit'))
    elif request.method=='GET':
        form.student.data=limit.student
        form.employee.data=limit.employee
        form.clas.data=limit.clas
    return render_template('editlimit.html',form=form,title="edit limit" )
#edit Tool

@app.route('/edittool/<int:id>',methods=['GET','POST'])
def edittool(id):
    tool=Tool.query.get_or_404(id)
    form=ToolForm()
    if form.validate_on_submit():
        tool.name=form.name.data
        flash(f'Class Successfully Updated','success')
        db.session.commit()
        return redirect(url_for('showtool',tool_id=tool.id))
    elif request.method=='GET':
        form.name.data=tool.name
    return render_template('edittool.html',form=form,title="edit Tool" )

#edit Position

@app.route('/editposition/<int:id>',methods=['GET','POST'])
def editposition(id):
    position=Position.query.get_or_404(id)
    form=PositionForm()
    if form.validate_on_submit():
        position.name=form.name.data
        flash(f'Position Successfully Updated','success')
        db.session.commit()
        return redirect(url_for('showpositions',position_id=position.id))
    elif request.method=='GET':
        form.name.data=position.name
    return render_template('editposition.html',form=form,title="edit Postion" )


#edit Student

@app.route('/editstudent/<int:id>',methods=['GET','POST'])
def editstudent(id):
    student=Student.query.get_or_404(id)
    classess=Class.query.all()
    form=StudentForm()
    if form.validate_on_submit():
        student.name=form.name.data
        student.fathername=form.fathername.data
        student.nic=form.nic.data
        student.age=form.age.data
        student.fees=form.fees.data
        
        flash(f'Student Successfully Updated','success')
        db.session.commit()
        return redirect(url_for('showstudents',student_id=student.id))
    elif request.method=='GET':
        form.name.data=student.name
        form.fathername.data=student.fathername
        form.nic.data=student.nic
        form.age.data=student.age
        form.fees.data=student.fees
    return render_template('editstudent.html',form=form ,classess=classess,title="edit Student")

#edit Subject
@app.route('/editsubject/<int:id>',methods=['GET','POST'])
def editsubject(id):
    subject=Subject.query.get_or_404(id)
    form=SubjectForm()
    if form.validate_on_submit():
        subject.name=form.name.data
        subject.number=form.number.data
        flash(f'Subject Successfully Updated','success')
        db.session.commit()
        return redirect(url_for('showsubjects',subject_id=subject.id))
    elif request.method=='GET':
        form.name.data=subject.name
        form.number.data=subject.number
    return render_template('editsubject.html',form=form,title="edit Subject" )
#edit tools
@app.route('/edittools/<int:id>',methods=['GET','POST'])
def edittools(id):
    tools=Tool.query.all()
    tool=Tools.query.get_or_404(id)
    form=ToolsForm()
    if form.validate_on_submit():
        tool.number=form.number.data
        tool.money=form.money.data
        flash(f'Tool Successfully Updated','success')
        db.session.commit()
        return redirect(url_for('showtools',tool_id=tool.id))
    elif request.method=='GET':
        form.number.data=tool.number
        form.money.data=tool.money
    return render_template('edittools.html',form=form,tools=tools,title="edit Tools" )
#edit Few TOols
@app.route('/editfewtools/<int:id>',methods=['GET','POST'])
def editfewtools(id):
    tools=Tool.query.all()
    tool=FewTools.query.get_or_404(id)
    form=FewToolsForm()
    if form.validate_on_submit():
        tool.number=form.number.data
        tool.money=form.money.data
        flash(f'Tool Successfully Updated','success')
        db.session.commit()
        return redirect(url_for('showfewtools',tool_id=tool.id))
    elif request.method=='GET':
        form.number.data=tool.number
        form.money.data=tool.money
    return render_template('editfewtools.html',form=form,tools=tools,title="edit FewTools" )

#delete Employee
@app.route('/deleteemployee/<int:id>',methods=['GET','POST'])
def deleteemployee(id):
    employee=Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    flash('Employee Successfully Deleted','success')
    return redirect(url_for('showemployees'))
#delete Class
@app.route('/deleteclass/<int:id>',methods=['GET','POST'])
def deleteclass(id):
    clas=Class.query.get_or_404(id)
    db.session.delete(clas)
    db.session.commit()
    flash('Class Successfully Deleted','success')
    return redirect(url_for('showclassess'))
#delete LImit
@app.route('/deletelimit/<int:id>',methods=['GET','POST'])
def deletelimit(id):
    limit=Limit.query.get_or_404(id)
    db.session.delete(limit)
    db.session.commit()
    flash('limit Successfully Deleted','success')
    return redirect(url_for('addlimit'))


#delete position
@app.route('/deleteposition/<int:id>',methods=['GET','POST'])
def deleteposition(id):
    position=Position.query.get_or_404(id)
    db.session.delete(position)
    db.session.commit()
    flash('Position Successfully Deleted','success')
    return redirect(url_for('showpositions'))

# delete Student
@app.route('/deletestudent/<int:id>',methods=['GET','POST'])
def deletestudent(id):
    student=Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Student Successfully Deleted','success')
    return redirect(url_for('showstudents'))
#delete Subject
@app.route('/deletesubject/<int:id>',methods=['GET','POST'])
def deletesubject(id):
    subject=Subject.query.get_or_404(id)
    db.session.delete(subject)
    db.session.commit()
    flash('Subject Successfully Deleted','success')
    return redirect(url_for('showsubjects'))
#delete tools
@app.route('/deletetools/<int:id>',methods=['GET','POST'])
def deletetools(id):
    tools=Tools.query.get_or_404(id)
    db.session.delete(tools)
    db.session.commit()
    flash('Tool Successfully Deleted','success')
    return redirect(url_for('showtools'))

#delete Few Tools
@app.route('/deletefewtools/<int:id>',methods=['GET','POST'])
def deletefewtools(id):
    tools=FewTools.query.get_or_404(id)
    db.session.delete(tools)
    db.session.commit()
    flash('Tool Successfully Deleted','success')
    return redirect(url_for('showfewtools'))


#delete tool
@app.route('/deletetool/<int:id>',methods=['GET','POST'])
def deletetool(id):
    tool=Tool.query.get_or_404(id)
    db.session.delete(tool)
    db.session.commit()
    flash('Tool Successfully Deleted','success')
    return redirect(url_for('showtool'))

