import logging, time

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

import models

class Value(webapp.RequestHandler):
    def get(self):
        ## get a string representing the current time
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

        ## get the counter from the Counter table
        counter = models.Counter.all().get()

        ## create the context dictionary for rendering the page
        context = { 'now': now,
                    'counter': counter,
                    }

        ## put the counter back in the store, forcing the atime to be
        ## updated via auto_add
        if counter: counter.put()

        ## write the HTML page back to the client
        self.response.out.write(template.render("page.html", context))

class Incr(webapp.RequestHandler):
    def post(self):
        ## again, get the current time
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

        ## get the current counter value
        counter = models.Counter.all().get()
        if not counter:
            ## if there isn't one, create it
            counter = models.Counter()
        else:
            ## if there is one, increment its value by one
            counter.value += 1

        context = { 'now': now,
                    'counter': counter,
                    }
        
        ## put the counter back in the store
        counter.put()

        ## write the HTML back
        self.response.out.write(template.render("page.html", context))

## EX. view the admin console at <http://localhost:8080/_ah/admin> -
## how many rows are in your table?
      
## EX. extend this application to allow you to increment by an
## arbitrary value.

