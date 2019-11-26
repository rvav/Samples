from class_collection import pingtest
ipaddress='10.220.38.98'
n=10
i=0
while i<=n:
    result_pred = pingtest.ping(ipaddress)
    print(result_pred)
    i+=1
