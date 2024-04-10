from icecream import ic


def group_anagrams(strings):
    anagram = {}
    for string in strings:
        count_key = [0] * 26
        for char in string:
            count_key[ord(char) - ord("a")] += 1
        ic(count_key)
        key = tuple(count_key)
        if key not in anagram:
            anagram[key] = [string]
        else:
            anagram[key].append(string)
    ic(anagram.values())
    pass


# strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
# group_anagrams(strings)


def two_sum(nums, target):
    num_to_index = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return num_to_index[complement], idx
        num_to_index[num] = idx
    return None
    pass


# print(two_sum([5, 1, 7, 2, 9, 3], 10))
# print(two_sum([4, 2, 11, 7, 6, 3], 9))
# print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
# print(two_sum([1, 3, 5, 7, 9], 10))


def subarray_sum(nums, target):
    running_sum_index = {0: -1}
    running_sum = 0
    for idx, num in enumerate(nums):
        running_sum += num
        complement_sum = running_sum - target
        if complement_sum in running_sum_index:
            return [running_sum_index[complement_sum] + 1, idx]
        running_sum_index[running_sum] = idx
    pass


# nums = [1, 2, 3, 4, 5]
# target = 9
# print(subarray_sum(nums, target))

# nums = [-1, 2, 3, -4, 5]
# target = 0
# print(subarray_sum(nums, target))

# nums = [2, 3, 4, 5, 6]
# target = 3
# print(subarray_sum(nums, target))

# nums = []
# target = 0
# print(subarray_sum(nums, target))


def remove_duplicates(my_list):
    my_set = set()
    for num in my_list:
        my_set.add(num)
    return list(my_set)
    pass


# my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
# new_list = remove_duplicates(my_list)
# print(new_list)


def has_unique_chars(string):
    my_set = set()
    for char in string:
        if char in my_set:
            return False
        my_set.add(char)
    return True
    pass


print(has_unique_chars("abcdefg"))  # should return True
print(has_unique_chars("hello"))  # should return False
