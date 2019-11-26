import xlrd
import xlwt
import re
import subprocess
import datetime
from xlutils.copy import copy
from class_collection import pingtest

iparr = []
data_begin = []
number = []
terr = []
device = []
location = []
iparrs = []
zagruzka = []
#столбцы в выгрузке
opsanie = 15
stk = 11
nachalo = 12
status  = 17

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
    result = re.search('\d+\.\d+\.\d+\.\d+', cell (row, opsanie))
    data_result = str(cell(row, nachalo))
    number_result = str(cell(row, 1))
    terr_result = str(cell(row, stk))
    zagr = re.search('Абонентов \- ФЛ \(\d+\) ЮЛ \(\d+\)', cell (row, opsanie))
    loc = re.search('оборудование:\n.*?#', cell (row, opsanie))
    dev = re.search('\d+\.\d+\.\d+\.\d+ .*?$', cell (row, opsanie))
    control = re.search('Managed Object', cell (row, opsanie))
    control_2 = re.search('Закрыт', cell (row, status))
    if control and not control_2:
        data_begin.append(data_result)
        number.append(number_result)
        terr.append(terr_result)
        iparr.append(result.group(0))
        location.append(loc.group(0))
        device.append(dev.group(0))
        if zagr:
            zagruzka.append(zagr.group(0))
        else:
            zagruzka.append(zagr)
        true_row += 1
    row+=1

x = 0
while x < true_row:
    result = 0
    ito = 0
    schetchik = 0
    while schetchik < 2:
        result_pred = pingtest.ping(iparr[x])
        result = result + result_pred
        schetchik += 1
    ito = result / 2    
    if ito > -1:
        iparrs.append("Da")
    else :
        iparrs.append("Net")

    print (iparr[x], "  " , iparrs[x] , "    ", x+1, "---", true_row, "result:", ito)
    x+=1
    
del x

file_output = 'cbr_' + datetime.datetime.now().strftime("%d-%m-%Y") + '.txt'
f = open(file_output, 'w')
x = 0
f.write ("Номер инцидента" + "|" + "Дата начала аварии"+ "|" + "IP адрес" + "|"  + "Территория" + "|" + "Адрес" + "|" + "Оборудование" + "\n")
while x < true_row:
    location[x] = location[x].replace('оборудование:\n', '')
    location[x] = location[x].replace('#', '')
    device[x] = re.sub('\d+\.\d+\.\d+\.\d+ ', '', device[x])
    f.write (number[x] + "|" + data_begin[x] + "|" + iparr[x] + "|" + terr[x] + "|" + location[x] + "|" + device[x] + "\n")
    if pingtest.test_rtcomm(iparr[x]): 
        device[x] = "rtcomm " + device[x]
        location[x] = location[x] + ' c.' + pingtest.test_rtcomm(iparr[x])
    x+=1
f.close()
del x

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, "Номер инцидента")
ws.write(0, 1, "Дата начала аварии")
ws.write(0, 2, "IP адрес")
ws.write(0, 3, "Статус")
ws.write(0, 4, "Территория")
ws.write(0, 5, "Адрес")
ws.write(0, 6, "Оборудование")

x = 0
while x < true_row:
    ws.write(x+1, 0, number[x])
    ws.write(x+1, 1, data_begin[x])
    ws.write(x+1, 2, iparr[x])
    ws.write(x+1, 3, iparrs[x])
    ws.write(x+1, 4, terr[x])
    ws.write(x+1, 5, location[x])
    ws.write(x+1, 6, device[x])
    ws.write(x+1, 7, zagruzka[x])
    x+=1
del x

file_output_exel = 'cbr_' + datetime.datetime.now().strftime("%d-%m-%Y") + '.xls'
wb.save(file_output_exel)

print("\nОбработанная информация записана в файл", file_output_exel)
input("\nДля завершения нажмите клавищу ENTER ...")
#    row+=1
#wt_sheet.write(row, 17, 'looked')
#print (control.group(0))
#workbook_wt.save("./061118.xlsx")

