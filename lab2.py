print("----------------------")

# begin user input
# print "Enter price of food: $"
price = float(input("Enter price of food: $"))

# print "Enter tax rate in percent (e.g. .08 for 8%):"
taxRate = float(input("Enter tax rate in percent (e.g. .08 for 8%):"))
# end of user input


# compute tax and total
tax = price * taxRate
total = price + tax

# output final numbers
print("Tax on food is $" + str(tax))
print("Total price is $" + str(total))
