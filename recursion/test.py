obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}
 
def collectStrings(obj):
    result = []
    for key in obj:
        if type(obj[key]) is dict:
            result = result + collectStrings(obj[key])
        elif type(obj[key]) is str:
            result.append(obj[key])
    return result
print(collectStrings(obj))
# def collectStrings(obj, result=[]):
#     # result = []
#     for key in obj:
#         if type(obj[key]) is dict:
#             collectStrings(obj[key])
#         elif type(obj[key]) is str:
#             result.append(obj[key])
#     return result
# print(collectStrings(obj))
# obj = {
#   "num": 1,
#   "test": [1,2,3,4],
#   "data": {
#     "val": 4,
#     "info": {
#       "isRight": True,
#       "random": 66
#     }
#   }
# }
 
# def stringifyNumbers(obj):
#     for key in obj:
#         if type(obj[key]) is dict:
#             stringifyNumbers(obj[key])
#         elif type(obj[key]) is int:
#             obj[key] = str(obj[key])
#         elif type(obj[key]) is list:
#             obj[key] = list(map(str, obj[key]))
#     return obj
        
# print(stringifyNumbers(obj))

# words = ['i', 'am', 'learning', 'recursion']
# def capitalizeWords(words):
#     if len(words)==0:
#         return []
#     result = []
#     result.append(words[0].upper())
#     return result + capitalizeWords(words[1:])
# print(capitalizeWords(words))
# def capitalizeWords(words, result=[]):
#     if len(words)==0:
#         return []
#     # result = []
#     result.append(words[0].upper())
#     capitalizeWords(words[1:])
#     return result
# print(capitalizeWords(words))
# obj1 = {
#   "outer": 2,
#   "obj": {
#     "inner": 2,
#     "otherObj": {
#       "superInner": 2,
#       "notANumber": True,
#       "alsoNotANumber": "yup"
#     }
#   }
# }
# obj2 = {
#   "a": 2,
#   "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
#   "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
#   "d": 1,
#   "e": {"e": {"e": 2}, "ee": 'car'}
# }
obj3 = {
#   "a": 2,
    "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}}
#   "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
#   "d": 1,
#   "e": {"e": {"e": 2}, "ee": 'car'}
}
# def nestedEvenSum(obj, sum=0):
#     print("first", sum)
#     for key in obj:
#         print("in for", sum)
#         if type(obj[key]) is dict:
#             sum += nestedEvenSum(obj[key])
#         elif type(obj[key]) is int and obj[key]%2==0:
#             sum += obj[key]
#     return sum 

# nestedEvenSum(obj1)
# print(nestedEvenSum(obj3))

# arr = ['car', 'taco', 'banana']
# def capitalizeFirst(arr):
#     result = []
#     if len(arr)==0:
#         return result
#     # for item in arr:
#     result.append(arr[0][0].upper()+arr[0][1:])
#     return result +(capitalizeFirst(arr[1:]))

# print(capitalizeFirst(arr))
# arr = [[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]
# def flatten(arr):
#     resultArr = []
#     for item in arr:
#         if type(item) is list:
#             resultArr.extend(flatten(item))
#         else:
#             resultArr.append(item)
#     return resultArr
# print(flatten(arr))

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