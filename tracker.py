# Expense Tracker | Installment 2
# Author: Jose D.C. Rebeta III
# This is a simple expense tracker program that displays a menu for users to interact with.

print("=" * 40)

print("\tEXPENSE TRACKER")
print("\tTrack your expenses easily!")

print("=" * 40)

print("MAIN MENU")

print("1. Add an expense\t(coming soon)")
print("2. View all expenses\t(coming soon)")
print("3. Show total spent\t(coming soon)")
print("4. Exit\t\t\t(coming soon)")

print("-" * 40)

name = input("Enter your name: ")
print(f"\nWelcome, {name}! Let's log two expenses.\n")

subtotal = 0

item1 = input("Enter first item: ")
amount1 = float(input("Enter amount: "))
subtotal += amount1

item2 = input("Enter second item: ")
amount2 = float(input("Enter amount: "))
subtotal += amount2

average = subtotal / 2

tax_percent = float(input("Enter tax rate %?: "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

budget = float(input("Enter your budget: "))
over_budget = total > budget
left = budget - total

print("-" * 40)
print("SUMMARY")
print(f"{item1}\t\t{amount1}")
print(f"{item2}\t\t{amount2}")
print(f"Subtotal\t{subtotal}")
print(f"Average\t\t{average}")
print(f"Tax ({tax_percent}%)\t{tax}")
print(f"Grand total\t{total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget\t{left}")

print("-" * 40)
print("Made by: Jose D.C. Rebeta III | Installment 3")
print("=" * 40)