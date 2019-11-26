import subprocess
from multiping import MultiPing
import xlrd
import xlwt
import re
from xlutils.copy import copy

class pingtest:
    def ping(host, n = 0):
        if(n>0):
            avg = 0
            for i in range (n):
                avg += ping(host)
            avg = avg/n
        # Create a MultiPing object to test hosts / addresses
        mp = MultiPing([host])

        # Send the pings to those addresses
        mp.send()

        # With a 1 second timout, wait for responses (may return sooner if all
        # results are received).
        responses, no_responses = mp.receive(5)


        for addr, rtt in responses.items():
            RTT = rtt


        if no_responses:
            # Sending pings once more, but just to those addresses that have not
            # responded, yet.
            mp.send()
            responses, no_responses = mp.receive(1)
            RTT = -1

        return RTT
    
    def test_rtcomm(proverka):
        workbook = xlrd.open_workbook("lpu_list.xlsx")        # загрузка файла в память
        sheet = workbook.sheet_by_index(2)                    # загрузка страницы в память
        def cell (row, col):
            return (sheet.cell (row, col).value)
        row = 0                     #Счетчик подсчета инцидентов
        true_row = 0
        this_village = ''
        for row in range(sheet.nrows):
            village = str(cell(row, 6))
            ip_kd = str(cell(row, 23))
            control = re.search('Республика Саха', cell (row, 3))
            control_2 = re.search('Якутск Покровский тракт 16 км ЗССС "Орбита"', cell (row, 16))
            if control and not control_2:
                if proverka in ip_kd:
                    this_village = village
            row+=1            
        return this_village

