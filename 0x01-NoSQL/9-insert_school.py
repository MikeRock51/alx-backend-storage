#!/usr/bin/env python3
"""
    Write a Python function that inserts a new
    document in a collection based on kwargs:
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection"""

    inserted = mongo_collection.insert_one(kwargs)

    return inserted.inserted_id
