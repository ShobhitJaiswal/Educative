def fizzbuzz(n):
    # print(n)
    new_ls=["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(n)]
    print(new_ls)
"""
    for i in range(n):
        # print(i) 
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue
        elif i % 3 == 0 :
            print("Fizz")
            continue
        elif i % 5 == 0:
            print("Buzz")
            continue
        else:
            print(i)
"""

fizzbuzz(50)