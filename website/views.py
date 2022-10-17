import markdown
import requests
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_required, current_user
import markdown.extensions.fenced_code
import randfacts
import requests
from bs4 import BeautifulSoup


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/about')
def index():
    fact = randfacts.getFact()
    print(fact)
    return render_template("about.html", fact=fact)


@views.route('/contact')
def contact():
    return render_template("contact.html")


@views.route('/projects')
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
    link4 = 'https://raw.githubusercontent.com/victorDigital/dictionary-api-python/main/README.md'
    md4 = markdown.Markdown()
    readme_file4 = requests.get(link4)
    html4 = md4.convert(readme_file4.text)
    return render_template("projects.html", html1=html1, html2=html2, html3=html3, html4=html4)


@views.route('/projects/dictionary', methods=['GET', 'POST'])
@login_required
def dictionary():
    if request.method == 'POST':
        try:
            query = request.form.get('word')
            link = f"https://ordnet.dk/ddo/ordbog?query={query}"
            r = requests.get(link)
            soup = BeautifulSoup(r.text, "html.parser")
            deffRaw = soup.find_all("span", class_="definition")
            deffPure = [i.text for i in deffRaw]
            wordRaw = soup.find_all("span", class_="match")
            wordPure = wordRaw[0].text
            word = {"word": wordPure, "deff": deffPure}
            print(word)
        except Exception as e:
            print(e)
            flash("No word found", category='error')
            return redirect(url_for('views.dictionary'))
        if word == {}:
            flash('Word not found', category='error')
        else:
            return render_template("dictionary.html", user=current_user, word=word)
    else:
        return render_template("dictionary.html", user=current_user)
