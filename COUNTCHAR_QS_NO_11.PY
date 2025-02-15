def count_char_occurrences(string, char):
    return string.count(char)

input_string = input("Enter a string: ")
character = input("Enter the character to count: ")

count = count_char_occurrences(input_string, character)
print(f"The character '{character}' appears {count} times in the string.")


# OUTPUT:
# Enter a string: hello world
# Enter the character to count: o
# The character 'o' appears 2 times in the string.

