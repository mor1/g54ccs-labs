## a new GAE library, supporting access to Google's BigTable storage.
from google.appengine.ext import db

## the Counter class, which GAE maps into a table.  in this case each
## row in the table contains three columns:
## -- ctime, a timestamp denoting when the row was created
## -- atime, a timestamp denoting when the row was last accessed
## -- value, the actual value of the counter

class Counter(db.Model):
    ctime = db.DateTimeProperty(auto_now_add=True)
    atime = db.DateTimeProperty(auto_now=True)
    value = db.IntegerProperty(default=0, required=True)

## EX. read the GAE documentation and find out what auto_now and
## auto_now_add mean for DateTimeProperty fields.
