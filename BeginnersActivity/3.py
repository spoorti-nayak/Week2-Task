def most_frequent(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    max_count = 0
    most_common = None
    for item, count in frequency.items():
        if count > max_count:
            max_count = count
            most_common = item

    return most_common

print(most_frequent([1, 2, 2, 3, 3, 3, 4]))  


# from collections import Counter

# def most_frequent(lst):
#     counter = Counter(lst)
#     return counter.most_common(1)[0][0]

# # 
# print(most_frequent([1, 2, 2, 3, 3, 3, 4]))  
