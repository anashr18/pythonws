arr = [[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]
def flatten(arr):
    resultArr = []
    for item in arr:
        if type(item) is list:
            resultArr.extend(flatten(item))
        else:
            resultArr.append(item)
    return resultArr
print(flatten(arr))

# def isOdd(n):
#     if n%2 ==0:
#         return False
#     return True
# arr = [12,4,4]
# def someRecursive(arr, cb):
#     if len(arr)==0:
#         return False
#     if not(cb(arr[0])):
#         return someRecursive(arr[1:], cb)
#     else:
#         return True

# print(someRecursive(arr, isOdd))
# def isPalindrome(name):
#     if len(name)==0:
#         return True
#     if name[0]!=name[-1]:
#         return False
#     return isPalindrome(name[1:-1])

# print(isPalindrome("tacocat"))
# print(isPalindrome("amanaplanacanalpanama"))
# print(isPalindrome("amanaplanacanalpandemonium"))

# def reverse(name):
#     if len(name)==0:
#         return ""
#     return  reverse(name[1:]) + name[0]
# print(reverse("YUG"))
# def recursiveRange(n):
#     if n==0:
#         return 0
#     return n + recursiveRange(n-1)
# print(recursiveRange(3))
# arr = [12,3,4]
# def prodOfArr(arr):
#    if len(arr)==0:
#       return 1
#    return arr[0] * prodOfArr(arr[1:])
    
# print(prodOfArr(arr))
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))
# def toBinary(n):
#     # print("hhh")
#     # print(n)
#     # print(n%2)
#     if n==0:
#         return 0
#     else:
#         return (n%2) + 10*toBinary(int(n/2))

# print(toBinary(13))
# def GCD(a, b):
#     # Euclidean theorem 
#     assert int(a)==a and int(b)==b, "Only integers are allowed"
#     if a<0:
#         a*=(-1)
#     if b<0:
#         b*=(-1)
#     if b==0:
#         return a
#     return GCD(b, a%b)

# print(GCD(18,49))

# def power(x, n):
    # assert int(n)==n, "exponent must be integer"
    # if n==0:
    #     return 1
    # else:
    #     return x*power(x, n-1)

# print(power(5.3,5))


# def digitsSum(n):
    # assert n>=0 and int(n)==n, "number has to be positive integer"
    # if n==0:
    #     return 0
    # else:
    #     return n%10 + digitsSum(int(n/10))
    
# print(digitsSum(1993))

# def factorial(n):
    # if (n==0):
    #     return 1;
    # else:
    #     return n*factorial(n-1);

# def fibonacci(n):
    # if n==0:
    #     return 0;
    # elif n==1:
    #     return 1;
    # else:
    #     return fibonacci(n-1) + fibonacci(n-2)

# print(factorial(6))
# print(fibonacci(7))