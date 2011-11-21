from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import views

urls = [
    (r'/$', views.Root),
    (r'/cron/?$', views.Cron),
    (r'/sync(?:/(?P<cmd>start|stop))?/?$', views.Sync),
    (r'/tweets/?$', views.Tweets),
    ]
    
application = webapp.WSGIApplication(urls, debug=True)
def main(): run_wsgi_app(application) 
if __name__ == "__main__": main()
