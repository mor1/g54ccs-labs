import logging, time, os.path

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

import models

def now():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

def t(p):
    return os.path.join("templates", p)

class Value(webapp.RequestHandler):
    def get(self):
        counter = models.Counter.all().get()
        context = { 'now': now(),
                    'counter': counter,
                    }
        if counter: counter.put()

        self.response.out.write(template.render(t("page.html"), context))

class Incr(webapp.RequestHandler):
    def post(self):
        counter = models.Counter.all().get()
        if not counter: counter = models.Counter()
        else:
            counter.value += 1

        context = { 'now': now(),
                    'counter': counter,
                    }
        counter.put()

        self.response.out.write(template.render(t("page.html"), context))

