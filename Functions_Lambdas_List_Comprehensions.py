'''
Task Date: 10 Jan
Problem 1: The "Price Tagger"
The Challenge: You are given a list of product prices. You need to write a function that takes this list and a "Discount Percentage." Inside the function, use a list comprehension to create a new list where each price is reduced by that percentage.

prices = [100, 250, 400, 50]

'''
prices =[100,250,400,50,100.5,500.85]
discount_rate=15

'''
HOW WORK THE PROCESS?
100 TK  OF LOSS = 15TK
1   TK  OF LOSS = 15/100 TK
250 TK  OF LOSS = (15 * 250)/100 TK
                = 37.5 TK
FINAL DISCOUNT PRICE = ( 250 - 37.5) TK
                     = 215.5 TK
'''
def discount_percentage(priceslist,rate):
    reduce_price = [price - ((rate*price)/100) for price in priceslist]
    return reduce_price

final_price_reduce_by_percentage = discount_percentage(prices,discount_rate)

print(f"\n\nTask One")
print("====================")
print(f"\nOriginal prices: {prices}")
print(f"Discount rate use: {discount_rate}%")
print(f"Final Reduce price using discount rate: {final_price_reduce_by_percentage}")

final = [round(x,2) for x in final_price_reduce_by_percentage]
print(f"final discount update price with two decimal point: {final}")




"""
Problem 2: The "Short Word" Filter
The Challenge: You have a list of words. Some are long, some are short.Create a Lambda function that checks if a word has more than 3 letters (returns True or False).
Use a List Comprehension and that Lambda to create a new list containing only the "Long Words."

words = ["hi", "python", "is", "cool", "code", "a"]
"""

words = ["hi", "python", "is", "cool", "code", "a","elephant","great","apple"]

is_long = lambda word : len(word) > 3

long_words = [word for word in words if is_long(word)]

# Print the original and the new list to verify
print("\n\nTask two")
print("====================")
print(f"Original words: {words}")
print(f"Long words (more than 3 letters): {long_words}")
