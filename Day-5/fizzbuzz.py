#Write your code below this row 👇

for num in range(1,101):
    if num % 3 == 0 and num % 15 != 0:
        print("Fizz")
    
    elif num % 5 == 0 and num % 15 != 0:
        print("Buzz")

    elif num % 15 == 0:
        print("FizzBuzz")
    
    else:
        print(num)