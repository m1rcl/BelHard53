"""
Повторить проект с приложением QUIZ (папка flask2)
Добавить возможность:    
    - просматривать все квизы и вопросы
    - добавлять квизы и вопросы  
    - редактировать квизы и вопросы
    - удалять квизы и вопросы
    - изменять связи вопросов с квизами




"""

from flask import Flask, redirect, render_template, request, session, url_for, jsonify
import os
from models import db, User, Question, Quiz, db_add_new_data
import sys
from random import shuffle

BASE_DIR = os.getcwd()
DB_PATH = os.path.join(BASE_DIR, "db", "db_quiz.db")

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SECRET_KEY"] = "secretkeysecretkeysecretkey1212121"
app.config["JSON_AS_ASCII"] = False
db.init_app(app)

html_config = {"admin": True, "debug": False}

with app.app_context():
    db_add_new_data()


@app.route("/", methods=["GET"])
def index():
    return render_template("base.html", html_config=html_config)


@app.route("/quiz/", methods=["POST", "GET"])
def view_quiz():
    if request.method == "GET":
        session["quiz_id"] = -1
        quizes = Quiz.query.all()
        return render_template("start.html", quizes=quizes, html_config=html_config)

    session["quiz_id"] = request.form.get("quiz")
    session["question_n"] = 0
    session["question_id"] = 0
    session["right_answers"] = 0
    return redirect(url_for("view_question"))


@app.route("/question/", methods=["POST", "GET"])
def view_question():
    if not session["quiz_id"] or session["quiz_id"] == -1:
        return redirect(url_for("view_quiz"))

    if request.method == "POST":
        question = Question.query.filter_by(id=session["question_id"]).one()
        if question.answer == request.form.get("ans_text"):
            session["right_answers"] += 1
        session["question_n"] += 1

    quiz = Quiz.query.filter_by(id=session["quiz_id"]).one()

    if int(session["question_n"]) >= len(quiz.question):
        session["quiz_id"] = -1
        return redirect(url_for("view_result"))
    else:
        question = quiz.question[session["question_n"]]
        session["question_id"] = question.id
        answers = [question.answer, question.wrong1, question.wrong2, question.wrong3]
        shuffle(answers)
        return render_template(
            "question.html", answers=answers, question=question, html_config=html_config
        )


@app.route("/result/")
def view_result():
    return render_template(
        "result.html",
        right=session["right_answers"],
        total=session["question_n"],
        html_config=html_config,
    )


@app.route("/quizes_view/", methods=["POST", "GET"])
def view_quiz_edit():
    if request.method == "POST":
        pass

    quizes = Quiz.query.all()
    questions = Question.query.all()

    return render_template(
        "quizes_view.html",
        html_config=html_config,
        quizes=quizes,
        questions=questions,
        len=len,
    )


@app.route("/quiz_edit/<int:index>/", methods=["POST", "GET"])
def quiz_edit(index):
    if request.method == "POST":
        pass

    quiz = Quiz.query.filter_by(id=index).one()
    current_questions = quiz.question
    other_questions = [
        question
        for question in Question.query.all()
        if question not in current_questions
    ]

    return render_template(
        "quiz_edit.html",
        html_config=html_config,
        quiz_name=quiz.name,
        current_questions=current_questions,
        other_questions=other_questions,
        index=index,
        len=len,
    )


@app.errorhandler(404)
def page_not_found(e):
    return '<h1 style="color:red; text-align:center; margin-top:100px"> Упс..... </h1>'


app.run(debug=True, port=7777)
