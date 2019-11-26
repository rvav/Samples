import subprocess

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
    result=subprocess.call(["ping", "-n", "3", iparr[x]])
    if result == 0:
        iparr[x] =iparr[x] + " active"
    else :
        iparr[x] =iparr[x] + " Inactive"
    
    x+=1
    print (result)
del x


f = open('address_out.txt', 'w')
x = 0
while x < l:
    
    f.write (iparr[x] + "\n")
    x+=1
f.close()
del x
