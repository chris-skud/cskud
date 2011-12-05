#!/usr/bin/env python
import cgi
import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render('main.html', {}))
        
def main():
    
    application = webapp.WSGIApplication([('/', MainHandler)],debug=True)
    util.run_wsgi_app(application)
    
if __name__ == '__main__':
    main()

