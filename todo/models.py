from datetime import datetime
from todo import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    todo_posts = db.relationship('Todo', backref='author', lazy=True)
    
    def __repr__(self):
        return f'({self.username})'


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    todo_item = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"{self.todo_item}"

