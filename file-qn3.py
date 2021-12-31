f=open("file-qn3.txt","w")
banks_list = ["Kotak", "HDFC", "RBI", "SBI", "Bank of Baroda"]
i=0
while i<len(banks_list):
    f.write(banks_list[i])
    f.write("\n")
    print(banks_list[i])
    i+=1
f.close()