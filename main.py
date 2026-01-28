#Write a program that prints the first 1000 numbers of FizzBuzz. Output should look like this:
#```
#1
#2
#Fizz
#4
#Buzz
#Fizz
#7
#8
#Fizz
#```
#**However, it should continue on up to 1000.**
#**Remember: case matters!** This project will be automatically graded, and computers are very literal!
for number in range(1, 1001):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
