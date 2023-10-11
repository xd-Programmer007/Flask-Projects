from flask import Flask,flash,render_template,send_file,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message
from werkzeug.utils import secure_filename
from datetime import datetime
import json
import os
import math

with open('config.json','r') as f:
    params = json.load(f)['params']


app = Flask(__name__)

app.secret_key = "AnythingButSecret"
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-password']
)

mail = Mail(app)
app.config['SQLALCHEMY_DATABASE_URI'] = params['uri']
app.config['UPLOAD_FOLDER'] = params['upload_location']
db = SQLAlchemy(app)

class Contacts(db.Model):
    '''
        sno, name ,phone_num , mes, date, email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    mes = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(12), nullable=True)

class Projects(db.Model):
    '''
        sno, name ,phone_num , mes, date, email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    img_file = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(12), nullable=True)



@app.route('/')
def home():
    return render_template('index.html', params=params)

@app.route('/submit/<string:type>' , methods =['GET','POST'])
def submit(type):
    if request.method == 'POST':
        if(type == 'contact'):
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            message = request.form.get('message')
            entry = Contacts(name=name, email=email, phone_num=phone, mes=message, date=datetime.now())
            body = f'Hi Adarsh its me {name}\n and I wanted to say {message} you can contact me on {phone} \n'
            msg = Message(subject=message[0:13],
                          sender=email,
                          recipients=[params['gmail-user']],
                            body=body)
            mail.send(msg)
            db.session.add(entry)
            db.session.commit()
            #mail is left
            
        else:
            pass
        return redirect('/')


@app.route('/resume')
def resume():
    pdf_path = 'static/file/Adarsh_Resume.pdf'
    return send_file(pdf_path,as_attachment=True)

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        print(name,' ',password," ",params['admin_user']," ",params['admin_password'])

        if name == params['admin_user'] and password == params['admin_password']:
            print('Entered here')
            session['user'] = name
            return redirect('/dashboard')
        return "<h1> Wrong Username or password </h1>"
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user' in session and session['user'] == params['admin_user']:
        projects = Projects.query.all()
        return render_template('dashboard.html',projects=projects)
    return render_template('login.html')


@app.route('/uploader',methods=['POST','GET'])
def uploader():
    if not ('user' in session and session['user'] == params['admin_user']):
        return redirect('/dashboard')
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
    print('adarsh-tiwari')
    return "<h1>file uploaded </h1>"


@app.route('/delete/<string:sno>', methods = ['GET','POST'])
def delete(sno):
    if( 'user' in session and session['user'] == params['admin_user']):
        project = Projects.query.filter_by(sno=sno).first()
        db.session.delete(project)
        db.session.commit()
        return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')

@app.route('/edit/<string:sno>', methods = ['GET','POST'])
def edit(sno):
    if( 'user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()
            if sno == "0":
                project = Projects(title=box_title,content=content,img_file=img_file,date=date)
                db.session.add(project)
                db.session.commit()
            else :
                post = Projects.query.filter_by(sno=sno).first()
                post.title = box_title
                post.content = content
                post.date = date
                post.img_file = img_file
                db.session.commit()
                return redirect('/edit/'+sno)
        project = Projects.query.filter_by(sno=sno).first()
        return render_template('edit.html',params=params,project=project,sno=sno)


@app.route('/projects',methods=['GET'])
def projects():
    project = Projects.query.filter_by().all()
    per_page = int(params['no_of_projects'])
    page = request.args.get('page')
    last = math.ceil(len(project)/per_page)
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    val = (page-1)*per_page
    project = project[val:val+per_page]
    if page == 1:
        prev = "#"
        if(last == 1):
            next = "#"
        else:
            next = "/projects?page="+str(page+1)
    elif page == last:
        prev = "/projects?page="+str(page-1)
        next = "#"
    else:
        prev = "/projects?page="+str(page-1)
        next = "/projects?page="+str(page+1)
    
    return render_template('projects.html',params=params,projects=project,next=next,prev=prev)



app.run(debug=True)
