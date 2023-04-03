from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Recipe



views = Blueprint('views', __name__)

@views.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipe.html', recipe=recipe)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

# Views of the homepage