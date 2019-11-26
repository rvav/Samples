
from class_collection import pingtest

f = open('address.txt', 'r')
line = f.readline()
iparr = []
while line:
    
    line = line.replace("\n", "")       # удаление символа отступа в строке
    iparr.append (line)                 # добавление в список iparr
    line = f.readline()                 # чтение следующей строки
f.close()
print (iparr)
l=len(iparr)

x = 0
while x < l:
    result = 0
    ito = 0
    schetchik = 0
    while schetchik < 2:
        result_pred = pingtest.ping(iparr[x])
        result = result + result_pred
        schetchik += 1
    ito = result / 2
    print (pingtest.test_rtcomm(iparr[x]))
    if pingtest.test_rtcomm(iparr[x]) == 1: 
        iparr[x] =iparr[x] + " rtcomm"
    if ito > -1:
        iparr[x] =iparr[x] + " Da"
    else :
        iparr[x] =iparr[x] + " net"

    print (iparr[x], ' ' , ito)
    x+=1
    
del x


f = open('address_out.txt', 'w')
x = 0
while x < l:
    
    f.write (iparr[x] + "\n")
    x+=1
f.close()
del x
