from elasticsearch import Elasticsearch
import numpy as np
import time
from queries.elasticQueries import elastic_query_list as query_list

es = Elasticsearch()

for idx, query in enumerate(query_list):
    times = []

    for i in range(0, 100):
        t0 = time.time()
        results = es.search(index="opswi", body={"query": query})
        t1 = time.time()

        times.append((t1 - t0) * 1000)

    print "ElasticSearch query nr %d " % (idx + 1)
    print "mean %f ms" % np.mean(times)
    print "standard deviation %f ms" % np.std(times)

    print("%d document(s) found " % results['hits']['total'])
    print('---------------------\n')
