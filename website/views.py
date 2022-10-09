from flask import Blueprint, render_template
from flask_login import login_required, current_user
import randfacts

views = Blueprint('views', __name__)


@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user, username=current_user.username)


@views.route('/')
def index():
    fact = randfacts.getFact()
    return render_template("index.html", fact=fact)
