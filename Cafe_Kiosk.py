#Byte&Brew Tech Cafe
#Self Service Tech Cafe Kiosk
#Individual Lab
#Establish starting tab at $0.00
total_bill=0.00
total_sales=0.00

#Assign prices to each drink
#Menu items and prices
iced_latte=4.50
iced_coffee=3.50
hot_latte=4.00
hot_coffee=3.00

#Welcome user to cafe and display menu items with prices
print("Welcome to Byte & Brew Cafe! Please select your drink from the menu below:")
print("1. Iced Latte - $4.50\n2. Iced Coffee - $3.50\n3. Hot Latte - $4.00\n4. Hot Coffee - $3.00\n5. Order Complete - Checkout")

#Ask for user input to select drink one at a time
while True:
    order=input("Please enter the number of the drink you'd like to order:")
    if order=="1":
        total_bill+=iced_latte
        print("Iced Latte added to your order. Your total is now: $", total_bill)
    elif order=="2":
        total_bill+=iced_coffee
        print("Iced Coffee added to your order. Your total is now: $", total_bill)
    elif order=="3":
        total_bill+=hot_latte
        print("Hot Latte added to your order. Your total is now $", total_bill)
    elif order=="4":
        total_bill+=hot_coffee
        print("Hot Coffee added to your order. Your total is now $", total_bill)
    elif order=="5":
#Discount code prompt added in final Option before completing order
        discount=input("Do you have a discount code for today's order? Type in now or hit Enter to Proceed.")
        if discount=="Welcome10":
            total_bill=total_bill*.90
        elif discount=="5off":
            total_bill=total_bill-5.0
        print("Thank you for your order! Your total is $", total_bill)
        break
else: 
    print("Sorry, that item doesn't exist just yet. Please select a number from 1-4; or select 5 to checkout.")
#Maybecan be False statement instead?^ 

