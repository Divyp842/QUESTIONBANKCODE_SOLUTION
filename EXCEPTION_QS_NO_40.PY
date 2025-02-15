def get_number():
    try:
        number = int(input("Enter a number: "))
        
        if number < 0:
            raise ValueError("The number cannot be less than zero.")
        
        print(f"You entered: {number}")
    
    except ValueError as e:
        print(f"Error: {e}")

get_number()




# OUTPUT
# Enter a number: -5
# Error: The number cannot be less than zero.

# Enter a number: 10
# You entered: 10
