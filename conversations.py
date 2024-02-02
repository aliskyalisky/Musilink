from db import db
from sqlalchemy.sql import text
import users

def get_list():
    sql = text("SELECT C.title, C.content, U.username, C.created_at, C.id FROM conversations C, users U WHERE C.user_id=U.id ORDER BY C.id")
    result = db.session.execute(sql)
    return result.fetchall()

def get_first_post_by_id(id):
    sql = text("SELECT C.title, C.content, U.username, C.created_at, C.id FROM conversations C, users U WHERE C.id=:id AND C.user_id=U.id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()

def get_messages_by_id(id):
    sql = text("SELECT DISTINCT M.content, U.username, M.sent_at, M.id, U.id FROM conversations C, users U, messages M WHERE M.conversation_id=:id AND M.user_id=U.id ORDER BY M.id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def send_message(id, content):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO messages (content, user_id, sent_at, conversation_id) VALUES (:content, :user_id, NOW(), :conversation_id)")
    db.session.execute(sql, {"content":content, "user_id":user_id, "conversation_id":id})
    db.session.commit()
    return True

def send(title, content):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO conversations (title, content, user_id, created_at) VALUES (:title, :content, :user_id, NOW())")
    db.session.execute(sql, {"title":title, "content":content, "user_id":user_id})
    db.session.commit()
    return True