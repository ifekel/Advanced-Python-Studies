# Finding the smallest or largest N items
import heapq

nums = [1, 2, 44, 53, 23, 1, 11, 9, 34, 67, 20]
print(heapq.nlargest(5, nums))
print(heapq.nsmallest(5, nums))

portfolio = [
    {'name': "IBM", 'shares':100, 'prices':91.9},
    {'name': "AAPL", 'shares': 50, 'prices': 543.22},
    {'name': "FB", 'shares': 200, 'prices': 21.09},
    {'name': "YAHOO", 'shares':45, 'prices':16.35},
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['prices'])
print(cheap)
