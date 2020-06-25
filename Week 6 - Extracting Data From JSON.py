import urllib.request as ur
import json

json_url = input("Enter location: ")
print("Retrieving ", json_url)
data = ur.urlopen(json_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')


info = json.loads(data)
print('User count:', len(info))
sum=0
for item in info['comments']:
    print('Name', item['name'])
    print('Id', item['count'])
    sum=sum+item['count']
print(sum)