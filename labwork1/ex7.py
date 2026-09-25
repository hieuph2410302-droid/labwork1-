def remove_dollar_sign(s):
    new_string = ""
    for char in s:
        if char != '$':
            new_string = new_string + char
    return new_string


result = remove_dollar_sign("The value is $100")

print(result)