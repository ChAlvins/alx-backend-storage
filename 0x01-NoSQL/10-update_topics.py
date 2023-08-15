#!/usr/bin/env python3
""" module with function that changes topics of a school
based on a name
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """changes al topics of a school document"""
    updated_doc = mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )
    return updated_doc
