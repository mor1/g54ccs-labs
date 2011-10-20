G54CCS Labs, Exercise 3
=======================

This exercise extends the previous exercise as follows:

+ As your programmes are getting more complex, we impose more
  structure by splitting `app.py` up, to help keep the code
  manageable.
+ We introduce two ways for the user to pass parameters into your
  GAE application from their browser.
  
  
Structure
---------

Commonly, GAE applications split into three parts, given in three
separate files: 

+ `urls.py` containing the mapping between the application's URLs and
  the classes that handle them;
+ `views.py` containing the classes with the code that actually
  handles the URLS; and
+ `models.py` containing code connected with storing data in App
  Engine -- this is investigated in the next exercise.
  
Splitting the code up like this makes it easier to track your code as
the application becomes more complex.  It is, of course, possible to
further subdivide your code among more files if it continues to grow.


`urls.py`
---------
