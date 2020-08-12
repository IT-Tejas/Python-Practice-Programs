import time
mg=input("Type Message: ")
msg = mg
tme=input('Time Limit: ')
tme=float(tme)
for i in msg:
    print(i,end='')
    time.sleep(tme)
