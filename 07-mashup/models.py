import sys, logging, datetime, time
log = logging.info
err = logging.exception

from django.utils import simplejson as json
from google.appengine.ext import db

def datetime_as_float(dt):
    '''Convert a datetime.datetime into a microsecond-precision float.'''
    return time.mktime(dt.timetuple())+(dt.microsecond/1e6)

class SYNC_STATUS:
    unsynchronized = 'UNSYNCHRONIZED'
    inprogress = 'INPROGRESS'
    synchronized = 'SYNCHRONIZED'

class SyncStatus(db.Model):
    status = db.StringProperty(
        default=SYNC_STATUS.unsynchronized, required=True)
    last_sync = db.DateTimeProperty()

    def todict(self):
        last_sync = datetime_as_float(self.last_sync) if self.last_sync else None
        return { 'status': self.status,
                 'last_sync': last_sync,
                 }

    def tojson(self):
        return json.dumps(self.todict(), indent=2)

    def put(self):
        if self.status == SYNC_STATUS.synchronized:
            self.last_sync = datetime.datetime.now()
        super(SyncStatus, self).put()

class Tweet(db.Model):
    raw = db.TextProperty(required=True)
    txt = db.TextProperty(required=True)
