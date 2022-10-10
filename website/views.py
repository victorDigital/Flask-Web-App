import markdown
import requests
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_required, current_user
import markdown.extensions.fenced_code
import randfacts


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/home')
def index():
    fact = randfacts.getFact()
    return render_template("index.html", fact=fact)


@views.route('/about')
def about():
    return render_template("about.html")


@views.route('/contact')
def contact():
    return render_template("contact.html")


@views.route('/projects')
@login_required
def projects():
    link1 = 'https://raw.githubusercontent.com/victorDigital/p5weather/main/README.md'
    md1 = markdown.Markdown()
    readme_file1 = requests.get(link1)
    html1 = md1.convert(readme_file1.text)
    link2 = 'https://raw.githubusercontent.com/victorDigital/lectioToGoogleCalendar/main/README_SHORT.md'
    md2 = markdown.Markdown()
    readme_file2 = requests.get(link2)
    html2 = md2.convert(readme_file2.text)
    link3 = 'https://raw.githubusercontent.com/victorDigital/Flask-Web-App/main/README.md'
    md3 = markdown.Markdown()
    readme_file3 = requests.get(link3)
    html3 = md3.convert(readme_file3.text)
    return render_template("projects.html", user=current_user, html1=html1, html2=html2, html3=html3)
