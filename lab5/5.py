#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
def r(text):
    return re.sub('[ ,.]', ':', text)

text = input()
print(r(text))