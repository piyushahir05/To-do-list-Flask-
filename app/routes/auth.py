from flask import Flask,Blueprint,render_template,request,redirect,url_for,flash,session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from app import db
from app.models import User

auth_bp=Blueprint('auth',__name__)


@auth_bp.route('/login',methods=["GET","POST"])
def login():

    if request.method == "POST":
        username=request.form.get('username')
        password=request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password,password):
            session['user_id'] = user.id
            session['user'] = user.username
            flash('Login successful','success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash('Invalid credentials','danger')
           
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user',None)
    session.pop('user_id',None)
    flash('Logged out','info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/register',methods=["GET","POST"])
def register():
    if request.method=="POST":
        username = request.form.get('username')
        password = request.form.get('password')

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists','danger')
            return redirect(url_for('auth.register'))
    
        hashed_password = generate_password_hash(password)

        new_user = User(username=username,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')