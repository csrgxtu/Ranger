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

# first, get command argument, the directory of the json files
if len(sys.argv) != 2:
    print 'Usage: ./main.py jsondir'
    exit(1)
JSON_DIR = sys.argv[1]

# second, loop the json file in JSON_DIR
for jsonfile in glob.glob(JSON_DIR + "/*.json"):
    print jsonfile
