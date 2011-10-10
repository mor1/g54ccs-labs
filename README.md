G54CCS Lab Exercises: Google App Engine (Python)
================================================

These exercises are intended to take you through the basics of
building simple cloud-hosted applications, using the Python
programming language on Google's App Engine (GAE) platform as an
example.  They can all be carried out using the local development
server provided as part of the GAE development environment.  If you
wish to try running them live on GAE you will need to sign up for a
Google account on GAE by following the instructions at
<http://appspot.com/>.

Ultimately, cloud programming necessarily involves the Internet.  In
particular, many platforms, GAE among them, make extensive use of the
HTTP protocol used when you access the web.  Although the details of
HTTP are outside the scope of this lab, it is necessary to understand
a few basics of its operation. 

HTTP is a text-based protocol which allows clients to make _requests_
of servers, which return _responses_.  Requests and responses both
contain a number of _headers_ and some _content_.  Headers are used to
communicate important data -- or _metadata_ -- about the content and
the connection to the server, e.g., the length of the content
(`Content-Length`).   

There are several different types of request which indicate different
behaviours to be carried out at the server.  The two main ones used in
these labs are: 
+ `GET` which simply fetches a page and should _not_ make any
  modification to data on the server; and
+ `POST` which is commonly used to send data to the server, and _may_
  result in modification of state stored at the server.


[0] Plain Old Hello World! in Python
-----------------------------------

### Topics:
+ variables: strings, ints, floats, tuples (inc. singleton), lists,
  maps 
+ arithmetic operators
+ (simple) type conversions such as converting string to int
+ string interpolation
+ function definition and invocation, with parameters
+ modules
   
This exercise does not involve GAE at all, but takes you through the
basics of simple Python programming.  Python is a rich, dynamic,
object-oriented programming language, used for programs ranging in
size from simple scripts to multi-thousand line applications.  
                                                               
The intent of this exercise is _not_ to turn you into a first class
Python programmer, but to give you sufficient understanding that you
can follow these exercises.  Those who believe they are already fluent
Python programmers may be able to skip this exercise, although I would
recommend at least reading through it.  More details can be found at
<http://python.org/> and, in particular, the tutorial at
<http://python.org/tutorial/> is available for those who wish a better
understanding of Python programming. 
  
   
[1] Hello World!
---------------

### Topics:
+ basic Google App Engine application structure
+ basic URL handling with a response (GET)
+ errors

This exercise introduces GAE through a minimal sample application.
GAE applications provide for interaction by invoking computation when
supported URLs are accessed.  In this case, the application provides
two URLs:

+ `/hello` which returns a basic HTML page saying "hello world!"
+ `/error` which deliberately


[2] Hello Wait!
--------------

### Topics:
+ a more structured application 
+ simple parameter handling (GET)

This exercise builds on the previous exercise in the following ways:
+ restructuring it so that it is better modularised and easier to
  understand as it grows; and
+ introduces two ways to pass _parameters_ into your GAE application.

The application presents three URL handlers:
+ `/wait-random/` which waits for a random delay between [0, 10]
  seconds before returning a slightly modified "hello world" page;
+ `/wait-param/` which waits for the delay specified as a URL
  parameter in the request before returning the modified "hello world"
  page; and;
+ `/wait-url/` which does the same but obtains the delay parameter
  from the URL itself rather than as a request parameter.


[3] Hello again!
---------------

### Topics:
+ storing and retrieving data
+ GET, POST
+ simple templates
+ admin console


<!--
4. Hello for the final time!
   + maintaining state via tickets 

5. Hello Mashup!
   + simple use of web services eg., twitter search
-->   
