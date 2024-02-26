from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text

def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = username
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username, password, is_admin):
    hash_value = generate_password_hash(password)

    sql = text("INSERT INTO users (username,password,joined_at) VALUES (:username,:password,NOW())")
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()

    if is_admin:
        sql = text("INSERT INTO admins (username) VALUES (:username)")
        db.session.execute(sql, {"username":username})
        db.session.commit()
    return login(username, password)

def user_id():
    return session.get("user_id",0)

def user_is_admin():
    try:
        username = session.get("username",0)
        sql = text("SELECT count(*) FROM admins WHERE username=:username")
        result = db.session.execute(sql, {"username":username})
        if result.fetchone()[0] > 0:
            return True
        else:
            return False
    except:
        return False