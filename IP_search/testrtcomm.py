import xlrd
import xlwt
import re
import subprocess
import datetime
from xlutils.copy import copy


workbook = xlrd.open_workbook("lpu_list.xlsx")        # загрузка файла в память

sheet = workbook.sheet_by_index(2)                    # загрузка страницы в память
proverka = '10.60.240.43'
def cell (row, col):
    return (sheet.cell (row, col).value)
row = 0                     #Счетчик подсчета инцидентов
true_row = 0
for row in range(sheet.nrows):
    village = str(cell(row, 6))
    ip_kd = str(cell(row, 23))
    control = re.search('Республика Саха', cell (row, 3))
    control_2 = re.search('Якутск Покровский тракт 16 км ЗССС "Орбита"', cell (row, 16))
    if control and not control_2:
        if proverka in ip_kd:
            t_rt = 1
            this_village = village
            print('yes')
    row+=1            
return this_village, t_rt
