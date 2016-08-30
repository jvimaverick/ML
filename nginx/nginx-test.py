#!/usr/bin/python

import requests
import sys

class Smoketest:
    def __init__(self, server='127.0.0.1'):
        self.server = server
        self.urls = {
	   '/a1': {'response':[200,301], 'text': 'app'},
	   '/a2': {'response':[200,301], 'text': 'app'},
	   '/test4': {'response':[200,301], 'text': 'app'},
	}
        self.test_urls()
	self.ok()

    def test_urls(self):
        for key,value in self.urls.iteritems():
            self.get_url(key, value['response'], value['text'])

    def get_url(self, url, response=[200], text=None):
        try:
            r = requests.get("%s%s" %(self.server, url))
            #print url
            #print r.status_code
	    if not r.status_code in response:
                print "not passed on: url=%s status_code=%s" %(url,r.status_code)
                sys.exit(1)
            
            if text!=None and r.text.find(text)==-1:
                print "string=%s not found" %text
                sys.exit(1)
            #print r.text
        except Exception as e:
            print e
            sys.exit(1)

    def ok(self):
        print "awesome all looks good"
        sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv)==1:
	print "usage: %s http://example.com" %sys.argv[0]
	sys.exit(1)
    test = Smoketest(sys.argv[1])
