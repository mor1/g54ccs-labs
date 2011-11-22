import sys, logging, datetime, time
log = logging.info
err = logging.exception

from google.appengine.ext import db

class SYNC_STATUS:
    unsynchronized = 'UNSYNCHRONIZED'
    inprogress = 'INPROGRESS'
    synchronized = 'SYNCHRONIZED'

class SyncStatus(db.Model):
    status = db.StringProperty(
        default=SYNC_STATUS.unsynchronized, required=True)
    last_sync = db.DateTimeProperty()

    def put(self):
        if self.status == SYNC_STATUS.synchronized:
            self.last_sync = datetime.datetime.now()
        super(SyncStatus, self).put()

class Tweet(db.Model):
    raw = db.TextProperty(required=True)
    txt = db.TextProperty(required=True)
