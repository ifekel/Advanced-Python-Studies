# Unpacking a sequence into variables
# Example 1
# Example 2 Unpacking a tuple
p = (1, 2, 3)
a, b, c = p
print(a)
print(b)
print(c)

# Example 2 Unpacking a list
data = ["ACME", 10, 50, (2022, 12, 21)]
name, num1, num2, date = data
print(name)
print(num1)
print(num2)
print(date)

# Example 3
# Example 2 Unpacking a string
s = "Hello"
s1, s2, s3, s4, s5 = s
print("\nUnpacking the string \"hello\"")
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

# Example 4 Picking  a throwaway name for a value
myList = ["ACME", 10, 50, (2022, 12, 21)]
__, num, _,  dDate = myList
print(num)
print(dDate)