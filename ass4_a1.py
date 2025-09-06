#Write a recursive function which print string in reverse order.

def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])

text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))
