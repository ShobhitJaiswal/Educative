dic = {'one':1,'two':2,'three':3}

new_dic = {key:value for key,value in zip(dic.keys(),reversed(dic.values()))}
print(new_dic)