## standard GAE libraries
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

## enable writing to console for development environment, or to the
## log in a live application
import logging

## the (constant) page we will return, as a string
HTML = """\
<!DOCTYPE html>
<html>
  <head>
    <title>Yet Another Hello World! page</title>
    <meta charset='utf-8'>
  </head>
  
  <body>
    Hello World!
  </body>
</html>"""
        
## the handler object referred to in urls.py
class HelloWorld(webapp.RequestHandler):

    ## we only handle the HTTP GET method
    def get(self):

        ## log the request
        logging.info("request: %s" % (self.request,))

        ## send the response to the client
        self.response.out.write(HTML)

        ## ...and that's it!


## another URL handler that handles GETs but is deliberately broken.
class Broken(webapp.RequestHandler):

    ## this will raise a NameError when invoked, as BARF is undefined.
    def get(self):
        BARF

## list the supported URL entry-points.  these are given as a list of
## pairs (string, object-ref).  the string is formatted as a regular
## expression.  the object-ref is the name of a class that will be
## used to handle access to the specified URL.  we have just two for
## now: /hello and /broken
urls = [
    (r'/hello', views.HelloWorld),
    (r'/broken', views.Broken),
    ]
## EX. try accessing /hello/ - what happens?  why?  how might you
## allow /hello/ to work in addition to /hello?

## create the application instance that will handle a user request.
application = webapp.WSGIApplication(urls, debug=True)
## EX.  access /broken from your browser.  what do you see?  now
## change "debug=False" above, and try again.  what do you see?  why
## and when might you choose to use debug=True vs. debug=False?

## allow GAE to run our application when our URLs are hit.

## NB.  the next three lines are a Python idiom: there is *nothing*
## significant about the name of main(), unlike in C and similar
## languages.
def main():
    run_wsgi_app(application) 
if __name__ == "__main__": main()
