arr = [1,2,3,4,5,9]
def twoSum(arr, sum):
    left=0
    right=len(arr)-1
    while(left < right):
        if arr[left]+arr[right]< sum:
            left+=1
        elif arr[left]+arr[right]> sum:
            right-=1
        else:
            return [arr[left], arr[right]]
    return -1
print(twoSum(arr, 9))

def findNumber(arr, num):
    
    low = 0
    high = len(arr)-1
    mid = 0
    while(low<=high):
        mid = (high+low)//2
        if arr[mid] > num:
            high = mid-1
        if arr[mid] < num:
            low = mid+1
        else:
            return arr[mid]
    return -1

print(findNumber(arr, 19))
        


# # list = [i for i in range(1,101)]
# list1 = [i for i in ([i for i in range(1,101)]) if i%90!=0]
# print(list1)
# x = lambda n: n*(n+1)/2
# print(sum)
# num = x(100)-sum(list1)
# print(num)

# numDays = int(input("How many days of temprature?"))
# tempArr = []
# total = 0
# for i in range(1, numDays+1):
#     nextDayTemp = int(input("Day "+str(i)+" temprature:"))
#     tempArr.append(nextDayTemp)
#     total+=nextDayTemp

# avg = round(total/numDays, 2)  
# # count =0
# # count1 = [1 if (i>avg) else 0 for i in tempArr]
# count = len([1 for i in tempArr if (i>avg)])

# # print(count1)
# print("Avg temprature is: "+ str(avg) +" Number of days above avg temprature: "+str(count))
