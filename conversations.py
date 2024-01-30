from db import db
from sqlalchemy.sql import text
import users

def get_list():
    sql = text("SELECT C.title, C.content, U.username, C.created_at FROM conversations C, users U WHERE C.user_id=U.id ORDER BY C.id")
    result = db.session.execute(sql)
    return result.fetchall()

def send(title, content):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO conversations (title, content, user_id, created_at) VALUES (:title, :content, :user_id, NOW())")
    db.session.execute(sql, {"title":title, "content":content, "user_id":user_id})
    db.session.commit()
    return True