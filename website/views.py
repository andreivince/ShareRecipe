from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Recipe, User
from website import db


views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    recipes = Recipe.query.all()

    return render_template("home.html", user=current_user, recipes=recipes)

@views.route("/recipe/<int:recipe_id>")
@login_required
def recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template("recipe.html", user=recipe.user, recipe=recipe)
