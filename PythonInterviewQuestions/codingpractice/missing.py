ls1 = [1,2,3,5,7]

def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output
    
print(findMissingNumbers(ls1))
# ls2=findMissingNumbers(ls1)+ls1
# print(sorted(ls2))