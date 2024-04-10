class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def _hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for idx, value in enumerate(self.data_map):
            print(f"idx: {idx}, hash:{hash(idx)}, value:{value}")
            pass

    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        pass

    def get_item(self, key):
        if self.data_map is None:
            return None
        index = self._hash(key)
        lists = self.data_map[index]
        if lists:
            for singleList in lists:
                if key == singleList[0]:
                    return singleList[1]
        return None

    def keys(self):
        all_keys = []
        for idx, value_lists in enumerate(self.data_map):
            if value_lists:
                for single in value_lists:
                    all_keys.append(single[0])
        return all_keys
        pass


def item_in_common(list1, list2):
    temp = {value: "" for value in list1}
    for item in list2:
        if item in temp.keys():
            return True
    return False
    pass


def find_duplicates(num):
    temp = {}
    for item in num:
        temp[item] = temp.get(item, 0) + 1
    return [key for key, count in temp.items() if count > 1]
    pass


def first_non_repeating_char(string):
    temp = {}
    for char in string:
        temp[char] = temp.get(char, 0) + 1
    for char in string:
        if temp[char] == 1:
            return char
    return None
    pass
