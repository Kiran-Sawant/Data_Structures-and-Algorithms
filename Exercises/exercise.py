
def smaller_one(array1:list, array2:list)->list:

    if len(array1) > len(array2):
        return (array2, array1)     # (small, big)
    else:
        return (array1, array2)

def commonOne(array1:list, array2:list)->bool:
    """Time Complexity: O(n*m)"""
    parse_array = smaller_one(array1, array2)

    for i in parse_array[0]:
        if i in parse_array[1]:
            return True
    return False


def commonOne2(array1:list, array2:list)->bool:
    """Time complexity: O(n+m)"""
    hash_table = dict()
    
    for i, value in enumerate(array1):
        hash_table[value] = i

    for j in array2:
        if j in hash_table:
            return True
    return False

array_one = "a b c x".split(' ')
array_two = "z y i".split(' ')
array_three = "z v x".split(' ')

# print(commonOne(array_two, array_three))

print(commonOne2(array_two, array_three))