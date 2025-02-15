lst = [9, 8, 7, 6, 5, 4, 3]
print("Original list:", lst)
lst = [10] + lst
lst = lst + [2]
lst = lst[:5] + lst[6:]
print("Modified list:", lst)
print("Reversed list:")
for i in range(len(lst)-1, -1, -1):
    print(lst[i], end=" ")

# OUTPUT:
# Original list: [9, 8, 7, 6, 5, 4, 3]
# Modicfied list: [10, 9, 8, 7, 6, 4, 3, 2]
# Reversed list:
# 2 3 4 6 7 8 9 10
