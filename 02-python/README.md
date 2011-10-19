G54CCS Labs, Exercise 2
=======================

In this exercise you will extend your Google App Engine (GAE)
application to introduce some more simple Python syntax.

First we see, as with the previous exercise, some _module imports_.
These allow you to access extra functionality than is provided by the
core Python language, which is quite simple and can only do relatively
very basic operations.

```python
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import logging, random
```

In this case, we import two GAE specific modules, and then we import
the standard `logging` and `random` modules to enable simple logging
of output and generation of random numbers.

Next we have the HTML boilerplate for the page we will return:
```python

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
```
This is a `string`, that is, `HTML` is a _variable_ -- a label
representing some contents which can change -- that currently contains
data which represents some text.  Note the `%s` toward the end -- this
will allow us to insert extra contents into the HTML boilerplate at
that point. 

Next we have the definition of the class and its method used to handle
incoming `GET` requests to the `/invoke` URL, followed by the simple
logging statement as in the first exercise.  Classes and methods are more
advanced programming concepts which we will not discuss further here.
```python        
class Invoke(webapp.RequestHandler):
    def get(self):
        logging.info("request: %s" % (self.request,))
```

Then we have the following block of code:
```python
        x = random.randint(0, 16)
        y = random.randint(16, 30)

        z = x/y
        f = float(x)/y

        result = "<p>x=%d y=%d z=%d f=%0.3f</p>" % (x, y, z, f)
```
Taking each line in turn, this does the following:
+ Generates a random _integer_ between 0 and 10, and assigns it to the
  variable `x`; 
+ Generates a random integer between 10 and 20, and assigns it to the 
  variable `y`;
+ Computes `x` divided by `y` and assigns the result to the variable
  `z`; 
+ Converts the integer `x` to a _floating point value_ and divides it
  by `y` and assigns the result to the variable `f`; and finally
+ Constructs a string, `result`, by a process which Python calls
  _string interpolation_, which contains the values of the _tuple_
  `x`, `y`, `z`, and `f` within an HTML paragraph (delimited by
  `<p>`...`</p>`). 

Look closely at the difference between `z` and `f`: `z` is always 0
because you cannot represent fractional (or irrational) numbers as a
variable of integer type.  By converting `x` to a floating point value
first, we allow non-integer values to be represented in the
computation `float(x)/y` and so `z` is also a floating point value.

Also, look closely at the string interpolation: the substrings
beginning `%` between the quotes "..." are _format specifiers_ --
placeholders which are filled in with strings representing the values
given in the tuple.  The particular format specifiers used here are
`%d` which produces the string representing an integer as a decimal;
and `%0.3f` which takes a _f_loating point value and represents it as
a decimal string to 3 decimal places.  

__Exercise__: Try changing the `%d`s to `%x`s and see what happens.
Try some format specifiers from
<http://docs.python.org/release/2.6.7/library/stdtypes.html#string-formatting-operations>. 





--

some imports

a constant HTML string for interpolation/result - note the %s

some integers and string interpolation of those ints

note the 1/3 = 0 -- need to use floats not ints

string addition, mulitplication -- python has quite powerful string manip. techniques

lists - you saw tuples with ints (...) -- singleton tuple vs scalar --
lists similar but mutable -- can append/extend

dictionary/map -- maps keys to values -- multiple types permittable
(tech note: keys must be "hashable") -- tuples, lists, dictionaries
are iterable ie., can do for...in... on them
...


consider adding the following function at line xxx

def p(s):
    return "<p>%s</p>" % s

...use this to simplify code/increase readability/reduce repetition


[[

next ex:

string split etc

calculator eg

params into app 

]]
