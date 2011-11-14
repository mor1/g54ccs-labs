G54CCS Labs, Exercise 5
=======================

Previous exercises have been quite tightly directed as to what you need to do
and the result you should produce.  This exercise is more open-ended and will
require you to apply what you have learnt so far to build a simple
cloud-hosted guestbook application.  It leans heavily on material from
exercises #3 and #4 in particular.

Note that this exercise is about trying to apply the cloud computing
techniques you have learned so far.  It is __not__ about producing a heavily
styled, graphically appealing website with flashy images, intrusive
audio, or extensive use of Javascript.

The Guestbook
-------------

The basic guestbook application needs to support essentially two methods:

+ _Add an entry_.  A user should be able to add an entry to the guestbook,
  which should be stored along with some user name and the time the entry was
  added.
+ _Retrieve all entries_.  A user should be able to visit a page which
  displays all of the entries so far added to the guestbook, in the order in
  which they were added.
  
To implement these core features think about the _data model_ (`models.py`)
and the changes to the set of fields you require over exercise #4 (storage).
Note that you will (obviously) need to store _multiple_ entries this time,
where the code discussed in exercise #4 ended up storing only a _single_ row.
Think also about the URLs (`urls.py`) through you wish to expose views on your
data (`views.py`).  Finally, you may need to make use of slightly more complex
page templating that exercise #4 required: read the documentation on GAE page
templates at
<http://code.google.com/appengine/docs/python/gettingstarted/templates.html>. 

Extensions
----------

Having got these first two features -- the core of the application -- working,
consider adding the following extensions: 

__Ex.1__.  Allow users to edit and update existing entries.

__Ex.2__.  Store a a full edit history with each entry, and when entries are
retrieved for display, allow each entry's full history to be displayed with
the entry. 

__Ex.3__.  Enable users to vote for entries with which they agree/disagree.

__Ex.4__.  Enable users to discuss and comment on entries, and on comments, in
a simple 'threaded' interface. 
