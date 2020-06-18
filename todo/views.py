from todo import app, db, bcrypt
from flask import render_template, redirect, request, url_for, Response, flash, jsonify
from todo.models import Todo, User
from flask_login import login_user, logout_user, current_user, login_required

@app.route("/")
@app.route("/todo", methods=["GET","POST"])
@login_required
def home():
    todo_items = Todo.query.filter_by(author=current_user)
    
    if request.method == 'POST':
        if request.form.get('btn_identifier') == 'addTodo':
            added_item = request.form.get('todoItem')
            if added_item != '':
                item = Todo(todo_item=added_item, user_id=current_user.id)
                db.session.add(item)
                db.session.commit()
                return redirect(url_for('home'))
            else:
                flash('no item written')
        elif request.form.get('btn_identifier') == 'delete all':
            try:
                # delete_item = Todo.query.first()
                # db.session.delete(delete_item)
                del_items = Todo.query.filter_by(user_id = current_user.id).all()
                for item in del_items:
                    db.session.delete(item)
                    db.session.commit()
                return redirect(url_for('home'))
            except:
                flash('no items to delete')

    return render_template('todo.html', todo_items=todo_items)

@app.route("/todo/delete", methods={"POST","GET"})
@login_required
def delete_item():
    if request.method == 'POST':
        to_delete_item = request.data
        item = Todo.query.filter_by(user_id=current_user.id, todo_item=str(to_delete_item, 'utf-8')).first()
        db.session.delete(item)
        db.session.commit()
    return 'item deleted'


@app.route("/todo/completed", methods={"POST","GET"})
@login_required
def completed_item():
    if request.method == 'POST':
        if request.is_json:
            completed_todo_item = request.get_json()
            is_completed = {'is_completed': item.completed }
            return jsonify(is_completed)
        else:
            return 'qwe'

    
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            encrypted_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(username=username, password=encrypted_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            flash('fill both fields')

    return render_template('register.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password')
                
    return render_template('login.html')


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

