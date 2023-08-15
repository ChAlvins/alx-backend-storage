#!/usr/bin/env python3
"""module with  function that returns the list of school
having a specific topic:
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """returns list of school having a specific topic"""
    school_new_topic = mongo_collection.find(
            {"topics": topic})
    return list(school_new_topic)
