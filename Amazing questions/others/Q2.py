# print a string in reverse without using loops or slicing

def rev(s, i=0):
    if i == len(s):
        return ""
    return rev(s, i + 1) + s[i]
print(rev("shivam"))