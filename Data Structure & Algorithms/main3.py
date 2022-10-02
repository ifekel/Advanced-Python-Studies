# Keeping the last N items
from collections import deque

# def search(lines, pattern, history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line, previous_lines
#             previous_lines.append(line)

# using the deque function
q = deque(maxlen=3)
q.append(1)
print(q)

q.append(2)
print(q)

q.append(3)
print(q)

# As the items in q increases the first item is removed to make q not more than 3
q.append(4)
print(q)

q.append(5)
print(q)