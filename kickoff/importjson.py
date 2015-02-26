import json
json_data=open('/home/sylvestre/dev/mozilla/product-details.svn/json/languages.json')
parsed = json.load(json_data)
#print parsed

print json.dumps(parsed, indent=4, sort_keys=True, encoding="ascii").decode('unicode-escape')

#json_data=open('foo')
#parsed = json.load(json_data)
#print parsed
#print json.dumps(parsed, indent=4, sort_keys=True).decode('unicode-escape')
#.decode('unicode-escape')
