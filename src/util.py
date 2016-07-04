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

    # publisher_name
    if '210' in dictjson:
        if 'c' in dictjson['210']:
            start = dictjson['210'].index('c') + 1
            if 'd' in dictjson['210']:
                end = dictjson['210'].index('d')
            else:
                end = -1
            BookInfo['publisher_name'] = dictjson['210'][start:end]
    else:
        BookInfo['publisher_name'] = None

    # 发布地址， publish_place
    if '210' in dictjson:
        if 'a' in dictjson['210']:
            start = dictjson['210'].index('a') + 1
            if 'c' in dictjson['210']:
                end = dictjson['210'].index('c')
            else:
                end = -1
            BookInfo['publish_place'] = dictjson['210'][start:end]
    else:
        BookInfo['publish_place'] = None

    # 发布时间， publisher_date
    if '210' in dictjson:
        if 'd' in dictjson['210']:
            start = dictjson['210'].index('d') + 1
            BookInfo['publisher_date'] = dictjson['210'][start:]
    else:
        BookInfo['publisher_date'] = None

    # binding
    if '010' in dictjson:
        if 'b' in dictjson['010']:
            start = dictjson['010'].index('b') + 1
            if 'd' in dictjson['010']:
                end = dictjson['010'].index('d')
                BookInfo['binding'] = dictjson['010'][start:end]
            else:
                BookInfo['binding'] = dictjson['010'][start:]
    else:
        BookInfo['binding'] = None

    # 书籍类型， length_style
    if '200' in dictjson:
        if 'b' in dictjson['200']:
            start = dictjson['200'].index('b') + 1
            end = start + 2
            BookInfo['length_style'] = dictjson['200'][start:end]
    else:
        BookInfo['length_style'] = None

    # price
    if '010' in dictjson:
        if 'd' in dictjson['010']:
            start = dictjson['010'].index('d') + 1
            BookInfo['price'] = dictjson['010'][start:]
    else:
        BookInfo['price'] = None

    # summary
    if '330' in dictjson:
        if 'a' in dictjson['330']:
            start = dictjson['330'].index('a') + 1
        else:
            start = 0
        BookInfo['summary'] = dictjson['330'][start:]
    else:
        BookInfo['summary'] = None

    # isbn
    if '010' in dictjson:
        if 'a' in dictjson['010']:
            start = dictjson['010'].index('a') + 1
            end = start + 17
            if 'b' in dictjson['010']:
                end = dictjson['010'].index('b')
            elif 'd' in dictjson['010']:
                end = dictjson['010'].index('d')
            else:
                end = -1
            BookInfo['isbn'] = dictjson['010'][start:end].strip('-')
    else:
        BookInfo['isbn'] = None

    # 书籍尺寸， size
    if '215' in dictjson:
        if 'd' in dictjson['215']:
            start = dictjson['215'].index('d') + 1
            if 'cm' in dictjson['215']:
                end = dictjson['215'].index('cm')
            else:
                end = -1
            BookInfo['size'] = dictjson['215'][start:end]
    else:
        BookInfo['size'] = None

    # pagesize
    if '215' in dictjson:
        if 'a' in dictjson['215']:
            dictjson['215'] = dictjson['215'].strip('cm')
            start = dictjson['215'].index('a') + 1
            if 'c' in dictjson['215']:
                end = dictjson['215'].index('c')
            elif 'd' in dictjson['215']:
                end = dictjson['215'].index('d')
            elif 'e' in dictjson['215']:
                end = dictjson['215'].index('e')
            else:
                end = -1
            BookInfo['pagesize'] = dictjson['215'][start:end]
    else:
        BookInfo['pagesize'] = None



    # print_date
    if '100' in dictjson:
        if 'a' in dictjson['100']:
            start = dictjson['100'].index('a') + 1
            # end = dictjson['100'].index('d')
            end = start + 8
            BookInfo['print_date'] = dictjson['100'][start:end]
    else:
        BookInfo['print_date'] = None

    # title
    if '200' in dictjson:
        if 'a' in dictjson['200']:
            start = dictjson['200'].index('a') + 1
            end = dictjson['200'].index('b')
            BookInfo['title'] = dictjson['200'][start:end]
    else:
        BookInfo['title'] = None

    # translators[]

    # authors[]
    BookInfo['authors'] = []
    if '701' in dictjson:
        if 'a' in dictjson['701']:
            start = dictjson['701'].index('a') + 1
            if '9' in dictjson['701']:
                end = dictjson['701'].index('9')
            else:
                end = -1
            BookInfo['authors'].append(dictjson['701'][start:end])

    if '702' in dictjson:
        if 'a' in dictjson['702']:
            start = dictjson['702'].index('a') + 1
            if '9' in dictjson['702']:
                end = dictjson['702'].index('9')
            else:
                end = -1
            BookInfo['authors'].append(dictjson['702'][start:end])
    # if len(BookInfo['authors']) == 0:
    #     print dictjson
    #     exit(2)

    # tags[]
    # BookInfo['tags'] = []
    if '606' in dictjson:
        dictjson['606'] = dictjson['606'][2:]
        # replace a, x, y, z, j
        dictjson['606'] = dictjson['606'].replace('a', '#')
        dictjson['606'] = dictjson['606'].replace('x', '#')
        dictjson['606'] = dictjson['606'].replace('y', '#')
        dictjson['606'] = dictjson['606'].replace('z', '#')
        dictjson['606'] = dictjson['606'].replace('j', '#')
        BookInfo['tags'] = dictjson['606'].split('#')[1:]

    return BookInfo
