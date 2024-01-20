from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User

@app.route('/')
def dashboard():
    return render_template('index1.html', users_list=User.get_all())

@app.route('/new_user')
def new_user():
    return render_template("index2.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    User.create(request.form)
    return redirect('/')

@app.route('/edit/<int:id>')
def update_user(id):
     return render_template("edit.html", user = User.save_one(id))

@app.route('/save', methods=["POST"])
def save_user():
    User.update(request.form)
    return redirect("/")

@app.route('/show/<int:id>')
def show_user(id):
    return render_template("show.html", user = User.get_one(id))

@app.route('/delete/<int:id>')
def delete(id):
    User.delete(id)
    return redirect('/')