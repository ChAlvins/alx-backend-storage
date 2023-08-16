#!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx, Display same as example
first line: x logs, x number of documents in this collection
second line: Methods
5 lines with method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
one line with method=GET, path=/status
"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def get_logs_stats(collection, option=None):
    """
    Provide some stats about Nginx logs stored in MongoDB
    """
    if option:
        count = collection.count_documents({"method": option})
        print("\tmethod {}: {}".format(option, count))
        return

    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))
    print("Methods:")
    for method in METHODS:
        get_logs_stats(collection, method)
    status_check_count = collection.count_documents(
            {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check_count))


if __name__ == "__main__":
    """ Replacing'mongodb://127.0.0.1:27017' with MongoDB connection URL"""
    mongodb_url = 'mongodb://127.0.0.1:27017'
    client = MongoClient(mongodb_url)
    db = client.logs
    nginx_collection = db.nginx

    get_logs_stats(nginx_collection)
