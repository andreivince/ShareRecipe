from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        if len(email) < 4:
            flash("Email Incorrect", category="error")
            pass
        elif len(firstName) < 2:
            flash("Name must be greater than 2 characters", category="error")
            pass
        elif password1 != password2:
            flash("Passwords don\'t match", category="error")
            pass
        elif len(password1) < 7:
            flash("Passwords must be at least 7 characters", category="error")
            pass
        else:
            flash("Account created", category="success")
            pass
    
    return render_template("sign_up.html")

# Views of the bar
# line 8 is collecting data
#Message flashing import flash