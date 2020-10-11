from collections import Counter

str = 'In the example below, a string is passed to Counter. It returns dictionary format, with key/value pair where the key is the element and value is the count. It also considers space as an element and gives the count of spaces in the string.'

count = Counter(str).most_common(10)
print(count)