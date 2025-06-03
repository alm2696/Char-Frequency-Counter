input_string = input("Enter a string: ")

count = {}

for char in input_string:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

most_frequent = max(count, key=count.get)

print("The most frequent character is:", most_frequent)
print("It appears", count[most_frequent], "times.")