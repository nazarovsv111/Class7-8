def check_empty_string(input_string):
    if input_string == "":  # Check if the string is empty
        return "The string is empty!"
    else:
        return f"The string is not empty. It contains: '{input_string}'"


# Test the function
print(check_empty_string(""))  # Testing with an empty string
print(check_empty_string("Hello World"))  # Testing with a non-empty string
