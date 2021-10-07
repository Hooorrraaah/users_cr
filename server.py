from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/users')

@app.route('/users')
def create_user():
    return render_template("users.html",users=User.get_all())

@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create',methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')

@app.route("/delete/<int:id>")
def delete(id):
    data = {
    "id":id
    }
    User.delete_user(data)
    return redirect ("/")

@app.route("/edit/<int:id>")
def get_user(id):
    data = {
    "id":id
    }
    user = User.get_user(data)
    return render_template("edit_user.html", user=user)

@app.route('/edituser/<int:id>',methods=['POST'])
def update_user_db(id):
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id":id
    }
    User.update_user(data)
    return redirect('/users')

@app.route("/show/<int:id>")
def show_user(id):
    data = {
    "id":id
    }
    user = User.show_user(data)
    return render_template("examine.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)

