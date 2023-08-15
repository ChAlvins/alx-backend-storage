#!/usr/bin/env python3
"""
With a function that list all document
in a collection
"""
import pymongo


def list_all(mongo_collection):
    """find or list all collection documents"""
    documents = mongo_collection.find()
    return list(documents)
