#!/usr/bin/env python3
''' Function that lists all documents in a collection '''
from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)

def list_all(mongo_collection) -> list:
    '''List all documents in a collection'''
    documents: list = []

    for document in mongo_collection.find():
        documents.append(document)

    return documents
