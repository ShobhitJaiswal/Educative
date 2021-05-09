def fibonacci(n):
    ls=[]
    if n<=0 or n==1:
        print("value must be greater than 0 and 1")
    # elif n==2:
    #     print("1")
    else:
        a=0
        b=1
        ls=[a,b]
        while b<n-1:
            a,b=b,a+b
            # print(b)
            if b<a+b:
                ls.append(b)
        print(ls)
    return ls
x=int(input())
fibonacci(x)