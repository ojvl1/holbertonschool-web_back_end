#!/usr/bin/env python3
''' 
    function that changes all topics of a 
    school document
'''
import pymongo
from typing import List


def update_topics(mongo_collection, name, topics):
    '''
    mongo_collection = collection
    name = school name to update
    topics = list of topics approached in the school
    '''

    query: dict = {'name': name}
    mongo_collection.update_many(query, {"$set": {"topics": topics}})
