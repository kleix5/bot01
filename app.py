# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 10:55:47 2025

@author: po
For correct work is necessary to this file to be with "jsons" directory in the
same place!

"""
import pandas as pd
import numpy as np
from tools import *
import json
import os

# протяжённость тарифных периодов согласно тарифному плану ООО "ЛОКЭЙТ"
# 0 - июнь, 1 - июль, 2 - август, 3 - сентябрь
rate_len = {0 : 11, 1 : 20, 2 : 30, 3 : 25}


jsons = os.listdir("jsons")
for i in range(len(jsons)):
    jsons[i] = "jsons/"+jsons[i] 
    



actions = {
    0 : lambda: sortvalYa(jsons[0]),
    1 : lambda: sortvalYa(jsons[1]),
    2 : lambda: sortvalYa(jsons[2]),
    3 : lambda: sortvalYa(jsons[3])
}


def file_write(file_name: str, write_flag: str, rate_num: int):
    '''
    Parameters
    ----------
    file_name : str
        ТУТ ПИШЕМ НАЗВАНИЕ ФАЙЛА КУДА БУДЕМ ЗАПИСЫВАТЬ.
    write_flag : str
        'w' - записываем с нуля; 'a' - дописываем.
    rate_num : int
        0(20.06-30.06), 1(01.07-20.07), 2(21.07-25.08), 3(26.08-20.09)

    Returns
    -------
    None.
    '''
    prices = actions[rate_num]() # обработали ya_json
    with open(file_name, write_flag,  encoding='utf-8') as f:
        print("Write the header below:")
        header = input()
        f.write(header)
        for i in prices:
            f.write(str(round(i[1]/rate_len[rate_num], 2)))
            f.write("  ")
            f.write(str(i[2]))
            f.write("  ")
            f.write(str(i[-1]))
            f.write('\n')
        f.write("\n\n")
        f.close()







'''
RATE1 = 0
RATE2 = 1
RATE3 = 2
RATE4 = 3


# ниже протяженность тарифных периодов в сезоне
LEN_RATE_1 = 11
LEN_RATE_2 = 20
LEN_RATE_3 = 30
LEN_RATE_4 = 25



# список тарифных периодов всего сезона
rates = [LEN_RATE_1, LEN_RATE_2, LEN_RATE_3, LEN_RATE_4]

# ниже json'ы по каждому тарифному периоду
feo1_json = "jsons/feo_ya_1.json"
feo2_json = "jsons/feo_ya_2.json"
feo3_json = "jsons/feo_ya_3.json"
feo4_json = "jsons/feo_ya_4.json"

feo_jsons =[feo1_json, feo2_json, feo3_json, feo4_json]


'''
# Запалняем текстовый файл в части I-го тарифного периода (июнь), указана цена
# как за весь период, так и средняя цена за ночь (вся стоимость/кол-во дней) 
'''
feo_prices_1 = sortvalYa(feo_jsons[RATE1]) # обработали ya_json

with open("answer.txt", 'w', encoding="utf-8") as f:
    f.write("ОТВЕТ ЯНДЕКСА 20.06-01.07 2026 года  (стоимость всего периода):\n\n")
    for i in feo_prices_1:
        f.write(str(i[1]))
        f.write("  ")
        f.write(str(i[2]))
        f.write("  ")
        f.write(str(i[-1]))
        f.write('\n')
    f.write("\n\n")
    f.close()


with open("answer.txt", 'a',  encoding='utf-8') as f:
    f.write("ОТВЕТ ЯНДЕКСА 20.06-01.07 2026 года (цена за 1 ночь):\n\n")
    for i in feo_prices_1:
        f.write(str(round(i[1]/rates[RATE1], 2)))
        f.write("  ")
        f.write(str(i[2]))
        f.write("  ")
        f.write(str(i[-1]))
        f.write('\n')
    f.write("\n\n")
    f.close()
    
    
'''
# Запалняем текстовый файл в части II-го тарифного периода (jul)
'''
feo_prices_2 = sortvalYa(feo_jsons[RATE2]) # обработали ya_json

with open("answer.txt", 'a', encoding="utf-8") as f:
    f.write("ОТВЕТ ЯНДЕКСА 01.07-21.07 2026 года  (стоимость всего периода):\n\n")
    for i in feo_prices_2:
        f.write(str(i[1]))
        f.write("  ")
        f.write(str(i[2]))
        f.write("  ")
        f.write(str(i[-1]))
        f.write('\n')
    f.write("\n\n")
    f.close()


with open("answer.txt", 'a',  encoding='utf-8') as f:
    f.write("ОТВЕТ ЯНДЕКСА 01.07-21.07 2026 года (цена за 1 ночь):\n\n")
    for i in feo_prices_2:
        f.write(str(round(i[1]/rates[RATE2], 2)))
        f.write("  ")
        f.write(str(i[2]))
        f.write("  ")
        f.write(str(i[-1]))
        f.write('\n')
    f.write("\n\n")
    f.close()
    
    
'''
# Запалняем текстовый файл в части III-го тарифного периода (aug) 
'''
feo_prices_3 = sortvalYa(feo_jsons[RATE3]) # обработали ya_json

with open("answer.txt", 'a', encoding="utf-8") as f:
    f.write("ОТВЕТ ЯНДЕКСА 25.07-24.08 2026 года  (стоимость всего периода):\n\n")
    for i in feo_prices_3:
        f.write(str(i[1]))
        f.write("  ")
        f.write(str(i[2]))
        f.write("  ")
        f.write(str(i[-1]))
        f.write('\n')
    f.write("\n\n")
    f.close()


with open("answer.txt", 'a',  encoding='utf-8') as f:
    f.write("ОТВЕТ ЯНДЕКСА 25.07-24.08 2026 года (цена за 1 ночь):\n\n")
    for i in feo_prices_3:
        f.write(str(round(i[1]/rates[RATE3], 2)))
        f.write("  ")
        f.write(str(i[2]))
        f.write("  ")
        f.write(str(i[-1]))
        f.write('\n')
    f.write("\n\n")
    f.close()
    
    
'''
# Запалняем текстовый файл в части IV-го тарифного периода (sep)
'''
feo_prices_4 = sortvalYa(feo_jsons[RATE4]) # обработали ya_json

with open("answer.txt", 'a', encoding="utf-8") as f:
    f.write("ОТВЕТ ЯНДЕКСА 26.08-20.09 2026 года  (стоимость всего периода):\n\n")
    for i in feo_prices_4:
        f.write(str(i[1]))
        f.write("  ")
        f.write(str(i[2]))
        f.write("  ")
        f.write(str(i[-1]))
        f.write('\n')
    f.write("\n\n")
    f.close()


with open("answer.txt", 'a',  encoding='utf-8') as f:
    f.write("ОТВЕТ ЯНДЕКСА 26.08-20.09 2026 года (цена за 1 ночь):\n\n")
    for i in feo_prices_1:
        f.write(str(round(i[1]/rates[RATE4], 2)))
        f.write("  ")
        f.write(str(i[2]))
        f.write("  ")
        f.write(str(i[-1]))
        f.write('\n')
    f.write("\n\n")
    f.close()
    
'''