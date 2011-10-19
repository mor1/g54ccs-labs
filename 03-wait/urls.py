from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import views

urls = [
    ## wait a random delay before returning
    (r'/wait-random/?', views.WaitRandom),

    ## NB. in regular expressions, x? means zero or one x, ie,. x is
    ## optional
    
    ## wait a requested delay before returning, as a parameter, ie.,
    ## "/wait-param/?delay=2"
    (r'/wait-param/?', views.WaitParam),

    ## wait a requested delay before returning, from the URL.
    (r'/wait-url/(?P<delay>\d+)/?', views.WaitUrl),

    ## NB.  decoding the regular expression above we have: the
    ## constant string "/wait-url/", followed by "(?P<delay>...)"
    ## which takes the result of ... and puts it in a variable named
    ## "delay". here ... is "\d+", a sequence of one or more decimal
    ## digits, and finally, following the delay parameter, an optional
    ## "/"

    ## EX.  adjust the regular expression above to make the delay
    ## parameter optional.  don't forget to set a default value in
    ## views.py:WaitUrl:get() though!
    ]

application = webapp.WSGIApplication(urls, debug=True)
def main(): run_wsgi_app(application) 
if __name__ == "__main__": main()

