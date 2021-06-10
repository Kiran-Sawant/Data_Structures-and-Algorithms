"""Find the first recurring number from the array"""

def firstRecurringCharacter(array:list)->str:
    
    for i in range(len(array)):
        cache = []
        cache.append(array[i])
        for j in range(i+1, len(array)):
            if array[j] in cache:
                return f"element {array[j]} at index {j}"
            else:
                cache.append(array[j])
                continue

array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
array2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
array3 = [0, 0, 8, 7, 4, 6]

print(firstRecurringCharacter(array3))
