def count(string, substring):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

def rindex(string, substring):
    for i in range(len(string) - 1, -1, -1):
        if string[i:i+len(substring)] == substring:
            return i
    return -1

def rsplit(string, separator):
    result = []
    current = ""
    for char in reversed(string):
        if char == separator:
            result.append(current)
            current = ""
        else:
            current = char + current
    result.append(current)
    return list(reversed(result))

def rfind(string, substring):
    for i in range(len(string) - 1, -1, -1):
        if string[i:i+len(substring)] == substring:
            return i
    return -1

def replace(string, old, new):
    result = ""
    i = 0
    while i < len(string):
        if string[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += string[i]
            i += 1
    return result

string = input("Enter a string:")
substring = input("Enter a substring:")

print(count(string, substring)) 
print(rindex(string, substring))  
print(rsplit(string, " ")) 
print(rfind(string, substring))  
print(replace(string, "hello", "hi"))  
