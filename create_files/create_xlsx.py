from imports import *

drop_columns = ['Торговая сессия',
                'Средневзвешенная цена предыдущего дня, % к номиналу',
                'Последняя цена пред. дня',
                'Размер лота',
                'Режим торгов',
                'Точность',
                'Официальная цена закрытия предыдущего дня',
                'Признаваемая котировка предыдущего дня',
                'Рынок',
                'Группа инструментов',
                'Дата, к кот.рассч.доходность',
                'ISIN',
                'Англ. наименование',
                'Регистрационный номер',
                'Сопр. валюта инструмента',
                'Тип ценной бумаги',
                'Дата расчетов',
                'Объем лучшей котировки на покупку, штук',
                'Спрос',
                'Объем лучшей котировки на продажу, штук',
                'Предложение',
                'Совокупный спрос',
                'Первая, %',
                'Минимум, %',
                'Максимум, %',
                'Цена посл., %',
                'Изменение',
                'Объем последней, лотов',
                'Объем последней, руб.',
                'Объем последней, дол. США',
                'Ср.взвеш.',
                'Изменение к средневзвешенной цене',
                'Изменение срвзв. к срвзв. пред. дня, %',
                'Изменение срвзв. к срвзв. пред. дня',
                'Закрытие',
                'Рыночная цена пред. дня',
                'Количество сделок',
                'Объем в бумагах',
                'Объем сделок, дол. США',
                'Состояние сессии',
                'Время обновления',
                'Заявок на покупку',
                'Заявок на продажу',
                'Время последней',
                'Наибольшая цена спроса',
                'Наименьшая цена предложения',
                'Спрос сессии',
                'Предложение сессии',
                'Цена закрытия',
                'Рыночная цена 2',
                'Призн. котир., %',
                'Цена предторгового периода',
                'Номер обновления (служебное поле)',
                'Время загрузки',
                'Объем, руб.',
                'Вмененная ставка',
                'BEI',
                'Вмененная Банка России',
                'Доходность к оферте',
                'Маркер КБД',
                'Тип даты, к кот. расч. пар.',
                'Z-spread',
                'G-spread',
                'Вмененная Руония',
                'Вмененная инфляция',
                'Доходность по оценке пред. дня',
                'Дюрация cр.взвеш.']


def clear_dict(dict):  # доделать очистку дублей в словаре
    new_dict = {}
    n = 0
    for key_n in new_dict.keys():
        for key in dict.keys():
            if new_dict[key_n] == dict(key):
                pass

    return dict  # поменять на new_dict когда допишу


def xls_file(dict, filename, sort=None, drop1=None, pogash=None, period=None, for_buy=[], date_coupon=None):
    """ Сохранение результата в ексель файл с сортировкой по доходности
    drop1 - листинг
    pogash - период погашения """
    #dict = clear_dict(dict) # доделать очистку от дублей в словаре
    df = pd.DataFrame(dict)
    data_in_file = df.transpose()
    data_in_file = data_in_file.reindex(sorted(data_in_file.columns), axis=1)
    columns = data_in_file.columns.tolist()
    drop_col = [x for x in columns if x in drop_columns]
    data_in_file = data_in_file.drop(columns=drop_col)
    if sort != None:
        print(f'Сортируем {sort}')
        data_in_file[sort].astype('float')
        data_in_file = data_in_file.sort_values(by=sort, ascending=False)
    if drop1 != None:
        print(f'фильтруем {drop1}')
        data_in_file = data_in_file[data_in_file['Уровень листинга'].values == drop1]
    if period != None:
        print(f'Фильтруем период {period}')
        data_in_file = data_in_file[data_in_file['Длительность купона'].values <= period]
    if for_buy != []:
        drop_col2 = [x for x in columns if x in for_buy]
        data_in_file = data_in_file.drop(columns=drop_col2)
    if date_coupon != None:
        data_in_file['Дата окончания купона'].replace('0000-00-00', np.nan, inplace=True)
        data_in_file['Дата погашения'].replace('0000-00-00', np.nan, inplace=True)
        data_in_file.dropna(subset=['Дата окончания купона'], inplace=True)
        data_in_file.dropna(subset=['Дата погашения'], inplace=True)
        data_in_file['Дата окончания купона'].astype('datetime64')
        data_in_file['Дата погашения'].astype('datetime64')
        data_in_file = data_in_file.sort_values(by=['Дата окончания купона','Дата погашения'], ascending=True)
    data_in_file.to_excel(filename, sheet_name='operation', index=False)
    print(f'Создание файла {filename} завершено')





