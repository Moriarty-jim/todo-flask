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
        todo_item = request.form['todo-text']
        if todo_item:
            item = Todo(user_id=current_user.id, todo_item=todo_item)
            db.session.add(item)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            flash('Empty input, Enter todo', 'warning')

    return render_template('todo.html', todo_items=todo_items)

# @app.route("/todo/add", methods={"POST","GET"})
# @login_required
# def add_item():
#     if request.method == 'POST':
#         if request.get_json:
#             try:
#                 response = request.get_json()
#                 item_to_add = response['todo_item']
#                 item = Todo(user_id=current_user.id, todo_item=item_to_add)
#                 db.session.add(item)
#                 db.session.commit()
#                 return jsonify({'item':item_to_add})
#             except:
#                 flash('error')
        
    

@app.route("/todo/delete", methods={"POST","GET"})
@login_required
def delete_item():
    if request.method == 'POST':
        if request.is_json:
            try:
                response = request.get_json()
                to_delete_post_id = response['todo_post_id']
                item = Todo.query.filter_by(user_id=current_user.id, id=to_delete_post_id).first()
                db.session.delete(item)
                db.session.commit()
                # flash('deleted', 'success')
                return str(item.id)
            except:
                return str(current_user.id)

        


@app.route("/todo/completed", methods={"POST","GET"})
@login_required
def completed_item():
    if request.method == 'POST':
        if request.is_json:
            try:
                response = request.get_json()
                is_completed = response['is_completed']
                todo_id = response['todo_id']
                item = Todo.query.filter_by(user_id=current_user.id, id=todo_id).first()
                try:
                    if is_completed:
                        item.completed = True
                        db.session.commit()

                    else:
                        item.completed = False
                        db.session.commit()
                        
                    return jsonify({'is_completed':item.completed})
                except:
                    return 'fail'
            except:
                    return 'fail2'      

# @app.route("/register/somefunction", methods=["POST"])
# def somefunction():
#     if request.method == "POST":
#         if request.is_json:
#             response = request.get_json()
#             text = response['text']
#             return jsonify({'text':text})
#         else:
#             return 'not json'
#         return 'post'
#     else:
#         return 'not post'

    
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            if username and password:
                encrypted_password = bcrypt.generate_password_hash(password).decode('utf-8')
                user = User(username=username, password=encrypted_password)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))
            else:
                flash('fill both fields')
        except:
            flash('username already taken', 'fail')
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
            flash('Login Unsuccessful. Please check email and password', 'fail')
                
    return render_template('login.html')


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


