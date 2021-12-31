f=open("file_question4.txt","r")
lines=f.readlines()
for i in lines:
    if  "delhi" in i:
        k=open("fdelhi.txt","a")
        k.write(i)
        print(k)
        k.close()
    elif "shimla" in i:
        b=open("fshimla.txt","a")
        b.write(i)
        print(b)
    else:
        c=open("fothers.txt","a")
        c.write(i)
        print(c)