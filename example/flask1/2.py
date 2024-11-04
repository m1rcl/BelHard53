from flask import Flask, render_template, url_for, redirect, session, request
import os

BASE_FOLDER = os.getcwd()
print(BASE_FOLDER)

app = Flask(__name__, 
            static_folder=os.path.join(BASE_FOLDER, "static"), 
            template_folder=os.path.join(BASE_FOLDER, "templates"))


# Секретный ключ для сессий
app.config['SECRET_KEY'] = "my secret key - ds;ldks;ldks;ldks"


# модель MVC
    # model
    # view
    # controller



ADMIN = True

@app.route('/')
def index():
    session['click_count'] = 0 
    return 'Hello world!!!'


@app.route('/test1/')
def test1():    
    if session['login'] == True:        
        return '<h2>Test1</h2>'
    redirect('/login/')


@app.route('/test2/')
def test2():    
    session['click_count'] += 1 
    users = ['user1', 'user2', 'user3', 'user4']
    return render_template("2.html", admin = ADMIN, users = users)


@app.route('/edit/')
def edit():
    if ADMIN:    
        return "edit"
    return redirect(url_for('view'))


@app.route('/view/')
def view():    
    return "view"

@app.route('/form1/', methods=['GET', 'POST'])
def form1():    
    
    
    # если GET - т.е. запрос пришел из браузера обычным способом
    if request.method =='GET':
        return render_template('form1.html')
    
    
    # иначе если POST - т.е. запрос прешел как отправка данных форсы
    name = request.form.get('name')
    surname = request.form.get('surname')
    pas = request.form.get('pass')
    print('-'*20, name, surname, pas)
    if pas == "111":
        return redirect('/edit/') # если пароль правильный перенаправляем на соотв.страницу
    
    # иначе формируем ошибку и заново рисуем форму
    return render_template('form1.html', err="Пароль неверный", val=surname)

    # поля формы можно можно представить подобной схемой и 
    # затем проверять универсальной функцией 
    # fields = {
    #     'name':{'ru':'имя', 'data':'', 'type':'str', 'max':25,  'min':3},
    #     'age':{'ru':'возраст', 'data':'', 'type':'int', 'max':16,  'min':6}
    # }
    # err = check_fields(fields, request) - вернет список ошибок 
    # функцию check_fields - пишем сами


# Сработает если ошибка 404 - т.е. любой другой путь который выше не предусмотрен
@app.errorhandler(404)
def page_not_found(error):
    return render_template('err.html')



app.run(port=5500, debug=True)


