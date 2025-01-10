def is_palindrome(s):
    reversed_s = s[::-1]
    return s == reversed_s

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
