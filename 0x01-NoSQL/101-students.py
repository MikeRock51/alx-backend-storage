#!/usr/bin/env python3
"""
    Write a Python function that returns all students
    sorted by average score:
        Prototype: def top_students(mongo_collection):
        mongo_collection will be the pymongo collection object
        The top must be ordered
        The average score must be part of each item
        returns with key = averageScore
"""

from statistics import mean


def top_students(mongo_collection):
    """Returns all students sorted by average score"""

    students = mongo_collection.find()

    for student in students:
        average_score = mean(
            [topic.get('score') for topic in student.get('topics')]
        )
        st = mongo_collection.update_one(
            {'_id': student.get('_id')},
            {'$set': {'averageScore': average_score}}
        )

    return mongo_collection.find().sort('averageScore', -1)
