

def add(a,b):
    return a+b

def main(a,b):
    print("main function")
    
    add_result = add(a,b)
    print("add_result = ", add_result)

if __name__ == '__main__':
    a=10
    b=5
    main(a=a, b=b)