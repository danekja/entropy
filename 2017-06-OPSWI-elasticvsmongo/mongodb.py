import numpy as np
from pymongo import MongoClient

from queries.mongodbQueries import mongo_query_list as query_list

client = MongoClient('localhost', 27017)
db = client['opswi']  # db name
collection = db['data']  # collection name

for idx, query in enumerate(query_list):
    times = []

    for i in range(0, 100):
        res = collection.find(query).explain()
        exec_time = res['executionStats']['executionTimeMillis']
        times.append(exec_time)

    print "MongoDB query nr %d " % (idx + 1)
    print "mean %f ms" % np.mean(times)
    print "standard deviation %f ms" % np.std(times)

    print("%d document(s) found " % res['executionStats']['nReturned'])
    print('---------------------\n')
