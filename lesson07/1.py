"""
Создать в прошлом проекте страницу с формой регистрации и страницу с формой входа на сайт
регистрация должна содержать имя фамилию возраст email логин пароль.
Форму делаем максимально простой без CSS.
После отправки формы регистрации проверить данные на валидность
    - имя фамилия - только русские буквы
    - логин - латинские цифры и _. От 6 до 20 символов
    - пароль - обязательно хотя бы 1 латинская маленькая, 1 заглавная и  1 цифр. От 8 до 15 символов.
    - email - должен быть валидным
    - возраст - целое число от 12 до 100


после регистрации добавить пользователя в базу/файл/список/словарь

при входе пользователя 
    - проверить есть ли такой пользователь 
    - пометить в сессиях что он залогинился
    - перенаправить на главную страницу

Все прежние страницы сделать открытыми только для пользователей которые произвели вход на сайт.
Если пользователь не залогинился и переходит на них - перенаправлять его на форму входа. 
На фоме входа сделать ссылку на форму регистрации.

Если пользовался залогинился - на каждой странице сверху писать - "Приветствуем вас имя фамилия"

На главной странице показывать ссылку ВХОД и РЕГИСТРАЦИЯ для пользователей которые не вошли на сайт
и ссылку ВЫХОД для  пользователей которые вошли на сайт

Таким образом новый пользователь имеет доступ  только на главную страницу где есть ссылка на вход регистрацию.
После регистрации и входа он имеет доступ на все доступные страницы.

"""

from flask import Flask, render_template, url_for, redirect, session, request
from datetime import datetime
import os
import requests

BASE_FOLDER = os.getcwd()
clicks = 0
users_list = []
USER = {}
login = False

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_FOLDER, "static"),
    template_folder=os.path.join(BASE_FOLDER, "templates"),
)
app.config["SECRET_KEY"] = "my_secret_key"


def name_valid(name):
    return True


def login_valid(login):
    return True


def password_valid(password):
    return True


def email_valid(email):
    return True


def age_valid(age):
    return True


@app.route("/")
def index():
    even_minutes_server = datetime.now().minute % 2 == 0
    return render_template("main.html", even_minutes_server=even_minutes_server)


@app.route("/registration/", methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        return render_template("registration.html")
    if request.method == "POST":
        user_name = request.form.get("name")
        user_login = request.form.get("login")
        user_password = request.form.get("password")
        user_email = request.form.get("email")
        user_age = request.form.get("age")
        if all(
            [
                name_valid(user_name),
                login_valid(user_login),
                password_valid(user_password),
                email_valid(user_email),
                age_valid(user_age),
            ]
        ):
            if user_login not in [
                awailable_user["login"] for awailable_user in users_list
            ]:
                users_list.append(
                    {
                        "name": user_name,
                        "login": user_login,
                        "password": user_password,
                        "email": user_email,
                        "age": user_age,
                    }
                )
                print(users_list)
                login = True
                return redirect("/")
            else:
                pass


@app.route("/duck/")
def duck():
    if login:
        url = "https://random-d.uk/api/v2"
        res = requests.get(f"{url}/random").json()
        rand_duck_url = res["url"]
        return render_template("duck.html", url=rand_duck_url)
    else:
        return redirect("/registration/")


@app.route("/fox/<int:count>/")
def fox(count):
    if login:
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
    if login == True:
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
    if login == True:
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
    if login == True:
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
    if login == True:
        return render_template("clicker.html", clicks=clicks)
    else:
        return redirect("/registration/")


@app.route("/fake-clicker/")
def fake_clicker():
    if login == True:
        global clicks
        clicks += 1
        return redirect("/clicker/")
    else:
        return redirect("/registration/")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("err.html")


app.run(port=7777)
