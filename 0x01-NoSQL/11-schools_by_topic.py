#!/usr/bin/env python3
"""
    Write a Python function that returns the list
    of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools that offers requested topic"""

    schools = mongo_collection.find({'topics': {'$in': [topic]}})

    return schools
