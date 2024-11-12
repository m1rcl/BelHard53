"""
добавить в прошлый проект ссылку на страницу с текущим дз
на этой страницы создать тэги header main floor.
в main сделать несколько section каждый со своим заданием.
Задания на картинках в этой папке. 
В 4 и 5 задании таблицы можно пока сделать черно-белыми. 
URL картинки для 6 задания: https://img.freepik.com/premium-vector/map-treasures-paper-parchment_8071-3421.jpg
"""

from datetime import datetime
from flask import Flask, render_template, redirect, session, request
from flask_sqlalchemy import SQLAlchemy
import os
import re
import requests

BASE_FOLDER = os.getcwd()

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_FOLDER, "static"),
    template_folder=os.path.join(BASE_FOLDER, "templates"),
)
app.config["SECRET_KEY"] = "my_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False)
    login = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    age = db.Column(db.Integer(), nullable=False)


with app.app_context():
    db.create_all()


def name_valid(name, errs):
    if re.search(r"[а-яА-ЯёЁ\s]", name):
        errs.append("")
        return True
    else:
        errs.append("Имя и фамилия должны содержать только русские буквы")
        return False


def user_login_exist(login):
    with app.app_context():
        user_exist = User.query.filter_by(login=login).first()
        if user_exist:
            return user_exist
        else:
            return None


def login_valid(login, errs):
    if user_login_exist(login):
        errs.append("Пользователь с таким логином уже существует")
        return False
    if re.search(r"[a-zA-Z0-9_]{6,20}", login):
        errs.append("")
        return True
    else:
        errs.append(
            "Логин должен содержать латинские буквы, цифры, _ и быть длиной от 6 до 20 символов"
        )
        return False


def password_valid(password, errs):
    if re.search(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,15}", password):
        errs.append("")
        return True
    else:
        errs.append(
            "Пароль должен содержать хотя бы 1 строчную букву, 1 заглавную букву и 1 цифру и быть длиной от 8 до 15 символов"
        )
        return False


def email_valid(email, errs):
    with app.app_context():
        user_password_exist = User.query.filter_by(email=email).first()
        if user_password_exist:
            errs.append("Пользователь с таким e-mail уже существует")
            return False
    if re.search(r"^\S+@\S+\.\S+$", email):
        errs.append("")
        return True
    else:
        errs.append("Введенный e-mail не соответствует формату электронной почты")
        return False


def age_valid(age, errs):
    try:
        if 11 < int(age) < 101:
            errs.append("")
            return True
        else:
            errs.append("Возраст должен быть от 12 до 100 включительно")
            return False
    except:
        errs.append("Возраст должен быть от 12 до 100 включительно")
        return False


def add_user(username, login, password, email, age):
    with app.app_context():
        new_user = User(
            username=username, login=login, password=password, email=email, age=age
        )
        db.session.add(new_user)
        db.session.commit()


@app.route("/")
def index():
    even_minutes_server = datetime.now().minute % 2 == 0
    return render_template("main.html", even_minutes_server=even_minutes_server)


