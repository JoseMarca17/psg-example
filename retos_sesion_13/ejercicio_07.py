for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz", end=" ")
    elif i % 5 == 0:
        print("Fizz", end=" ")
    elif i % 7 == 0:
        print("Buzz", end=" ")
    else: 
        print(i, end=" ")