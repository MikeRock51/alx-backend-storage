#!/usr/bin/env python3
"""Access mongodb via pymongo"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """Lists all documents in a mongodb collection"""

    client = MongoClient('mongodb://localhost:27017')
