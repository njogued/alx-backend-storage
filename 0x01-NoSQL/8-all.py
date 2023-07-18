#!/usr/bin/env python3
"""List all the databases using pymongo"""


def list_all(mongo_collection):
    """Function that return a list of docs in collection"""
    if mongo_collection:
        return [doc for doc in mongo_collection.find()]
    return []
