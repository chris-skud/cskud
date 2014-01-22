#!/usr/bin/env python
import cgi
import wsgiref.handlers
import json
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch

class MainHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write(template.render('main.html', {}))

class ProtoHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write(template.render('proto/main.html', {}))

def main():
  application = webapp.WSGIApplication([('/', MainHandler), ('/proto/', ProtoHandler)], debug=True)
  util.run_wsgi_app(application)

if __name__ == '__main__':
  main()