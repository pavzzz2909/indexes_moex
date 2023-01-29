from imports import *

from MOEX.get_boards import get_boards
from MOEX.get_columns_board import get_dict_columns
from MOEX.get_marketdata_board import get_marketdata_board
from MOEX.rgbi_index import get_indexes, get_index_info

from create_files.create_xlsx import do_excel


def mk_dir(dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)


mk_dir('files/')

time_start = datetime.now()
dict_boards_T_plus, dict_boards_all = get_boards()
list_indexes, dict_indexes = get_indexes()  # получаем все индексы Мосбиржи
# pprint(dict_indexes)
# list_indexes=['RGBI']
dict_RGBI = get_index_info(list_indexes)
# pprint(dict_RGBI)
dict_all = {}
for board in dict_boards_T_plus.keys():
    dict_columns = get_dict_columns(board)
    dict_RGBI, dict_all = get_marketdata_board(dict_columns, dict_RGBI, dict_all, dict_boards_T_plus[board]['board'])

dict_new_all = {}

for k, v in dict_all.items():
    if v['secid'] not in dict_new_all.keys():
        dict_new_all[v['secid']] = v

dict_alls = {}
n = 1
for i in dict_new_all.keys():
    if 'Доходность пслд.сделки' in dict_new_all[i].keys():
        if dict_new_all[i]['Доходность пслд.сделки'] > 0:
            dict_alls[n] = dict_new_all[i]
            n += 1

dict_list_1 = {}
n = 1
for i in dict_alls.keys():
    if dict_alls[i]['Уровень листинга'] == 1:
        dict_list_1[n] = dict_alls[i]
        n += 1


do_excel(dict_RGBI, dict_alls, dict_list_1, dict_indexes)
print('Формирование файлов завершено')
time_end = datetime.now()
print(f'Время работы скрипта составило:  {time_end - time_start}')
