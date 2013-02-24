#!/usr/bin/env python
import cgi
import jinja2
import os
import logging
import wsgiref.handlers
import urllib
import json
from datetime import date, timedelta
from google.appengine.api import urlfetch
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.api import memcache

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class PagerdutyHandler(webapp.RequestHandler):
    def get(self):
        today = date.today()
        baseUrl = 'https://pearsonsocial.pagerduty.com/api/v1'
        schedUrl = baseUrl + '/schedules/PPSH1M0?include_oncall=1&since=' + str(today) + '&until=' + str(today)
        
        #logging.info('schedUrl=' + schedUrl)
        scheduleHttpResponse = urlfetch.fetch(url=schedUrl,
                        method=urlfetch.GET,
                        headers={'Content-Type': 'application/json',
                            'Authorization': 'Token token=putyourtokenhere'})

        
        schedule = json.loads(scheduleHttpResponse.content)
        oncallUserId = str(schedule['schedule']['oncall']['user']['id'])

        oncallUserInfoUrl = baseUrl + '/users/' + oncallUserId + '/notification_rules'
        oncallUserInfoHttpResponse = urlfetch.fetch(url=oncallUserInfoUrl,
                        #payload=form_data,
                        method=urlfetch.GET,
                        headers={'Content-Type': 'application/json',
                            'Authorization': 'Token token=putyourtokenhere'})

        userNotification = json.loads(oncallUserInfoHttpResponse.content)
        # format sms/phone numbers correcctly
        for notification in userNotification['notification_rules']:
          if notification['contact_method']['address'].isalnum():
            if len(notification['contact_method']['address']) == 10:  # sorry, no international support...
              notification['contact_method']['address'] = notification['contact_method']['address'][0:3] + '.' \
                                                          + notification['contact_method']['address'][3:6] + '.' \
                                                          + notification['contact_method']['address'][6:10]

        #build the jinja template
        template_values = {
            'name': schedule['schedule']['oncall']['user']['name'],
            'oncallStartDate': schedule['schedule']['oncall']['start'],
            'oncallEndDate': schedule['schedule']['oncall']['end'],
            'userNotification': userNotification


        }

        template = jinja_environment.get_template('pagerduty-confluence-widget.html')
        self.response.out.write(template.render(template_values))

def main():
    
    application = webapp.WSGIApplication([('/pagerduty', PagerdutyHandler)],debug=True)
    util.run_wsgi_app(application)
    
if __name__ == '__main__':
    main()