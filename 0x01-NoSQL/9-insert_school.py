#!/usr/bin/env python3
"""Function that will insert a doc into school"""


def insert_school(mongo_collection, **kwargs):
    """Insert document into collection"""
    return mongo_collection.insert_one(kwargs).inserted_id
