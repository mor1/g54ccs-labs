G54CCS Labs, Exercise 2
=======================

In this exercise you will extend your Google App Engine (GAE)
application to introduce some more simple Python syntax.

Imports
-------

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

Constant String
---------------

Next we have the HTML boilerplate for the page we will return:

    HTML = """ 
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

This is a `string`, that is, `HTML` is a _variable_ -- a label
representing some contents which can change -- that currently contains
data which represents some text.  Note the `%s` toward the end -- this
will allow us to insert extra contents into the HTML boilerplate at
that point.  String in Python can be enclosed in single (') or double
(") quotes, but not a mixture.  Using triple single- or double-quotes
is a verbatim string, i.e., one which includes all whitespace,
newlines and so on until the appropriate closing triple. 

Boilerplate
-----------

Next we have the definition of the class and its method used to handle
incoming `GET` requests to the `/invoke` URL, followed by the simple
logging statement as in the first exercise.  Classes and methods are more
advanced programming concepts which we will not discuss further here.

```python        

    class Invoke(webapp.RequestHandler):
        def get(self):
            logging.info("request: %s" % (self.request,))
```

...followed by the meat of the programme, followed by the closing
boilerplate:


```python        
        
            self.response.out.write(HTML % result)

    urls = [
        (r'/invoke', Invoke),
        ]

    application = webapp.WSGIApplication(urls, debug=True)
    def main():
        run_wsgi_app(application) 
    if __name__ == "__main__":
        main()
```

We will now consider the meat of the programme between these two
blocks.

Function calls, Integers, Floats, Arithmetic, String interpolation
------------------------------------------------------------------

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

_Function calls_ in Python mean putting the name of the module from
which the function comes if required (`random` in this case), followed
by the separator (`.`) and then the name of the function (`randint`)
followed by parentheses containing any parameters to the function
(`(0, 16)` and `(16, 30)` in this case).

Look closely at the difference between `z` and `f`: `z` is always 0
because you cannot represent fractional (or irrational) numbers as a
variable of integer type.  By converting `x` to a floating point value
first, we allow non-integer values to be represented in the
computation `float(x)/y` and so `f` is also a floating point value.

The basic arithmetic operations are `+`, `-`, `*` (multiply) and `/`
(divide).  Since performing an operation on a variable and storing the
result back in the same variable is such a common operation, Python
provides shortcuts for this: `+=`, `+-`, etc.  For example, `x += 1`
is identical to `x = x+1`, i.e., it computes `x+1` and stores the
result back into `x`.  To test for equality, use `==` -- `=` is used
only to assign a value to a variable.

Also, look closely at the string interpolation: the substrings
beginning `%` between the quotes "..." are _format specifiers_ --
placeholders which are filled in with strings representing the values
given in the tuple.  The particular format specifiers used here are
`%d` which produces the string representing an integer as a decimal;
and `%0.3f` which takes a _f_loating point value and represents it as
a decimal string to 3 decimal places.  

Strings
-------

```python

            s = "x"*10 + "y" + ":z"*5
            ss = s.split(":")
            result += "<p>%s -> '%s'</p>" % (s, ss)
```

Python has a wide range of string manipulation functions and methods.
This demonstrates some simple ones: 

+ Multiplying a string by a number repeats the string the specified
  number of times;
+ Adding two strings together concatenates them; and
+ Invoking a string's `split` method creates a list of strings by
  dividing the original string where it contains any character in the
  parameter (in this case, splits the string `s` on every `:` character).
  
Lists
-----

```python

            lst = [x, y]
            lst.append(x)
            result = "%s<p>lst='%s'</p>" % (result, lst)
            result += "<p>elements:"
            for e in lst: result += "%d," % e
            result += "</p>"
```

You have already seen _tuples_ -- sequences of variables enclosed in
parentheses `(`...`)` -- which are _immutable_, i.e., they cannot be
changed after being defined.  The equivalent
_mutable_ type is the _list_, a sequence enclosed in square brackets
`[`...`]`.  Lists support a number of operations to sort, separate,
append, extend and so on.

Note one common problem with tuples is the following: _how do you
represent a tuple with just a single element_?  The obvious way to do
this -- `(x)` -- is unfortunately wrong: it is parsed as the
arithmetic expression returning `x`, i.e., `(x) == x`.  If you need to
represent a tuple with a single element, simply insert a trailing
comma, i.e., `(x,)`.

Dictionaries
------------

```python

            d = { "0-10": x,
                  "10-20": y,
                  "zero": z,
                  "string": s,
                  }
            result += "<p>%s</p>" % d
```

_Dictionaries_ known as _maps_ associate _values_ with _keys_.  That
is, you insert a value associate with a key, and you can then
subsequently get the value back out if you have the right key.  (By
analogy with a dictionary where, if you know the word, you can
retrieve the associated definition.)

In Python, dictionaries are very flexible and widely used.  A single
dictionary can simultaneously contain keys and values of many
different types.  The main restriction is that keys must be
_hashable_, but all the basic types meet this restriction so we will
not discuss it further here.

Iteration
---------

```python

            for k in d:
                result += "<p>key='%s' value='%s'</p>" % (k, d[k])
```

Several types in Python are _iterable_, that is, you can _iterate_
over them.  Iteration refers to the process of consider each element
of a variable in turn.  So, for example, if you wish to consider every
element of a list, you _iterate_ through the list.  The Python syntax
for this is very simple: 

`for <`variable`> in <`iterable`>: do-stuff-with-variable`.  

Iteration across a list or tuple considers
each element in order; iteration across a dictionary considers each
key in an arbitrary order (in fact, in the order defined by the hash
value of the key). 

In the example above, we iterate through the dictionary `d` referring
to each key as `k`.  For each key, we concatenate a paragraph
containing the key and the corresponding value to the result string. 

Closing Boilerplate
-------------------


Exercises
---------

__Ex.1__: Try changing the `%d`s to `%x`s and see what happens.  Try
some format specifiers from
<http://docs.python.org/release/2.6.7/library/stdtypes.html#string-formatting-operations>.  

__Ex.2__: Investigate some of the other built-in string manipulation
functions available in Python, documented at 
<http://docs.python.org/release/2.6.7/library/stdtypes.html#string-methods>.  

__Ex.3__: Investigate the builtin list functions in Python.  Modify
your programme to print `lst` both unsorted and sorted.

__Ex.4__: Consider the following function definition:

```python
def p(s):
    return "<p>%s</p>" % s
```

Add this to the application after the HTML boilerplate string, and
then make use of it to simplify and reduce repetition in your code.

__Ex.5__: Explore the builtin methods available to both lists and
dictionaries. 
