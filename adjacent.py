def stockpairs(stocks,target):
    #print(stocks)
    #print(target)
    a=set()
    b=set()
    #print(a)
    #print(b)
    for i in stocks:
        #print("==="*30)
        c=target-i
        #print(str(target)+"-"+str(i),c)
        if c in b:
            #print(str(c)+" in "+str(b))
            #print("if "+str(i)+"is greater than "+str(c)+"then"+str(i)+","+str(c)+" else "+str(c)+str(i))
            res=(i,c) if (i>c) else (c,i)
            #print(res)
            if res not in a:
                #print(str(res)+"not present in "+str(a))
                a.add(res)
        b.add(i)
        #print(a)
        #print(b)
    #print("==="*30)
    return len(a)

print(stockpairs([5,7,9,13,11,6,6,3,3],12))


filename='shyari.txt'
f=open(filename,'r')
print(len(f.read().splitlines()))
line=f.read().splitlines()
for i in range(len(line)):
    print(line[i])
f.close()
