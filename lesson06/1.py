"""
Добавить в проект прошлого задания шаблоны. 

На главной странице сделать ссылки на каждый ендпоинт

На каждой неглавной странице сделать кнопку-ссылку - возврат на главную страницу

Добавить страницу с картинкой и счетчиком кликов по ней. 
    На главной странице  добавить ссылку  на нее 

На главной странице добавить ссылку на страницу с погодой 5 разных городов, 
    которая будет отображаться если запрос пришел на сервер в четную минуту 
    текущего времени. 
    т.е. 10:52 - ссылка отображается на главной странице, 10:51 - нет
    если пользователь сам вбивает адрес этой страницы - тоже делать проверку
    

"""


from flask import Flask, render_template, url_for, redirect
import os
import requests

BASE_FOLDER = os.getcwd()

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_FOLDER, "static"),
    template_folder=os.path.join(BASE_FOLDER, "templates"),
)


@app.route("/")
def index():
    return render_template("main.html")


@app.route("/duck/")
def duck():
    url = "https://random-d.uk/api/v2"
    res = requests.get(f"{url}/random").json()
    rand_duck_url = res["url"]
    return render_template("duck.html", url=rand_duck_url)


@app.route("/fox/<int:count>/")
def fox(count):
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


@app.route("/weather-minsk/")
def weather_minsk():
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


@app.route("/weather/<city>/")
def weather_city(city):
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


# жуткий костыль
@app.route("/clicker/")
def clicker():
    global clicks
    clicks += 1
    return render_template("clicker.html", clicks=clicks)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("err.html")


clicks = -1
app.run(port=7777)
