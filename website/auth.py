from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Recipe
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages



auth = Blueprint('auth', __name__)

@auth.route('/create', methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        name_recipe = request.form.get("name")
        new_recipe = Recipe(name=name_recipe, user_id=current_user.id)
        db.session.add(new_recipe)
        db.session.commit()
        return redirect(url_for('views.home'))

    return render_template("create.html", user=current_user, Recipe=new_recipe)


@auth.route('/about')
def about():
    return render_template("about.html", user=current_user) 
   

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Try again!", category="error")
        else:
            flash("Email doesn't exist!!", category="error")
    return render_template("login.html", user=current_user)

            
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exist!!", category="error")
        

        
        if len(email) < 4:
            flash("Email Incorrect", category="error")
        elif len(first_name) < 2:
            flash("Name must be greater than 2 characters", category="error")
        elif password1 != password2:
            flash("Passwords don\'t match", category="error")
        elif len(password1) < 7:
            flash("Passwords must be at least 7 characters", category="error")
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created", category="success")
            return redirect(url_for('views.home'))
            
    
    return render_template("sign_up.html", user=current_user)

# Views of the bar
# line 8 is collecting data
#Message flashing import flash