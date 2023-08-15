#!/usr/bin/env python3
"""
The module function insert new documents
in a collection based on Kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert new documents"""
    new_id = mongo_collection.insert_one(kwargs)
    return new_id.inserted_id
