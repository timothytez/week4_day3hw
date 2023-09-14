# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.

# Don't forget the space after the closing parentheses!




create_phone_number = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


def phone_number(alist):
    alist[0]
    
    return f'({alist[0]}{alist[1]}{alist[2]}) {alist[3]}{alist[4]}{alist[5]}{alist[6]}'

print(phone_number(create_phone_number))

