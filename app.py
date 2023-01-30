from datetime import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = SQL("sqlite:///data.db")

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/Employee",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("Employee.html")
    else:
        email=request.form.get("email")
        password=request.form.get("pass")
        # db.execute("INSERT INTO employee (email,password) VALUES(?,?)", email, password)
        return redirect("/given_task")

@app.route("/manager",methods=["GET","POST"])
def managerlogin():
    if request.method == "GET":
        return render_template("manager.html")
    else:
        return redirect("/task")

@app.route("/task",methods=["GET","POST"])
def task():
    if request.method == "GET":
        employees=db.execute("SELECT name FROM employee")
        return render_template("task.html",employees=employees)
    else:
        name=request.form.get("employee")
        task=request.form.get("task")
        deadline=request.form.get("date")
        db.execute("INSERT INTO task (employee_name,task_assigned,deadline) VALUES(?,?,?)", name,task, deadline)
        return redirect("/check")

@app.route("/check",methods=["GET"])
def check():
    check=db.execute("SELECT employee_name,task_assigned,assigned_at,deadline,completed_at FROM task")
    return render_template("check.html",check=check)

@app.route("/Employee_register",methods=["GET","POST"])
def Employee_register():
    if request.method == "GET":
        return render_template("Employee_register.html")
    else:
        email=request.form.get("email")
        password=request.form.get("pass")
        name=request.form.get("bus")

        db.execute("INSERT INTO employee (email_id,password,name) VALUES(?,?,?)", email, password, name)
        return redirect("/Employee")

@app.route("/given_task",methods=["GET","POST"])
def given_task():

    if request.method == "GET":
        tasks=db.execute("SELECT task_assigned,assigned_at,deadline,completed,id FROM task WHERE completed='False'")
        return render_template("given_task.html",tasks=tasks)
    else:
        check = request.form.get("check")
        if(check == "on"):
            tasks=db.execute("SELECT task_assigned,assigned_at,deadline,completed,id FROM task")
            db.execute("UPDATE task SET completed='True',completed_at=? WHERE id=?",datetime.now(),tasks[0]["id"])
            return redirect("/given_task")


if __name__ == '__main__':
    app.run(debug=True)