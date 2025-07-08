char = input("Enter a character")

if len(char) == 1:
    ascii_value = ord(char)
    print("The ascii value of entered character is:" ,ascii_value)
else:
    print("Please enter a single character")