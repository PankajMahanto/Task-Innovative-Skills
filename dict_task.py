"""
Problem 1: The "User Login Tracker" (Initialization & Updates)
The Scenario: You are managing a server. You have a dictionary where the Key is the username and the Value is the number of times they have logged in.
The Task: 1. Create a dictionary login_counts with 3 existing users.
2. Write a function record_login(user_dict, username) that:
- Checks if the user exists.
- If they exist, increment their count by 1.
- If they are new, add them to the dictionary with a count of 1 using .setdefault() or a standard assignment.
3. Update the dictionary with a batch of new users using .update().

login_counts = {"admin": 5, "dev_user": 12, "guest_1": 1}
"""
# task1
# login_counts = {"admin": 5, "dev_user": 12, "guest_1": 1}
# for x in login_counts:
#     print(type(x),x)
# value = login_counts.get('admin')
# value+=1
# print(value)
# print(login_counts)

# task2
# def record_login(user_d, user_name):
#     flag=1
#     for x in user_d:
#         if x == user_name:
#             v = user_d.get(x)
#             v+=1
#             user_d[x]=v
#             flag=0
#     if flag:
#         user_d.setdefault(user_name,1)
            
#     return user_d


# user=input("Enter your user_name: ")
# new_log = record_login(login_counts,user)
# print(f'new updated login_counts: {new_log} and user name: {user}')

# # task 3
# def batch_user(arr,x):
#     arr.update(x)
#     return arr
# batch = {'pankaj':5,'joy':3,'arya':7}

# new_log = batch_user(login_counts,batch)
# print(f'new updated login_counts: {new_log} and batch users: {batch}')


"""
Problem 2: The "Menu Optimizer" (Deletion & Extraction)
The Scenario: You are managing a digital cafe menu. The dictionary contains item_name: price.
The Task:Given a dictionary of 5 items, use a for loop and .items() to print the menu in a clean format.The cafe is removing items that cost more than $10.
Use a loop to find those expensive items and remove them using the del keyword or .pop()                         
menu = { "Espresso": 3.50, "Latte": 4.50, "Gold_Flake_Coffee": 50.00, "Sandwich": 8.00, "Luxury_Truffle": 25.00 }

"""

remove_item = 10 # more than $10
menu = { "Espresso": 3.50, "Latte": 4.50, "Gold_Flake_Coffee": 50.00, "Sandwich": 8.00, "Luxury_Truffle": 25.00 }

for x in menu.items():
    # print(x,type(x))
    print(f'{x[0]}: ${x[1]:.2f}')
print("\n\n")
# Remove item more than 10 dollar
arr = list(menu.items())
# print(f'arr type: {type(arr)} value: {arr}')
expensive_items={}
for x in range(len(arr)-1,-1,-1):
    # print(f'arr[x][1]: {arr[x][1]}')
    if arr[x][1] > remove_item:
        expensive_items.update({arr[x]})
        del arr[x]

print(f'Remove expensive items: {expensive_items}')    
print(f'Update menu list: {dict(arr)}')

