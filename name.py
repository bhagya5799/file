f=open("bh.txt","r")
lines=f.readlines()
for i in lines:
    if "bhagya" in i:
        k=open("fbhagya .txt","a")
        k.write(i)
        print(k)
        k.close()
    elif "vinni" in i:
        b=open("fvinni","a")
        b.write(i)
        print(b)