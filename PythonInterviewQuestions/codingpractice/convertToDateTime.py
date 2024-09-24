import datetime
import time

current_date_string = '2024-09-03 16:47:05'

date_obj=datetime.datetime.strptime(current_date_string,'%Y-%m-%d %H:%M:%S')

# time.sleep(5)
# print(date_obj)

ls=[i for i in range(10)]
print(ls)

dt = {key:value for key,value in 'iterable'}