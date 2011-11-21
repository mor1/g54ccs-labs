import logging, urllib, urlparse
log = logging.info

from google.appengine.ext import webapp
from google.appengine.api import urlfetch, users
from google.appengine.api.labs import taskqueue
from django.utils import simplejson as json

import models

COUNT = 80
HASHTAG = '#cloud'

class Root(webapp.RequestHandler):
    def get(self):
        tweets = [
            json.loads(t.raw) for t in models.Tweet.all().order('__key__') ]

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(tweets))

class Cron(webapp.RequestHandler):
    def get(self):
        taskqueue.add(url="/sync/start", method="POST")

class Sync(webapp.RequestHandler):
    def get(self, cmd):
        ss = models.SyncStatus.get_by_key_name("twitter-status")
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(ss.tojson())

    def post(self, cmd):
        if cmd == "start":
            s = models.SyncStatus.get_or_insert("twitter-status")
            if s.status != models.SYNC_STATUS.inprogress:
                taskqueue.add(url="/tweets/", method="GET")
                s.status = models.SYNC_STATUS.inprogress
                
            s.put()

        elif cmd == "stop":
            s = models.SyncStatus.get()
            if s.status == models.SYNC_STATUS.inprogress:
                s.status = models.SYNC_STATUS.unsynchronized
                s.put()

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(s.tojson())

class Tweets(webapp.RequestHandler):
    def get(self):
        log("request:%s" % (self.request,))
        ps = { 'q': HASHTAG, 'rpp': COUNT, }
        max_id = self.request.GET.get("max_id")
        if max_id: ps['max_id'] = max_id

        page = self.request.GET.get("page")
        if page: ps['page'] = page
        
        url = "http://search.twitter.com/search.json?%s" % (
            urllib.urlencode(ps),)
        log("url:%s" % url)
        res = urlfetch.fetch(url)
        log("res:%s\nhdr:%s" % (res.content, res.headers))
        js = json.loads(res.content)

        if 'error' in js: ## retry after specified time
            retry = int(res.headers.get('retry-after', '300'))
            rurl = "%s?%s" % (self.request.path, self.request.query_string)
            log("retry: url:%s countdown:%d" % (rurl, retry+2,))
            taskqueue.add(url=rurl, countdown=retry+2, method="GET")

        else:
            if 'results' in js:
                for tw in js['results']:
                    t = models.Tweet.get_or_insert(
                        tw['id_str'], raw=json.dumps(tw), txt=tw['text'])
                    t.put()

            if 'next_page' in js:
                next_page = "%s%s" % (self.request.path_url, js['next_page'],)
                urlo = urlparse.urlsplit(next_page)
                next_page_rel = urlparse.urlunsplit(
                    ("", "", urlo.path, urlo.query, urlo.fragment))
                taskqueue.add(url=next_page_rel, method="GET")

            else:
                s = models.SyncStatus.get_by_key_name("twitter-status")
                s.status = models.SYNC_STATUS.synchronized
                s.put()
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(js, indent=2))
