number = int(input("Give me a number and I will tellyou if it is even or odd. Your number: "))
divisor = int(input("What divisor would you like to check? "))

if number % 2 == 0:
    print("%d is EVEN" % number)
else:
    print("%d is ODD" % number)

if number % 4 == 0:
    print("%d is evenly divisible by 4." % number)

if number % divisor == 0:
    print("%d is evenly divisible by %d." % (number, divisor))



