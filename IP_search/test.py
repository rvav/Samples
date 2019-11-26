import xlrd
import xlwt
import re
import subprocess
from xlutils.copy import copy

iparr = []
data_begin = []
number = []
terr = []
pro = ""
workbook = xlrd.open_workbook("./061118.xlsx")
sheet = workbook.sheet_by_index(0)
#workbook_wt = copy(workbook)
#wt_sheet = workbook_wt.get_sheet(0)

def cell (row, col):
    return (sheet.cell (row, col).value)
row = 4                     #Счетчик подсчета инцидентов
i = 0
for row in range(sheet.nrows):
#    print (re.search('оборудование:\n.*?#', cell (row, 16)).group(0))
#    print (cell (row, 16))
#    result = re.search('\d+\.\d+\.\d+\.\d+ ', cell (row, 16))
    result = re.search('\d+\.\d+\.\d+\.\d+ .*?$', cell (row, 16))
    if result:
        iparr.append(result.group(0))
#        iparr[row] = iparr[row].replace("оборудование:\n", "")
#        iparr[row] = iparr[row].replace("#", "")
#        print (iparr(0))
#        print (result.group(0))
    row += 1
iparr[1] = re.sub('\d+\.\d+\.\d+\.\d+ ', '', iparr[1])
#iparr[0] = iparr[0].replace('#', '')
print (iparr[1])

