def capitalize_file_content(filename):
   
    with open(filename, 'r') as file:
        content = file.read()    
    capitalized_content = content.upper()
 
    with open(filename, 'w') as file:
        file.write(capitalized_content)

    print(f"Content of {filename} has been capitalized.")

filename = input("Enter the name of the file to capitalize: ")
capitalize_file_content(filename)


# INPUT FILE1.TXT
# Hello, this is a sample file.
# This is another line.

# OUTPUT:
# HELLO, THIS IS A SAMPLE FILE.
# THIS IS ANOTHER LINE.


