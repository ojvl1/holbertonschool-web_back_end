#!/usr/bin/env python3
''' function that inserts a new document in a collection '''
from pymongo import MongoClient


client = MongoClient(host='localhost', port=27017)


def insert_school(mongo_collection, **kwargs):
    ''' insert document in collection '''
    new_value = mongo_collection.insert_one(kwargs)

    return (new_value.inserted_id)