#!/usr/bin/env python3
"""Change topics based on name"""


def update_topics(mongo_collection, name, topics):
    """Use update many to update the names of docs in collection"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
