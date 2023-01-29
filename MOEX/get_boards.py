""" Получение режимов торгов облигациями """
from imports import *


def get_boards():
    """ Получение двух словарей с индексом RGBI
    и всех облигаций в режиме торгов TQOB """
    dict_boards_all = {}
    dict_boards_T_plus = {}
    URL = f'https://iss.moex.com/iss/engines/stock/markets/bonds.json?iss.meta=off&iss.only=boards&boards'
    response = requests.get(URL).json()
    number_index = 1
    for board in response['boards']['data']:
        if 'Т+:' in board[3]:
            dict_boards_T_plus[board[0]] = {'board': board[2],
                                            'наименование': board[3],
                                            'is_trade': board[4]}
            dict_boards_all[board[0]] = {'board': board[2],
                                         'наименование': board[3],
                                         'is_trade': board[4]}
        else:
            dict_boards_all[board[0]] = {'board': board[2],
                                         'наименование': board[3],
                                         'is_trade': board[4]}
    return dict_boards_T_plus, dict_boards_all
