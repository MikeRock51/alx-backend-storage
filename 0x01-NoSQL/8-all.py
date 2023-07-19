#!/usr/bin/env python3
"""Access mongodb via pymongo"""


def list_all(mongo_collection):
    """Lists all documents in a mongodb collection"""

    docs = mongo_collection.find()

    if not docs:
        return []

    return docs
