from flask import Flask

html_start = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ТЕСТ Flask</title>   
    <style>  body{background-color:hotpink;} </style>
</head>
<body>
'''


html_test2 = '''
    <p>
        192.168.0.1, 192.168.1.1 - как правило адреса домашних сетей        
        127.0.0.1 - localhost - локальный адрес - внутренний адрес устройства
    </p>
    <img src="https://random-d.uk/api/7.gif" alt="dsdsd">
    
'''


html_end = '''
</body>
</html>
'''


app = Flask(__name__)


# стработает если пришел щапрос на главную страницу
# http://127.0.0.1:5500
@app.route('/')
def index():
    return 'Hello world!!!'

# http://127.0.0.1:5500/test1/
@app.route('/test1/')
def test1():    
    return '<h2>Test1</h2>'

# http://127.0.0.1:5500/test2/5/
@app.route('/test2/<int:count>/')
def test2(count):    
    text = ''
    for  i in range(count):
        text += '<h1>Test1</h1>'
    return html_start + html_test2 + text + html_end


# http://127.0.0.1:5500/test3/vasia/
@app.route('/test3/<name>/')
def test3(name):    
    text = f'<h1> привет {name} </h1>'
    
    return html_start + text + html_end


# Сработает если ошибка 404 - т.е. любой другой путь который выше не предусмотрен
@app.errorhandler(404)
def page_not_found(error):
    return '<h1 style="color:red">такой страницы не существует</h1>'



app.run(port=5500, debug=True)


