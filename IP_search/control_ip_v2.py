import xlrd
import xlwt
import re
import subprocess
import datetime
from xlutils.copy import copy

iparr = []
data_begin = []
number = []
terr = []
device = []
location = []
while True:
    file_name = input("Введите имя файла с инцидентами выгруженного из ЦБР 2.0:")
    try:
        workbook = xlrd.open_workbook("./" + file_name)        # загрузка файла в память
        break
    except:
        print("\n\nВведено не правильное имя файла или файл находится в другой папке.")

sheet = workbook.sheet_by_index(0)                    # загрузка страницы в память
#workbook_wt = copy(workbook)
#wt_sheet = workbook_wt.get_sheet(0)

def cell (row, col):
    return (sheet.cell (row, col).value)
true_row = 0                #Счетчик подсчета открытых инцидентов
row = 0                     #Счетчик подсчета инцидентов
for row in range(sheet.nrows):
    result = re.search('\d+\.\d+\.\d+\.\d+ ', cell (row, 16))
    data_result = str(cell(row, 13))
    number_result = str(cell(row, 1))
    terr_result = str(cell(row, 12))
    loc = re.search('оборудование:\n.*?#', cell (row, 16))
    dev = re.search('\d+\.\d+\.\d+\.\d+ .*?$', cell (row, 16))
    control = re.search('Managed Object', cell (row, 16))
    control_2 = re.search('Закрыт', cell (row, 18))
    if control and not control_2:
        data_begin.append(data_result)
        number.append(number_result)
        terr.append(terr_result)
        iparr.append(result.group(0))
        location.append(loc.group(0))
        device.append(dev.group(0))
        true_row += 1
    row+=1
print(sheet.nrows)
x = 0
while x < true_row:
    iparr[x] = iparr[x].replace(' ', '')
    pings = subprocess.call(["ping", "-n", "1", iparr[x]])
    if pings == 0:
        iparr[x] =iparr[x] + "|" + "active"
    else :
        iparr[x] =iparr[x] + "|" + "Inactive"
    print (iparr[x], "    ", x+1, "---",true_row)
    x+=1

file_output = 'cbr_' + datetime.datetime.now().strftime("%d-%m-%Y") + '.txt'
f = open(file_output, 'w')
x = 0
f.write ("Номер инцидента" + "|" + "Дата начала аварии"+ "|" + "IP адрес" + "|" + "Статус" + "|" + "Территория" + "|" + "Адрес" + "|" + "Оборудование" + "\n")
while x < true_row:
    location[x] = location[x].replace('оборудование:\n', '')
    location[x] = location[x].replace('#', '')
    device[x] = re.sub('\d+\.\d+\.\d+\.\d+ ', '', device[x])
    f.write (number[x] + "|" + data_begin[x] + "|" + iparr[x] + "|" + terr[x] + "|" + location[x] + "|" + device[x] + "\n")
    x+=1
f.close()
del x
print("\nОбработанная информация записана в файл", file_output )
input("\nНажмите любую клавищу ENTER ...")
#    row+=1
#wt_sheet.write(row, 17, 'looked')
#print (control.group(0))
#workbook_wt.save("./061118.xlsx")

