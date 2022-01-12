import json
import os
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator  

# https://docs.couchbase.com/python-sdk/current/hello-world/start-using-sdk.html  
f = open('scan.json')
data = json.load(f)
f.close()

couchbaseUser = os.environ.get("COUCHBASE_USER")
couchbasePassword = os.environ.get("COUCHBASE_PASSWORD")

cluster = Cluster('couchbase://localhost', ClusterOptions(
  PasswordAuthenticator(couchbaseUser, couchbasePassword)))

bucket = cluster.bucket('trivy')
# _default scope and collections are created by default for a new bucket
collection = bucket.scope("_default").collection("_default")
print(data[0]['Target'])
result = collection.insert(data[0]['Target'], data[0])
cas = result.cas