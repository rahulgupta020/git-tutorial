

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b


def main(a,b):
    print("main function")
    
    add_result = add(a,b)
    print("add_result = ", add_result)

    sub_result = add(a,b)
    print("sub_result = ", sub_result)

    mul_result = mul(a,b)
    print("mul_result = ", mul_result)

if __name__ == '__main__':
    a=10
    b=5
    main(a=a, b=b)
    