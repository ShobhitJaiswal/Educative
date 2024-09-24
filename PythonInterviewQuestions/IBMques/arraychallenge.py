def arraychallange(arr):
    n=len(arr)
    res_ls = []
    res_ls.append(0)
    for i in range(1,n):
        sum = 0
        for j in range(i):
            ele = arr[i]-arr[j]
            sum += ele
        res_ls.append(sum)
    return res_ls

print(arraychallange([2,4,3]))
print(arraychallange([2,1,3]))