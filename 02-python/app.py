from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import logging, random

HTML = """\
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Some Python</title>
    <meta charset='utf-8'>
  </head>
  
  <body>
    %s
  </body>
</html>"""
        
class Invoke(webapp.RequestHandler):
    def get(self):
        logging.info("request: %s" % (self.request,))
        
        x = random.randint(0, 16)
        y = random.randint(16, 20)

        z = x/y
        f = float(x)/y

        result = "<p>x=%d y=%d z=%d f=%0.3f</p>" % (x, y, z, f)

        s = "x"*10 + "y" + ":z"*5
        ss = s.split(":")
        result += "<p>%s -> '%s'</p>" % (s, ss)
        
        lst = [x, y]
        lst.append(x)
        result = "%s<p>lst='%s'</p>" % (result, lst)
        result += "<p>elements:"
        for e in lst: result += "%d," % e
        result += "</p>"
        
        d = { "0-10": x,
              "10-20": y,
              "zero": z,
              "string": s,
              }
        result += "<p>%s</p>" % d
        for k in d:
            result += "<p>key='%s' value='%s'</p>" % (k, d[k])
        
        self.response.out.write(HTML % result)

urls = [
    (r'/invoke', Invoke),
    ]

application = webapp.WSGIApplication(urls, debug=True)
def main():
    run_wsgi_app(application) 
if __name__ == "__main__":
    main()
