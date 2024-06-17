def add(a, b):
    return a + b

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python app.py <num1> <num2>")
    else:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print(f"The sum of {num1} and {num2} is {add(num1, num2)}")
