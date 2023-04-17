# Import the necessary modules
from website import db
from flask_login import UserMixin

# Define a Recipe class, representing a recipe with a title, category, ingredients, instructions, and author
class Recipe(db.Model):
    # Define the columns of the Recipe table
    id = db.Column(db.Integer, primary_key=True)  # unique identifier for the recipe
    instructions = db.Column(db.String(1000))    # instructions for cooking the recipe
    ingredients = db.Column(db.String(1000))     # ingredients required for the recipe
    title = db.Column(db.String(30))             # title of the recipe
    category = db.Column(db.String(30))          # category of the recipe
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # foreign key to the User table
    author = db.relationship('User', backref=db.backref('my_recipes', lazy=True)) # relationship with the User class
    user = db.relationship('User', backref='recipes') # relationship with the User class

    # Define the string representation of a Recipe object
    def __repr__(self):
        return f"Recipe('{self.title}', '{self.category}', '{self.ingredients}', '{self.instructions}')"

# Define a User class, representing a user with an email, password, and first name
class User(db.Model, UserMixin):
    # Define the columns of the User table
    id = db.Column(db.Integer, primary_key=True)   # unique identifier for the user
    email = db.Column(db.String(150), unique=True) # email address of the user
    password = db.Column(db.String(150))           # password of the user
    first_name = db.Column(db.String(150))         # first name of the user
