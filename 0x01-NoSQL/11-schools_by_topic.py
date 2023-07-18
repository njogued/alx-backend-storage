#!/usr/bin/env python3
"""Find topic given a collection in mongo using pymongo"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school matched by topic"""
    docs = mongo_collection.find({"topics": topic})
    return docs
