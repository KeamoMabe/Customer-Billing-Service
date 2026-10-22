#syntax that requires customer's name
user_name = input("Enter customer name: ")
#syntax that requires the number of items
number_of_items = float(input("Enter number of items: "))
#syntax keeps count of the number of items purchased
item_number = 1
#variable which provides the total cost
total_bill = 0
#loop that enters item price and adds to total bill, dependent on the number of items
while number_of_items > 0:
    price = input(f"Enter price for item {item_number}: ")
    item_number += 1
    total_bill += float(price)
#Ensures number of items corresponds to the total cost of the bill
    number_of_items -= 1
#prints the total cost of customer's items
print(f"Total bill: {total_bill}")
#provides a fixed number of attempts (3) for password
attempts = 3
password = " "
#requests the cashier to provide a payment confirmation password
while password != "Shop123":
    password = input("Enter cashier password: ")
#executes when cashier enter an incorrect password
    if password != "Shop123":
        print("incorrect password")
        attempts -= 1
#keeps count of the number of attempts left
        if attempts == 0:
            print("attempts exceeded")
            break
#executes when the password is correct
    elif password == ("Shop123"):
        print("payment successful, receipt printed")
        print(f"Thank you {user_name} for shopping with us")
        break