str = input("Enter a string: ")

if str.lower() == str.lower()[::-1]:
    print("Palidrome")
else:
    print("Not palidrome")