@app.route("/registration/", methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        errors_reg = ["", "", "", "", ""]
        return render_template("registration.html", messages=errors_reg)
    if request.method == "POST":
        username = request.form.get("name")
        login = request.form.get("login")
        password = request.form.get("password")
        email = request.form.get("email")
        age = request.form.get("age")
        errors_reg = []

        name_valid(username, errors_reg)
        login_valid(login, errors_reg)
        password_valid(password, errors_reg)
        email_valid(email, errors_reg)
        age_valid(age, errors_reg)
        print(errors_reg)

        if errors_reg == ["", "", "", "", ""]:
            print(username, login, password, email, age)
            add_user(username, login, password, email, age)
            return redirect("/")
        else:
            return render_template(
                "registration.html",
                user_name=username,
                user_login=login,
                user_email=email,
                user_age=age,
                messages=errors_reg,
            )


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        errors_login = ["", ""]
        return render_template("login.html", messages=errors_login)
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")
        errors_login = []
        user_exist = user_login_exist(login)
        if user_exist:
            if user_exist.password == password:
                session["user_id"] = user_exist.id
                session["username"] = user_exist.username
                session["clicks"] = 0
                return redirect("/")
            else:
                errors_login.append("")
                errors_login.append("Неверный пароль")
                return render_template(
                    "login.html", messages=errors_login, user_login=login
                )
        else:
            errors_login.append("Неверный логин")
            return render_template(
                "login.html", messages=errors_login, user_login=login
            )


@app.route("/logout/")
def logout():
    session.pop("user_id")
    session.pop("username")
    return redirect("/")


@app.route("/duck/")
def duck():
    if "user_id" in session:
        url = "https://random-d.uk/api/v2"
        res = requests.get(f"{url}/random").json()
        rand_duck_url = res["url"]
        return render_template("duck.html", url=rand_duck_url)
    else:
        return redirect("/registration/")


@app.route("/fox/<int:count>/")
def fox(count):
    if "user_id" in session:
        if 0 < count < 11:
            foxes_urls_list = []
            for _ in range(count):
                url = "https://randomfox.ca/floof/"
                res = requests.get(url).json()
                rand_fox_url = res["image"]
                foxes_urls_list.append(rand_fox_url)
            return render_template("fox.html", urls=foxes_urls_list)
        else:
            return "<h1>указано неверное количество, укажите число от 1 до 10 включительно</h1>"
    else:
        return redirect("/registration/")


@app.route("/weather-minsk/")
def weather_minsk():
    if "user_id" in session:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": "Minsk",
            "units": "metric",
            "lang": "ru",
            "APPID": "7505a3a45c2f09d2e4009d8887ceb17f",
        }
        res = requests.get(url, params).json()

        return render_template(
            "weather.html",
            city="Minsk",
            conditions=res["weather"][0]["description"],
            temp=res["main"]["temp"],
            feels_like=res["main"]["feels_like"],
        )
    else:
        return redirect("/registration/")


@app.route("/weather/<city>/")
def weather_city(city):
    if "user_id" in session:
        try:
            url = "https://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": f"{city}",
                "units": "metric",
                "lang": "ru",
                "APPID": "7505a3a45c2f09d2e4009d8887ceb17f",
            }
            res = requests.get(url, params).json()

            return render_template(
                "weather.html",
                city=city.capitalize(),
                conditions=res["weather"][0]["description"],
                temp=res["main"]["temp"],
                feels_like=res["main"]["feels_like"],
            )
        except:
            return "<h1>введенный город не найден</h1>"
    else:
        return redirect("/registration/")


@app.route("/weather-5city/")
def weater_five():
    if "user_id" in session:
        even_minutes_server = datetime.now().minute % 2 == 0
        if even_minutes_server:
            weather_city_list = []
            url = "https://api.openweathermap.org/data/2.5/weather"
            city_list = ["Brest", "Vitebsk", "Gomel", "Grodno", "Mogilev"]
            for _ in city_list:
                params = {
                    "q": _,
                    "units": "metric",
                    "lang": "ru",
                    "APPID": "7505a3a45c2f09d2e4009d8887ceb17f",
                }
                res = requests.get(url, params).json()
                weather_city_list.append(
                    {
                        "city": _,
                        "conditions": res["weather"][0]["description"],
                        "temp": res["main"]["temp"],
                        "feels_like": res["main"]["feels_like"],
                    }
                )
        else:
            return redirect("/")
        return render_template(
            "weather-5city.html",
            even_minutes_server=even_minutes_server,
            weather_city_list=weather_city_list,
        )
    else:
        return redirect("/registration/")


@app.route("/clicker/")
def clicker():
    if "user_id" in session:
        return render_template("clicker.html", clicks=session["clicks"])
    else:
        return redirect("/registration/")


@app.route("/fake-clicker/")
def fake_clicker():
    if "user_id" in session:
        session["clicks"] += 1
        return redirect("/clicker/")
    else:
        return redirect("/registration/")


@app.route("/samples/")
def samples():
    return render_template("samples.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("err.html")


app.run(port=7777, debug=True)
