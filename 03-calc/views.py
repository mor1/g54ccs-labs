import logging
from google.appengine.ext import webapp

HTML = """\
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>A Basic Calculator</title>
    <meta charset='utf-8'>
  </head>
  
  <body>
    %s
  </body>
</html>"""
        
class CalcParameters(webapp.RequestHandler):
    def get(self):
        logging.info("request: %s" % (self.request,))

        x = int(self.request.get('x'))
        y = int(self.request.get('y'))
        op = self.request.get("op")
        
        logging.info("x:%d y:%d op:%s" % (x, y, op,))

        if op.lower() == "add":
            r = "PARAMETERS: %d + %d = %d" % (x, y, x+y)
        elif op.lower() == "subtract":
            r = "PARAMETERS: %d - %d = %d" % (x, y, x-y)
        else:
            r = "PARAMETERS: unknown operation %s" % (op,)

        self.response.out.write(HTML % r)

class CalcUrl(webapp.RequestHandler):
    def get(self, op, x, y):
        logging.info("request: %s" % (self.request,))

        x = int(x)
        y = int(y)
        
        logging.info("x:%d y:%d op:%s" % (x, y, op,))

        if op.lower() == "add":
            r = "URL: %d + %d = %d" % (x, y, x+y)
        elif op.lower() == "subtract":
            r = "URL: %d - %d = %d" % (x, y, x-y)
        else:
            r = "URL: unknown operation %s" % (op,)

        self.response.out.write(HTML % r)
