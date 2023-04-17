# def sumOfDigits1(a, sum=0):
#     # base 
#     if a<10:
#         return a+sum
#     # rec 
#     rem = a %10
#     div = int(a/10)
#     sum = sum +rem
#     return sumOfDigits1(div, sum)
# def sumOfDigits2(a):
#     # base 
#     if a<10:
#         return a
#     # rec 
#     rem = a %10
#     div = int(a/10)
#     return rem + sumOfDigits2(div)

# print(sumOfDigits1(23468))
# print(sumOfDigits2(23468))

def arraySum(arr, sum=0):
    # base 
    if len(arr)==0:
        return 
    # rec
    sum+= arr[0]
    arraySum(arr[1:], sum)
    elem = arr[0]
    arr[0] = sum-elem
    return arr
    # # base 2
    # if len(arr)==4:
    #     return arr

arr = [2, 5, 7, 12]
res = [24, 21, 19, 14]
print(sum(arr))
print([sum(arr)-val for val in arr])
# test = Test()
# print(arraySum(arr))
