#The items
items = {
    "Milk" : 45,
    "Bread" : 50,
    "Egg" : 5
}

print(items)
#First thing to input
item1 = items[input("Enter your first item:  ")]

print(item1)
#Second thing to input
item2 = items[input("Enter your second item:  ")]

print(item2)
#Finding the bill
bill = item1 + item2

print(bill)
#Amount user wants to pay
amount = input("How much do you want to play:  ")

gh = int(amount)
#The change
change = gh - bill

h = str(change)
#Tells you the change
print("Your change is " + h)