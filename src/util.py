#!/usr/bin/env python
# coding=utf-8

# 读取文件到一个变量
# 接受文件路径，返回string文本
def ReadFile(filename):
    with open(filename, 'r') as f:
        return f.read()

# 解析一条JSON格式的CNMARC记录
# 接受dict(json)格式的一条记录，返回对应的书籍信息
def ParseJsonCNMARC(dictjson):
    BookInfo = {}

    # publisher
    if dictjson['210']:
        BookInfo['publisher'] = dictjson['210']
    else:
        BookInfo['publisher'] = None

    # binding
    if dictjson['010']:
        if dictjson['010'].index('b'):
            start = dictjson['010'].index('b')
            if dictjson['010'].index('d'):
                end = dictjson['010'].index('d')
                BookInfo['binding'] = dictjson['010'][start:end]
            else:
                BookInfo['binding'] = dictjson['010'][start:]
    else:
        BookInfo['binding'] = None

    # price
    if dictjson['010']:
        if dictjson['010'].index('d'):
            start = dictjson['010'].index('d')
            BookInfo['price'] = dictjson['010'][start:]
    else:
        BookInfo['price'] = None

    # summary
    if dictjson['330']:
        start = dictjson['330'].index('a')
        BookInfo['summary'] = dictjson['330'][start:]
    else:
        BookInfo['summary'] = None

    # isbn13
    if dictjson['010']:
        if dictjson['010'].index('a'):
            start = dictjson['010'].index('a')
            end = start + 17
            if dictjson['010'].index('b'):
                end = dictjson['010'].index('b')
            else:
                end = dictjson['010'].index('d')

        BookInfo['isbn'] = dictjson['010'][start:end]
    else:
        BookInfo['isbn'] = None

    # pages
    if dictjson['215']:
        if dictjson['215'].index('a'):
            start = dictjson['215'].index('a')
            if dictjson['215'].index('c'):
                end = dictjson['215'].index('c')
            elif dictjson['215'].index('d'):
                end = dictjson['215'].index('d')
            elif dictjson['215'].index('e')
                end = dictjson['215'].index('e')
            else:
                end = -1
            BookInfo['pages'] = dictjson['215'][start:end]
    else:
        BookInfo['pages'] = None

    # pubdate
    if dictjson['100']:
        if dictjson['100'].index('a'):
            start = dictjson['100'].index('a')
            end = dictjson['100'].index('d')
            BookInfo['pubdate'] = dictjson['100'][start:end]
    else:
        BookInfo['pubdate'] = None

    # title
    if dictjson['200']:
        if dictjson['200'].index('a'):
            start = dictjson['200'].index('a')
            end = dictjson['200'].index('b')
            BookInfo['title'] = dictjson['200'][start:end]
    else:
        BookInfo['title'] = None

    # translators[]

    # authors[]

    # tags[]
