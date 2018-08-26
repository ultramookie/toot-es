#!/usr/bin/env python

import json
import urllib
import urllib2
import datetime
from elasticsearch import Elasticsearch

tootinfo = {}

now = datetime.datetime.now()
index = "tootinfo-" + str(now.year)
doc_type = "tootinfo"
elastichost='localhost:9200'
url = "https://trblmkr.net/api/v1/instance"

es = Elasticsearch(elastichost)

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

req = urllib2.Request(url, None, headers)
r = urllib2.urlopen(req)
resp = json.loads(r.read())
r.close()

tootinfo['users'] = resp['stats']['user_count']
tootinfo['domains'] = resp['stats']['domain_count']
tootinfo['statuses'] =  resp['stats']['status_count']
tootinfo['version'] = resp['version']
tootinfo['uri'] = resp['uri']
tootinfo['date'] = now
id = now

es.index(index=index, doc_type=doc_type, id=id, body=tootinfo)
