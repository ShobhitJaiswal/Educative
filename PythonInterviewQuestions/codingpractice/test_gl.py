"""import requests as req
import pandas as pd

url = 'https://jsonplaceholder.typicode.com/todos/'

res = req.get(url)
json_data=res.json()
# print(res.json())

df=pd.DataFrame(json_data)
print(df)

filtered_df=df[df['id']<=5]
print(filtered_df)"""


# list1 = [2,11,7,15]
list1=[2,11,8,15,1]
target = 9

#output = 0,2

def returnIndex(ls,target):
    for i in range(len(ls)):
        if sum(ls)==target:
            return list(i)
        
print(returnIndex(list1,target))


# first_val=list1[0]
# find_val=target-first_val

# if find_val in list1:
#     print(list1.index(first_val),list1.index(find_val))
# # elif find_val+1 or find_val-1:



