from app import app
from flask import render_template, request, redirect
import users, conversations

@app.route("/")
def index():
    list = conversations.get_list()
    return render_template("index.html", conversations=list)

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    title = request.form["title"]
    if conversations.send(title, content):
        return redirect("/")
    else:
        # todo error handling
        return render_template("/")
    
@app.route("/sendmessage/<int:id>", methods=["POST"])
def send_message(id):
    content = request.form["content"]
    if conversations.send_message(id, content):
        return redirect("/conversations/" + str(id))
    else:
        # todo error handling
        return render_template("/")
    
@app.route("/conversations/<int:id>")
def conversation(id):
    current_conversation = conversations.get_first_post_by_id(id)
    messages = conversations.get_messages_by_id(id)
    return render_template("conversation.html", conversation=current_conversation, messages=messages)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("login.html", message="invalid credientials")
        
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        if users.register(username, password1):
            return redirect("/")
        else:
            # todo error handling
            return render_template("/")