from flask import Flask,Blueprint,render_template,request,url_for,session,flash,redirect
from app import db
from app.models import Task

tasks_bp=Blueprint('tasks',__name__)

@tasks_bp.route('/')
def view_tasks():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    tasks = Task.query.filter_by(user_id=session['user_id']).all()
    total = len(tasks)
   
    progress_score=0
    for task in tasks:
        if task.status == "Working":
            progress_score+=0.3
        elif task.status == "Done":
            progress_score+=1.0
    
    progress = int((progress_score / total) * 100) if total > 0 else 0
    last_progress = session.get('current_progress', 0)
    session['current_progress'] = progress



    return render_template('tasks.html',tasks=tasks,
        progress=progress,total=total,last_progress=last_progress)

@tasks_bp.route('/add',methods=["POST"])
def add_task():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    

    title=request.form.get('title')
    if title:
        new_task=Task(title=title,status="Pending",user_id=session['user_id'])
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully','success')

    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>',methods=["POST"])
def toggle_status(task_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    task=Task.query.get(task_id)
    if task and task.user_id==session['user_id']:
        if task.status=='Pending':
            task.status = 'Working'
        elif task.status == 'Working':
            task.status ='Done'
        else:
            task.status ='Pending'

        db.session.commit()
    return redirect(url_for('tasks.view_tasks') + f"#task-{task.id}")



@tasks_bp.route('/clear',methods=["POST"])
def clear_tasks():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    Task.query.filter_by(user_id=session['user_id']).delete()
    db.session.commit()
    flash('All tasks cleared!','info')
    return redirect(url_for('tasks.view_tasks'))