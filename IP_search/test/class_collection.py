import subprocess
from multiping import MultiPing

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
        f = open('ip rtcomm.txt', 'r')
        line = f.readline()
        ip_rtkomm = []
        while line:
            line = line.replace("\n", "")       # удаление символа отступа в строке
            ip_rtkomm.append (line)                 # добавление в список iparr
            line = f.readline()                 # чтение следующей строки
        f.close()

        if proverka in ip_rtkomm:
            t_rt = 1
        else:
            t_rt = 0

        return t_rt
