'''from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyC8uUGVz2j6tBJ0QGqRlFwTzTpvq9eSC28"
my_cse_id = "Custom Search Engine ID"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    'stackoverflow site:en.wikipedia.org', my_api_key, my_cse_id, num=10)
for result in results:
    pprint.pprint(result)
'''
import re
import urllib.request as ur

print('What would you like to look up?')
text = input('::')
search_string = text.split(' ')
search_string = '+'.join(search_string)
# you can change www.bing.com to any search engine except google.
googlesearch = 'https://www.bing.com/search?q=' + search_string
source = ur.urlopen(googlesearch)
source = source.read()
source = str(source)        
output = re.findall(r'''(?:http://|www.)[^"]+''', source)
for i in range(len(output)):
    print(output[i])
