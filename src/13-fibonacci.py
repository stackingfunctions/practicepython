
def getUserInput():
    return int(input("\nGive me the requested number: "))

def fib(n):
    a, b = 0, 1
    counter = 0
    while counter <= n:
        print(a if a != 0 else "", end=' ')
        a, b = b, a + b
        counter += 1
    print()

if __name__ == "__main__":
    fib(getUserInput())
