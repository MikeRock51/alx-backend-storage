#!/usr/bin/env python3
"""
    Write a Python script that provides some stats
    about Nginx logs stored in MongoDB:
        Database: logs
        Collection: nginx
        Display (same as the example):
        first line: x logs where x is the number of
        documents in this collection
        second line: Methods:
        5 lines with the number of documents with the
        method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        in this order (see example below - warning: it’s a
        tabulation before each line)
        one line with the number of documents with:
            method=GET
            path=/status
"""

from pymongo import MongoClient


if __name__ == '__main__':

    client = MongoClient()
    collection = client.logs.nginx

    logCount = collection.count_documents({})
    getMethodCount = collection.count_documents({'method': 'GET'})
    postMethodCount = collection.count_documents({'method': 'POST'})
    putMethodCount = collection.count_documents({'method': 'PUT'})
    patchMethodCount = collection.count_documents({'method': 'PATCH'})
    deleteMethodCount = collection.count_documents({'method': 'DELETE'})

    statusGetCount = collection.count_documents(
            {'method': 'GET', 'path': '/status'}
    )

    print("{} logs".format(logCount))
    print("Methods:")
    print("\tmethod GET: {}".format(getMethodCount))
    print("\tmethod POST: {}".format(postMethodCount))
    print("\tmethod PUT: {}".format(putMethodCount))
    print("\tmethod PATCH: {}".format(patchMethodCount))
    print("\tmethod DELETE: {}".format(deleteMethodCount))
    print("{} status check".format(statusGetCount))
