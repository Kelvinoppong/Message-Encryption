def caesar_cipher(text, shift_value, mode):
    # Define alphabets as lists
    lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
    uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    # Adjust the shift direction based on the mode
    if mode == "decrypt":
        shift_value = -shift_value
    
    # Initialize an empty result
    result = ""

    # Process each character in the input text
    for char in text:
        if char in lowercase_letters:  # For lowercase letters
            new_position = (lowercase_letters.index(char) + shift_value) % 26
            result += lowercase_letters[new_position]
        elif char in uppercase_letters:  # For uppercase letters
            new_position = (uppercase_letters.index(char) + shift_value) % 26
            result += uppercase_letters[new_position]
        else: 
            result += char  # Non-alphabet characters remain unchanged

    return result


# Get user inputs
action = input("Do you want to 'encrypt' or 'decrypt'?\n").lower()
message = input("Enter the message:\n")
shift = int(input("Enter the shift value:\n"))

# Call the function and display the result
output = caesar_cipher(message, shift, action)
print(f"The {action}ed message is: {output}")
