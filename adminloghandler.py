from db import db
from flask import session
from sqlalchemy.sql import text

def get_events():
    sql = text("SELECT content, event_time FROM eventlog GROUP BY content, event_time")
    result = db.session.execute(sql)
    return result.fetchall()

def insert_event(content):
    sql = text("INSERT INTO eventlog (content,event_time) VALUES (:content,NOW())")
    db.session.execute(sql, {"content":content})
    db.session.commit()