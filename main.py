

def main(a,b):
    print("main function")
    
    add_result = add(a,b)
    print("add_result = ", add_result)

    sub_result = sub(a,b)
    print("sub_result = ", sub_result)

    mul_result = mul(a,b)
    print("mul_result = ", mul_result)

    div_result = div(a,b)
    print("div_result = ", div_result)

    modulo_result = mod(a,b)
    print("modulo_result = ", modulo_result)


if __name__ == '__main__':
    a=10
    b=5
    main(a=a, b=b)
    