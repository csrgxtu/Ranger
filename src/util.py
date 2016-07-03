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
    if '210' in dictjson:
    # if dictjson['210']:
        BookInfo['publisher'] = dictjson['210']
    else:
        BookInfo['publisher'] = None


    # binding
    if '010' in dictjson:
    # if dictjson['010']:
        if 'b' in dictjson['010']:
            start = dictjson['010'].index('b')
            if 'd' in dictjson['010']:
                end = dictjson['010'].index('d')
                BookInfo['binding'] = dictjson['010'][start:end]
            else:
                BookInfo['binding'] = dictjson['010'][start:]
    else:
        BookInfo['binding'] = None

    # price
    if '010' in dictjson:
    # if dictjson['010']:
        if 'd' in dictjson['010']:
            start = dictjson['010'].index('d')
            BookInfo['price'] = dictjson['010'][start:]
    else:
        BookInfo['price'] = None

    # summary
    if '330' in dictjson:
    # if dictjson['330']:
        start = dictjson['330'].index('a')
        BookInfo['summary'] = dictjson['330'][start:]
    else:
        BookInfo['summary'] = None

    # isbn13
    if '010' in dictjson:
    # if dictjson['010']:
        if 'a' in dictjson['010']:
            start = dictjson['010'].index('a')
            end = start + 17
            if 'b' in dictjson['010']:
                end = dictjson['010'].index('b')
            else:
                end = dictjson['010'].index('d')

        BookInfo['isbn'] = dictjson['010'][start:end]
    else:
        BookInfo['isbn'] = None

    # pages
    if '215' in dictjson:
    # if dictjson['215']:
        if 'a' in dictjson['215']:
            start = dictjson['215'].index('a')
            if 'c' in dictjson['215']:
                end = dictjson['215'].index('c')
            elif 'd' in dictjson['215']:
                end = dictjson['215'].index('d')
            elif 'e' in dictjson['215']:
                end = dictjson['215'].index('e')
            else:
                end = -1
            BookInfo['pages'] = dictjson['215'][start:end]
    else:
        BookInfo['pages'] = None

    # pubdate
    if '100' in dictjson:
    # if dictjson['100']:
        if 'a' in dictjson['100']:
            start = dictjson['100'].index('a')
            end = dictjson['100'].index('d')
            BookInfo['pubdate'] = dictjson['100'][start:end]
    else:
        BookInfo['pubdate'] = None

    # title
    if '200' in dictjson:
    # if dictjson['200']:
        if 'a' in dictjson['200']:
            start = dictjson['200'].index('a')
            end = dictjson['200'].index('b')
            BookInfo['title'] = dictjson['200'][start:end]
    else:
        BookInfo['title'] = None

    # translators[]

    # authors[]

    # tags[]

    return BookInfo
