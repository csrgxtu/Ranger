#!/usr/bin/env python
# coding=utf-8
#
# Author: archer
# File: main.py
# Desc: Process all json data files, extract the BookInfo
# Produced By BR
import json
from util import ParseJsonCNMARC
import glob
import sys
from pymongo import MongoClient

# first, get command argument, the directory of the json files
if len(sys.argv) != 2:
    print 'Usage: ./main.py jsondir'
    exit(1)
JSON_DIR = sys.argv[1]

# second, loop the json file in JSON_DIR
client = MongoClient('mongodb://192.168.100.2:27017/')
db = client['cnmarc']
collection = db['cnmarc1']

for jsonfile in glob.glob(JSON_DIR + "/*.json"):
    print jsonfile
    f = open(jsonfile, 'r')
    recs = json.loads(f.read())
    for rec in recs:
        print rec
        BookInfo = ParseJsonCNMARC(rec)
        print collection.insert_one(BookInfo).inserted_id, BookInfo['authors']
