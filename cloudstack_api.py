import urllib.request
import urllib.parse
import hashlib
import hmac
import base64

baseurl='https://tky001b.pf.gmocloud.com/client/api?'
request={}
request['command']='listUsers'
request['response']='json'
request['apikey']=''
secretkey=''

request_str='&'.join(['='.join([k,urllib.parse.quote_plus(request[k])]) for k in request.keys()])

sig_str='&'.join(['='.join([k.lower(),urllib.parse.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request.keys())])

digest=hmac.new(secretkey.encode('utf-8'),sig_str.lower().encode('utf-8'),hashlib.sha1).digest()
sig=urllib.parse.quote_plus(base64.b64encode(digest).decode('utf-8').strip())

req=baseurl+request_str+'&signature='+sig

res=urllib.request.urlopen(req)
result=res.read()
print(result)
