
class test_rtcomm:

    f = open('ip rtcomm.txt', 'r')
    line = f.readline()
    ip_rtkomm = []
    while line:
        line = line.replace("\n", "")       # удаление символа отступа в строке
        ip_rtkomm.append (line)                 # добавление в список iparr
        line = f.readline()                 # чтение следующей строки
    f.close()

    if iparr[x] in ip_rtkomm:
        print(iparr[x] + ' Yes')
