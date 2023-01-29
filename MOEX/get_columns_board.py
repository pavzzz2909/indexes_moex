from imports import *


def get_dict_columns(board):
    URL = f'https://iss.moex.com/iss/engines/stock/markets/bonds/boards/{board}/securities/columns.json'
    # https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQOB/securities/columns.json
    dict = {}
    response = requests.get(URL).json()
    for key in response:
        for row in response[key]['data']:
            dict[row[1]] = row[2]
    return dict
