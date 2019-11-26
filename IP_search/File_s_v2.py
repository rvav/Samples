import subprocess
from multiping import MultiPing

def ping(host,n = 0):
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
        result_pred = ping(iparr[x])
        result = result + result_pred
        schetchik += 1
    ito = result / 2    
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
