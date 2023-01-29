from imports import *


def get_indexes():
    list = []
    dict = {}
    URL = f'http://iss.moex.com/iss/statistics/engines/stock/markets/index/analytics.json'
    response = requests.get(URL).json()
    for row in response["indices"]['data']:
        dict[row[0]]=row[1]
        list.append(row[0])
    return list, dict


def get_index_info(indexes=['RGBI']):
    '''
    Получение словаря с индексом RGBI
    '''
    dict = {}
    for index in indexes:
        dict[index] = {}
        URL = f'http://iss.moex.com/iss/statistics/engines/stock/markets/index/analytics/{index}.json?iss.meta=off&limit=200'
        response = requests.get(URL).json()
        number_index = 1
        for row in response['analytics']['data']:
            ticker = row[2]
            dict[index][number_index] = {"index" : row[0],
                                         "тикер" : row[2],
                                         "Короткое имя" : row[3],
                                         "secid" : row[4],
                                         "Доля в индексе" : row[5],
                                         "Торговая сессия" : row[6]}
            number_index +=1
    return dict
