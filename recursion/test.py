

# def power(x, n):
    assert int(n)==n, "exponent must be integer"
    if n==0:
        return 1
    else:
        return x*power(x, n-1)

# print(power(5.3,5))


# def digitsSum(n):
    assert n>=0 and int(n)==n, "number has to be positive integer"
    if n==0:
        return 0
    else:
        return n%10 + digitsSum(int(n/10))
    
# print(digitsSum(1993))

# def factorial(n):
    if (n==0):
        return 1;
    else:
        return n*factorial(n-1);

# def fibonacci(n):
    if n==0:
        return 0;
    elif n==1:
        return 1;
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(factorial(6))
# print(fibonacci(7))