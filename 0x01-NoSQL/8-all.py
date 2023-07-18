#!/usr/bin/env python3
"""List all the databases using pymongo"""
def list_all(collection):
    """Function that return a list of docs in collection"""
    if collection:
        return [doc for doc in collection.find()]
    return []
