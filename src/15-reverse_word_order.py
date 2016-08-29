
def reverseWordOrder(str):
    return " ".join(str.split(" ")[::-1])

if __name__ == "__main__":
    print(reverseWordOrder("Hi my name is Gergo and I like Python"))
