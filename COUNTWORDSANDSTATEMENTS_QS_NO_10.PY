def count_words_and_statements(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

            num_words = len(content.split())
            num_statements = content.count('.') + content.count('!') + content.count('?')

            print('Number of words:', num_words)
            print('Number of statements:', num_statements)

    except FileNotFoundError:
        print("File not found. Please check the file path.")



# output:
# EXAMPLE:
# This is a simple test. How many words are there? Let's find out! It should work well.
# 'Number of words     :13
# 'Number of statements:4

