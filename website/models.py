from website import db
from flask_login import UserMixin

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instructions = db.Column(db.String(1000))
    ingredients = db.Column(db.String(1000))
    title = db.Column(db.String(30))
    category = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref=db.backref('my_recipes', lazy=True))
    user = db.relationship('User', backref='recipes')


    def __repr__(self):
        return f"Recipe('{self.title}', '{self.category}', '{self.ingredients}', '{self.instructions}')"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
