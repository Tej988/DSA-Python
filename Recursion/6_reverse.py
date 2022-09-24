"""
Write a recursive function called reverse which accepts a string and returns a new string in reverse.

Examples

reverse('python') # 'nohtyp'
reverse('appmillers') # 'srellimppa'
"""


def reverse(strng):
    if len(strng) <= 1:
        return strng
    return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])


print(reverse('python'))  # 'nohtyp'
print(reverse('appmillers'))  # 'srellimppa'
