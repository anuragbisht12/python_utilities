"""Example of Python client calling Knowledge Graph Search API."""
from __future__ import print_function
import json
import urllib
#get API key from google developer
api_key = PUT_YOUR_API_KEY
query = 'Sachin Tendulkar'
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
    'query': query,
    'limit': 10,
    'indent': True,
    'key': api_key,
}
url = service_url + '?' + urllib.parse.urlencode(params)
response = json.loads(urllib.request.urlopen(url).read())
