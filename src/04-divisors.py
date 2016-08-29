num = int(input("Enter a number: "))

for i in range(num):
    if i < (num / 2):
        if num % (i + 1) == 0:
            print("%d is divisable by %d" % (num, i + 1))


