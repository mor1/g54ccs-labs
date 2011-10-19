from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import views

urls = [
    (r'/calc-parameters/?', views.CalcParameters),
    (r'/calc-url/(?P<op>add|subtract)/(?P<x>\d+)/(?P<y>\d+)/?', views.CalcUrl), 
    ]

application = webapp.WSGIApplication(urls, debug=True)
def main(): run_wsgi_app(application) 
if __name__ == "__main__": main()

