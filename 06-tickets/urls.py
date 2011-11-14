from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import views

urls = [
    (r'/value/?', views.Value),
    (r'/value/(?P<ticket>[a-fA-F0-9]+)/?', views.Value),

    (r'/incr/?', views.Incr),
    (r'/incr/(?P<ticket>[a-fA-F0-9]+)/?', views.Incr),
    ]

application = webapp.WSGIApplication(urls, debug=True)
def main(): run_wsgi_app(application)
if __name__ == "__main__": main()
