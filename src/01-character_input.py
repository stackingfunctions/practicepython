import time

name = input("Enter your name: ")
age = input("Enter your age: ")
repeat = input("How many times would you like to print this message? ")

current_year = time.localtime().tm_year

born_year = current_year - int(age)

for count in range(int(repeat)):
    print("\nPrinting message #%d:" % int(count+1), "\tDear %s, you will be 100 years old in %d." % (name, born_year + 100))
