from imports import *



def get_marketdata_board(dict_columns, dict_RGBI, dict_all, board='TQOB'):
    '''
    Получение двух словарей с индексом RGBI и всех облигаций в режиме торгов TQOB
    '''
    print(board)
    URL = f'https://iss.moex.com/iss/engines/stock/markets/bonds/boards/{board}/securities.json'
    #  https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQOB/securities.json
    response = requests.get(URL).json()
    for key in response.keys():
        for row in response[key]['data']:
            for index in dict_RGBI.keys():
                for secid in dict_RGBI[index].keys():
                    if row[0] == dict_RGBI[index][secid]['secid']:
                        for i in range(0,len(row)):
                            name = dict_columns[response[key]['columns'][i]]
                            itog = row[i]
                            dict_RGBI[index][secid][name] = itog


    if list(dict_all.keys()) == []:
        number_index = 1
    else:
        number_index = max(list(dict_all.keys()))+1


    for key in response.keys():
        for row in response[key]['data']:
            dict_all[number_index] = {}
            dict_all[number_index]['secid'] = row[0]
            number_index +=1


    for key in response.keys():
        for row in response[key]['data']:
            for secid in dict_all.keys():
                if row[0] == dict_all[secid]['secid']:
                    for i in range(0,len(row)):
                        if response[key]['columns'][i] in dict_columns.keys():
                            name = dict_columns[response[key]['columns'][i]]
                            itog = row[i]
                            dict_all[secid][name] = itog
                    #print(dict_all)
                    #break

    return dict_RGBI, dict_all


def get_marketdata_board2(dict_columns, dict_RGBI, dict_all, board='TQOB'):
    '''
    Получение двух словарей с индексом RGBI и всех облигаций в режиме торгов TQOB
    '''
    #dict_RGBI
    URL = f'https://iss.moex.com/iss/engines/stock/markets/bonds/boards/{board}/securities.json'
    #  https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQCB/securities.json

    # https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQOB/securities/columns.json
    # Колонки

    response = requests.get(URL).json()
    for key in response.keys():
        for row in response[key]['data']:
            for index in dict_RGBI.keys():
                for secid in dict_RGBI[index].keys():
                    if row[0] == dict_RGBI[index][secid]['secid']:
                        for i in range(0,len(row)):
                            name = dict_columns[response[key]['columns'][i]]
                            itog = row[i]
                            dict_RGBI[index][secid][name] = itog


    if list(dict_all.keys()) == []:
        number_index = 1
    else:
        number_index = max(list(dict_all.keys()))+1


    for key in response.keys():
        for row in response[key]['data']:
            dict_all[number_index] = {}
            dict_all[number_index]['secid'] = row[0]
            number_index +=1


    for key in response.keys():
        for row in response[key]['data']:
            for secid in dict_all.keys():
                if row[0] == dict_all[secid]['secid']:
                    for i in range(0,len(row)):
                        if response[key]['columns'][i] in dict_columns.keys():
                            name = dict_columns[response[key]['columns'][i]]
                            itog = row[i]
                            dict_all[secid][name] = itog
                    #print(dict_all)
                    #break

    return dict_RGBI, dict_all
