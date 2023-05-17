""" 
Created on : 16/05/23 4:41 pm
@author : ds  
"""

from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch("https://localhost:9200")

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}

res = es.index(index='test-index',document=doc)
print(res['_source'])


es.indices.refresh(index="test-index")

res = es.search(index="test-index", query={"match_all": {}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])