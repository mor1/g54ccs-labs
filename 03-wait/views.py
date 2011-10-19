import logging
from google.appengine.ext import webapp

import random, time ## to sleep for a random interval

## parameterised HTML
HTML = """\
<!DOCTYPE html>
<html>
  <head>
    <title>A Delaying Hello World! page</title>
    <meta charset='utf-8'>
  </head>
  
  <body>
    Hello World! (after waiting %d seconds)
  </body>
</html>"""
        
class WaitRandom(webapp.RequestHandler):
    def get(self):
        logging.info("request: %s" % (self.request,))

        ## generate a random integer in the range [0,10]
        delay = random.randint(0, 10)
        logging.info("delay: %d" % (delay,))

        ## sleep for the delay
        time.sleep(delay)

        ## return a page to the user, filling in the delay
        self.response.out.write(HTML % (delay,))

class WaitParam(webapp.RequestHandler):
    def get(self):
        logging.info("request: %s" % (self.request,))

        ## extract the delay parameter and convert to an integer
        delay = int(self.request.get('delay'))
        logging.info("delay: %d" % (delay,))

        ## sleep and return as in WaitRandom:get()
        time.sleep(delay)
        self.response.out.write(HTML % (delay,))
        
class WaitUrl(webapp.RequestHandler):

    ## note that the delay parameter below is constructed by the URL
    ## handler
    def get(self, delay):
        logging.info("request: %s" % (self.request,))

        ## convert the delay parameter to an integer
        delay = int(delay)
        logging.info("delay: %d" % (delay,))

        ## sleep and return as in WaitRandom:get()
        time.sleep(delay)
        self.response.out.write(HTML % (delay,))

## EX. try invoking one of the handlers multiple times simultaneously
## with different delay parameters - what happens?  what happens if
## you do so against a deployed instance?  why?

