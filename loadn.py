import os
import struct
print( "\033c\033[40;37m\n ? ")
a="my.dat"
b=[]
f1=open(a,"rb")
while(1):
    try:
        r=f1.read(4)
        rr=struct.unpack("i",r)[0]
        b=b+[rr]
    except:
        break
f1.close()
print(b)