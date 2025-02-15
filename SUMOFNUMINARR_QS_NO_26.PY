def sum_excluding_13(lst):
    total = 0
    i = 0
    while i < len(lst):
        if lst[i] == 13:
            i += 2  
        else:
            total += lst[i]
            i += 1
    return total

print(sum_excluding_13([1, 2, 3, 4])) 
print(sum_excluding_13([1, 2, 3, 4, 13]))  
print(sum_excluding_13([13, 1, 2, 3, 13]))  
print(sum_excluding_13([]))  


# Outputs:

#     For [1, 2, 3, 4], the output will be 10.
#     For [1, 2, 3, 4, 13], the output will be 10.
#     For [13, 1, 2, 3, 13], the output will be 5.
#     For an empty array [], the output will be 0.