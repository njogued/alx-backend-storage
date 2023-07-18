#!/usr/bin/env python3
"""Use pymongo to get deets on nginx logs"""


import pymongo
from pymongo import MongoClient


def log_nginx_stats(mongo_collection):
    """Function to get nginx stats logs"""
    print(f"{mongo_collection.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        number = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {number}")

    count_gets = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{count_gets} status check")


if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_nginx_stats(mongo_collection)
