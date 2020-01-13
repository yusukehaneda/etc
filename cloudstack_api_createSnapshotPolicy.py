import urllib.request
import urllib.parse
import hashlib
import hmac
import base64
import sys
import pprint
import json

baseurl = 'https://tky001b.pf.gmocloud.com/client/api?'
request = {}
request['command'] = 'createSnapshotPolicy'
#request['command'] = 'listUsers'
request['response'] = 'json'
request['volumeid'] = '48112a06-c81d-464f-aacd-08bed5a9c7c5'
#request['intervaltype'] = 'daily'
request['intervaltype'] = 'weekly'
#request['intervaltype'] = 'monthly'
request['maxsnaps'] = '2'
'''
daily '10:03'(3:10)
weekly '10:03:1'(Sunday 3:10)
monthly '10:03:15'(15th 3:10)
'''
#request['schedule'] = '0:03' #daily
request['schedule'] = '40:03:1' #weekly
request['schedule'] = '30:03:1' #monthly


request['timezone'] = 'JST'
#request['']=''
request['apikey'] = sys.argv[1]
secretkey = sys.argv[2]

request_str = '&'.join(['='.join([k,urllib.parse.quote_plus(request[k])]) for k in request.keys()])

sig_str = '&'.join(['='.join([k.lower(),urllib.parse.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request.keys())])

digest = hmac.new(secretkey.encode('utf-8'),sig_str.lower().encode('utf-8'),hashlib.sha1).digest()
sig = urllib.parse.quote_plus(base64.b64encode(digest).decode('utf-8').strip())

req = baseurl+request_str+'&signature='+sig

res = urllib.request.urlopen(req)
result = res.read()
print(type(result))

#python3.6
dd = json.loads(result)
pprint.pprint(dd, width=40)
print(dd['createsnapshotpolicyresponse']['snapshotpolicy']['schedule'])

#python 3.5
result = result.decode('utf-8')
ee = json.loads(result)
print(ee)
print(ee['createsnapshotpolicyresponse']['snapshotpolicy']['schedule'])
