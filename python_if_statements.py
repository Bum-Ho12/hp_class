num = int(input('Enter number: '))
num2 = int(input('Enter to check if number is even or odd: '))
if num>0:
    print("The number is positive")
else:
    print('The number is negative')

if num2 % 2 == 0:
    print(f"The {num2} is even")
else:
    print(f"The {num2} is odd")