def do_excel(dict_RGBI, dict_all, dict_list_1, dict_indexes):
    list_buy = ['Валюта номинала',
                'Изменение доходности',
                'Рыночная цена',
                'Дата оферты',
                'Дата последних торгов',
                'Дата, к кот.рассч.дох.',
                'Длительность купона',
                'Доходность для последнего купона',
                'Доходность по закрытию',
                'Доходность по срвзв.',
                'Эффективная доходность',
                'Дюрация',
                'Измен., % ном',
                'Изменение к послдн. цене пред. дня, %',
                'Изменение последней, %',
                'К оценке пред. дня',
                'Код инструмента',
                'Код режима',
                'Короткое имя',
                'Кратк. наим.',
                'Мин. шаг цены',
                'Непог.долг',
                'Общий объем на продажу',
                'Объем в валюте',
                'Объем в обращении',
                'Объем выпуска, штук',
                'Примечание',
                'Сектор',
                'Спред',
                'Статус',
                'Цена',
                'Цена оферты',
                'тикер']

    for index in dict_RGBI.keys():
        if len(dict_RGBI[index][1].keys()) > 7:
            print(index)
            xls_file(dict_RGBI[index], filename=f'files/{dict_indexes[index]}-f.xlsx', for_buy=list_buy, date_coupon=True)
        #xls_file_index(dict_RGBI, 'files/RGBI-full-доходность последней сделки.xlsx', sort='Доходность пслд.сделки')
        #xls_file_index(dict_RGBI, 'files/RGBI-full-доходность последней сделки_на покупку.xlsx', sort='Доходность пслд.сделки', for_buy=list_buy)
        #xls_file_index(dict_RGBI, 'files/RGBI-full-эффективная доходность.xlsx', sort='Эффективная доходность')
        #xls_file_index(dict_RGBI, 'files/RGBI-full-эффективная доходность_на покупку.xlsx', sort='Эффективная доходность', for_buy=list_buy)
    print()
    xls_file(dict_list_1,filename='files/_list1.xlsx', for_buy=list_buy, date_coupon=True)
    xls_file(dict_all, filename='files/все облигации-full.xlsx', for_buy=list_buy, date_coupon=True)
    #xls_file(dict_all, 'files/облигации-full-доходность последней сделки.xlsx', sort='Доходность пслд.сделки')
    #xls_file(dict_all, 'files/облигации-full-эффективная доходность.xlsx', sort='Эффективная доходность')
    #xls_file(dict_all, 'files/облигации-листинг 1-эффективная доходность.xlsx', sort='Эффективная доходность', drop1=1, for_buy=list_buy)
    #xls_file(dict_all, 'files/облигации-листинг 1-период до 91 дня-эффективная доходность.xlsx', sort='Эффективная доходность', drop1=1, period=91, for_buy=list_buy)
    #xls_file(dict_all, 'files/облигации-листинг 1-период до 31 дня-эффективная доходность.xlsx', sort='Эффективная доходность', drop1=1, period=31, for_buy=list_buy)
    #xls_file(dict_all,'files/все_облагации_купон_full.xlsx','Сумма купона, в валюте номинала','1')
    #xls_file(dict_all,'files/все_облагации_погашение_full.xlsx','Дней до погашения','1')
