G54CCS Labs -- Exercise 2
=========================

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
