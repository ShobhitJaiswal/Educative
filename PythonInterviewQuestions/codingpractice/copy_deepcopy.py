import copy

l=[1,2,3,[5,4]]
print(l)
l2=copy.copy(l)
l2.append(1)
l2[3][1]=7
print(l2,l)

l3=[7,8,9,[0,4,7]]
print(l3)
l4=copy.deepcopy(l3)
l4.append(6)
l4[3][1]='a'
print(l4,l3)