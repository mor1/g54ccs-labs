from google.appengine.ext import db

class Ticket(db.Model):
    value = db.StringProperty()
    ctime = db.DateTimeProperty(auto_now_add=True)

    def put(self):
        n = db.GqlQuery("SELECT * FROM Ticket WHERE value=:v",
                        v=self.value).count()
        if n > 0:
            raise ValueError("collision! n=%d v=%s" % (n, self.value,))
        super(Ticket, self).put()

class Counter(db.Model):
    ctime = db.DateTimeProperty(auto_now_add=True)
    atime = db.DateTimeProperty(auto_now=True)
    value = db.IntegerProperty(default=0, required=True)
    ticket = db.ReferenceProperty(
        Ticket, collection_name="counters", required=True)
