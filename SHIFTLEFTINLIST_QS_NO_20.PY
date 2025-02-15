def shift_left(lst):
    if len(lst) <= 1:
        return lst
    
    return lst[1:] + [lst[0]]

input_list = [1, 2, 3,4,5]
shifted_list = shift_left(input_list)

print("Original list:", input_list)
print("List after shifting left by one position:", shifted_list)

# OUTPUT:
# Original list: [1, 2, 3, 4, 5]
# List after shifting left by one position: [2,3,4,5,1]
