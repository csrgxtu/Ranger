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

    # rganization_name
    if '801' in dictjson:
        if 'b' in dictjson['801']:
            start = dictjson['801'].index('b') + 1
            if 'c' in dictjson['801']:
                end = dictjson['801'].index('c')
            else:
                end = -1
            BookInfo['rganization_name'] = dictjson['801'][start:end]
        else:
            BookInfo['rganization_name'] = None
    else:
        BookInfo['rganization_name'] = None

    # country_code
    # if '801' in dictjson:
    #     if 'a' in dictjson['801']:
    #         start = dictjson['801'].index('a') + 1
    #         end = start + 2
    #         BookInfo['country_code'] = dictjson['801'][start:end]
    # else:
    #     BookInfo['country_code'] = None

    if '102' in dictjson:
        if 'a' in dictjson['102']:
            start = dictjson['102'].index('a') + 1
            if 'b' in dictjson['102']:
                end = dictjson['102'].index('b')
            else:
                end = len(dictjson['102'])
            BookInfo['country_code'] = dictjson['102'][start:end]
        else:
            BookInfo['country_code'] = None
    else:
        BookInfo['country_code'] = None

    # book_responsible
    if '701' in dictjson:
        if '4' in dictjson['701']:
            start = dictjson['701'].index('4') + 1
            end = -1
            BookInfo['book_responsible'] = dictjson['701'][start:end]
        else:
            BookInfo['book_responsible'] = None
    else:
        BookInfo['book_responsible'] = None

    # primary_responsible
    if '200' in dictjson:
        if 'f' in dictjson['200']:
            start = dictjson['200'].index('f') + 1
            if 'g' in dictjson['200']:
                end = dictjson['200'].index('g')
            else:
                end = len(dictjson['200'])
            if end < start:
                end = len(dictjson['200'])

            BookInfo['primary_responsible'] = dictjson['200'][start:end]
        else:
            BookInfo['primary_responsible'] = None
    else:
        BookInfo['primary_responsible'] = None

    # other_responsible
    print dictjson['200']
    if '200' in dictjson:
        if 'f' in dictjson['200']:
            if 'g' in dictjson['200']:
                start = dictjson['200'].rindex('g')
                if start < dictjson['200'].rindex('f'):
                    BookInfo['other_responsible'] = None
                else:
                    BookInfo['other_responsible'] = dictjson['200'][start:dictjson['200'].rindex('f')]
            else:
                BookInfo['other_responsible'] = None
        else:
            BookInfo['other_responsible'] = None

        # if 'g' in dictjson['200']:
        #     start = dictjson['200'].index('g') + 1
        #     if start > dictjson['200'].index('f'):
        #         BookInfo['other_responsible'] = dictjson['200'][start:]
        #     else:
        #         BookInfo['other_responsible'] = None
        # else:
        #     BookInfo['other_responsible'] = None
    else:
        BookInfo['other_responsible'] = None


    # clc_sort_num
    if '690' in dictjson:
        if 'a' in dictjson['690']:
            start = dictjson['690'].index('a') + 1
            # end = dictjson['690'].index('v5')
            BookInfo['clc_sort_num'] = dictjson['690'][start:]
        else:
            BookInfo['clc_sort_num'] = None
    else:
        BookInfo['clc_sort_num'] = None

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
    else:
        BookInfo['publish_place'] = None

    # 发布时间， publisher_date
    if '210' in dictjson:
        if 'd' in dictjson['210']:
            start = dictjson['210'].index('d') + 1
            BookInfo['publisher_date'] = dictjson['210'][start:]
        else:
            BookInfo['publisher_date'] = None
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
    else:
        BookInfo['binding'] = None

    # 书籍类型， length_style
    if '200' in dictjson:
        if 'b' in dictjson['200']:
            start = dictjson['200'].rindex('b') + 1
            end = start + 2
            BookInfo['length_style'] = dictjson['200'][start:end]
        else:
            BookInfo['length_style'] = None
    else:
        BookInfo['length_style'] = None

    # price
    if '010' in dictjson:
        if 'd' in dictjson['010']:
            start = dictjson['010'].index('d') + 1
            BookInfo['price'] = dictjson['010'][start:]
        else:
            BookInfo['price'] = None
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
            BookInfo['isbn'] = dictjson['010'][start:end].replace('-', '')
        else:
            BookInfo['isbn'] = None
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
    else:
        BookInfo['print_date'] = None

    # title
    if '200' in dictjson:
        if 'a' in dictjson['200']:
            start = dictjson['200'].index('a') + 1
            end = dictjson['200'].index('b')
            title = dictjson['200'][start:end]
            if '9' in title:
                end = title.index('9')
            BookInfo['title'] = title[0:end]
        else:
            BookInfo['title'] = None
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
        # else:
        #     BookInfo['authors'] = None


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
    if BookInfo['authors']:
        # print BookInfo['primary_responsible']
        author = BookInfo['primary_responsible']
        BookInfo['authors'].append(author)

    # main_heading
    if '606' in dictjson:
        if 'a' in dictjson['606']:
            start = dictjson['606'].index('a') + 1
            if 'x' in dictjson['606']:
                end = dictjson['606'].index('x')
            elif 'y' in dictjson['606']:
                end = dictjson['606'].index('y')
            else:
                end = len(dictjson['606'])
            main_heading = dictjson['606'][start:end]
            if 'y' in main_heading:
                end = main_heading.index('y')
            else:
                end = len(main_heading)
            BookInfo['main_heading'] = dictjson['606'][0:end]
        else:
            BookInfo['main_heading'] = None
    else:
        BookInfo['main_heading'] = None

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

    # year_sub
    if '606' in dictjson:
        if 'z' in dictjson['606']:
            start = dictjson['606'].index('z') + 1
            BookInfo['year_sub'] = dictjson['606'][start:]
    else:
        BookInfo['year_sub'] = None

    # area_sub
    if '606' in dictjson:
        if 'y' in dictjson['606']:
            start = dictjson['606'].index('y') + 1
            if 'z' in dictjson['606']:
                end = dictjson['606'].index('z')
            else:
                end = -1
            BookInfo['year_sub'] = dictjson['606'][start:end]
    else:
        BookInfo['area_sub'] = None

    # yopic_sub
    if '606' in dictjson:
        if 'x' in dictjson['606']:
            start = dictjson['606'].index('x') + 1
            if 'y' in dictjson['606']:
                end = dictjson['606'].index('y')
            else:
                end = -1
            BookInfo['yopic_sub'] = dictjson['606'][start:end]
    else:
        BookInfo['yopic_sub'] = None



    # n_series_title
    if '225' in dictjson:
        if 'a' in dictjson['225']:
            start = dictjson['225'].index('a') + 1
            if 'i' in dictjson['225']:
                end = dictjson['225'].index('i')
            elif 'f' in dictjson['225']:
                end = dictjson['225'].index('f')
            else:
                end = -1
            BookInfo['n_series_title'] = dictjson['225'][start:end]
    else:
        BookInfo['n_series_title'] = None

    return BookInfo
