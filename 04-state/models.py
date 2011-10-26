from google.appengine.ext import db

class Counter(db.Model):
    ctime = db.DateTimeProperty(auto_now_add=True)
    atime = db.DateTimeProperty(auto_now=True)
    value = db.IntegerProperty(default=0, required=True)
