print( "\033c\033[40;37m\give the file ini to show ? ")
a=input()
f1=open(a,"r")
b=f1.read()
f1.close()
a=a.replace("/","_").replace("\\","_").replace(".","_")
a="/"+a
print(a)
c=b.split("[")
for z in c:
    z=z.strip()
    if z!="":
        x=z.split("]")
        print(a+"/"+x[0])
        if len(x)>1:
            y=x[1].strip()
            w=y.split("\n")
            for n in w:
                n=n.strip()
                if n!="":
                    m=n.split("=")
                    print(a+"/"+x[0]+"/"+m[0])
                    if len(m)>1:
                        o=m[1].strip()
                        q=o.split(";")
                        counter=0
                        for g in q:
                            g=g.strip()
                            if g!="":
                                print("            "+"["+str(counter)+"]"+g)
                                counter=counter+1