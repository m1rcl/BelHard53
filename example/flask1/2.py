from flask import Flask, render_template, url_for, redirect
import os

BASE_FOLDER = os.getcwd()
print(BASE_FOLDER)

app = Flask(__name__, 
            static_folder=os.path.join(BASE_FOLDER, "static"), 
            template_folder=os.path.join(BASE_FOLDER, "templates"))



ADMIN = True

@app.route('/')
def index():
    return 'Hello world!!!'


@app.route('/test1/')
def test1():    
    return '<h2>Test1</h2>'


@app.route('/test2/')
def test2():    
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

# Сработает если ошибка 404 - т.е. любой другой путь который выше не предусмотрен
@app.errorhandler(404)
def page_not_found(error):
    return render_template('err.html')



app.run(port=5500, debug=True)


