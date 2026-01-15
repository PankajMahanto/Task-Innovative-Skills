# Topics: String Manipulation, Tuples, List Comprehensions, and Functions
# Date : Due 13 Jan


"""
Problem 1: The "Email Validator" (Cleaning & Tuples)
The Scenario: You have a list of raw user inputs. You need to separate the Username from the Domain and return them as a "locked" pair.
The Task: Write a function process_email(email) that:Strips any whitespace.Converts it to lowercase.Splits the string at the @ symbol.Returns the result as a Tuple: (username, domain).
"""
print(f"\nProblem 1 Solved {'='*10}")
def process_email(email):
    clean_email=email.strip()
    lower_email = clean_email.lower()
    parts = lower_email.split("@")
    
    return parts[0],parts[1]
    # if len(parts) == 2:
    #     return (parts[0],parts[1])
    # else:
    #     return (None,None)
    
    

userInput ="aryanpankaj78@gmail.com"

userName,domain = process_email(userInput)

print(f"Orginal Input: {userInput}")
print(f"User Name: {userName}")
print(f"Domain Name: {domain}")


"""
Problem 2: The "Data Masker" (List Comp & Slicing)
The Scenario: You have a list of credit card numbers (strings). For security, you need to hide all numbers except the last 4.
The Task: Use a List Comprehension to take a list of 16-digit strings and turn them into "masked" versions where the first 12 digits are * and the last 4 are visible.
cards = ["1234567812345678", "9876543298765432", "1111222233334444"]
"""
print(f"\nProblem 2 Solved {'='*10}")
cards = ["1234567812345678", "9876543298765432", "1111222233334444"]
masked_cards = [ f"{"*"*12}{num[12:]}" for num in cards]

print(masked_cards)
"""
Problem 3: The "Inventory Analyzer" (Everything Combined)
The Challenge: You are given a list of product strings in this format: "itemName:Price".
Example: ["Laptop:1000", "Mouse:25", "Monitor:300"]
The Task: Write a script that:Uses a List Comprehension to turn that list into a list of Tuples: [("Laptop", 1000), ...]. (Hint: You'll need to split(":") and convert the price to an int).
Uses the max() and min() functions on the prices to find the most expensive and cheapest items.

raw_inventory = ["Laptop:1000", "Mouse:25", "Monitor:300", "Keyboard:50"]
"""
print(f"\nProblem 3 Solved {'='*10}")
raw_inventory = ["Laptop:1000", "Mouse:25", "Monitor:300", "Keyboard:50"]

raw_tuple = [tuple(x.split(":"))  for x in raw_inventory]
print(raw_tuple)

raw_tuple2 = [(x[0],int(x[1])) for x in raw_tuple]
print(raw_tuple2)
# print(raw_tuple2[0][1])

# print(f"\n\n{'*'*12}")
prices = [num[1] for num in raw_tuple2]
print(f"prices: {prices}")
print(f"most expensive price:{max(prices)}")
print(f"most cheapest price:{min(prices)}")

# print(f"\n\n{'*'*12}")
items  = [num[0] for num in raw_tuple2]
print(f"items: {items}")

expensive_item = max(raw_tuple2, key = lambda x : x[1])
print(f"expensive_item: {expensive_item}")
print(f"Expensive items tuple: {expensive_item[0]}")

cheapest_item = min(raw_tuple2, key = lambda x : x[1])
print(f"cheapest_item tuple: {cheapest_item}")
print(f"Cheapest items: {cheapest_item[0]}")

