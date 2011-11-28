import logging, datetime, hashlib, os

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

import models

def render(page, context):
    return template.render(os.path.join("templates", page), context)

def create_ticket():
    count = db.GqlQuery("SELECT * FROM Ticket").count()
    now = datetime.datetime.now().isoformat()    
    return hashlib.sha1("%s:%s" % (count, now)).hexdigest()

class Value(webapp.RequestHandler):
    def get(self, ticket=None):        
        logging.info("ticket:%s" % ticket)
        if ticket:
            ticket = models.Ticket.all().filter("value =", ticket).get()
            
        now = datetime.datetime.now().isoformat()
        
        counter = None
        counters = []
        if ticket: counter = models.Counter.all().filter("ticket =", ticket).get()
        else:
            counters = models.Counter.all().fetch(10)
        
        context = { 'now': now,
                    'ticket': ticket,
                    'counter': counter,
                    'counters': counters,
                    }
        if counter: counter.put()
        for c in counters: c.put()
        self.response.out.write(render("page.html", context))

class Incr(webapp.RequestHandler):
    def post(self, ticket=None):
        logging.info("ticket:%s ticket?%s" % (ticket, True if ticket else False))
        now = datetime.datetime.now().isoformat()

        if ticket:
            ticket = models.Ticket.all().filter("value =", ticket).get()
        
        if not ticket:
            ticket = models.Ticket(value=create_ticket())
            ticket.put()
            
        counter = models.Counter.all().filter("ticket =", ticket).get()
        if not counter: counter = models.Counter(ticket=ticket)
        else:
            counter.value += 1

        context = { 'now': now,
                    'ticket': ticket,
                    'counter': counter,
                    }        
        counter.put()

        self.redirect("/value/%s" % ticket.value)
