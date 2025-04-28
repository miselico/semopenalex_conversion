from boto.s3.connection import S3Connection
from smart_open import smart_open
import rdflib


conn = S3Connection()
bucket = conn.get_bucket('semopenalex')

for key in bucket.list():
    print(key.name)	
    # container = ""
    # if "summary" in key.name:
    # 	continue
    # content = smart_open('s3://semopenalex/'+key.name, 'rb')
    # graph = rdflib.Graph()
    # graph.parse(content)
    # graph.serialize(format='nt', destination="tbl.ttl")


