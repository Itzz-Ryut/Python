# Question 1: A shopkeeper wants to calculate total bill after discount.
# Input: Enter price and discount percentage
# Output: Final price after discount
def calculate_bill(price, discount_percent):
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount
    return final_price
 
price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))
final = calculate_bill(price, discount)
print(f"Final price after discount: {final}")

# Question 2: Check whether a person is eligible to vote.
# Input: Enter age
# Output: Eligible / Not Eligible
def verify_age(age):
        return age >= 18

age = int(input("Enter age: "))
verify = verify_age(age)
if verify:
    print("Eligible")
else:
    print("Not eligible")

# Question 3: Calculate electricity bill based on units consumed.
# Input: Enter units
# Output: Total bill amount
def electricity_bill(n):
    costs = n * 8
    return costs

unit = int(input("Enter units: "))
print("Total bill amount: ", electricity_bill(unit))

# Question 4: Print all even numbers between 1 to N.
# Input: Enter N
# Output: Even numbers list
def even_num(n):
    evenNumber = []
    for i in range(1, n+1):
        if i  % 2 == 0:
            evenNumber.append(i)
    return evenNumber

num = int(input("Enter N "))
print("Even number list ", even_num(num))

# Question 5: Create a function to calculate simple interest.
# Input: Enter P, R, T
# Output: Simple Interest
def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si
 
principal = float(input("Enter Principal (P): "))
rate = float(input("Enter Rate of Interest (R): "))
time = float(input("Enter Time in years (T): "))
si = simple_interest(principal, rate, time)
print(f"Simple Interest: {si}")

# Question 6: A shopkeeper wants to calculate total bill after discount.
# Input: Enter price and discount percentage
# Output: Final price after discount
price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))
final = price - (price * discount / 100)
print(f"Final price: {final}")

# Question 7: Check whether a person is eligible to vote.
# Input: Enter age
# Output: Eligible / Not Eligible
age1 = int(input("Enter ur age "))
if age1 >= 18 :
    print("Eligible")
else:
    print("Not Eligible")


# Question 8: Calculate electricity bill based on units consumed.
# Input: Enter units
# Output: Total bill amount
unit = float(input("Enter Units "))
print("Total bll units ", unit * 8)


# Question 9: Print all even numbers between 1 to N.
# Input: Enter N
# Output: Even numbers list
num1 = int(input("ENter N"))
even_numbers1 =[]
for i in range (1, num1):
    if i % 2 == 0:
        even_numbers1.append(i)
print("Even number list ", even_numbers1)

# Question 10: Create a function to calculate simple interest.
# Input: Enter P, R, T
# Output: Simple Interest
principal1 = float(input("Enter Principal (P): "))
rate1 = float(input("Enter Rate of Interest (R): "))
time1 = float(input("Enter Time in years (T): "))
si1 = (principal1 * rate1 * time1) / 100
print("Simple Interest: {si1}")

# Question 11: A shopkeeper wants to calculate total bill after discount.
# Input: Enter price and discount percentage
# Output: Final price after discount
price2 = float(input("Enter price: "))
discount2 = float(input("Enter discount %: "))
final2 = round(price2 - (price2 * discount2 / 100))
print("Final price: {final2}")

# Question 12: Check whether a person is eligible to vote.
# Input: Enter age
# Output: Eligible / Not Eligible
age2 = int(input("Enter age: "))
result2 = "Eligible" if age2 >= 18 else "Not Eligible"
print(result2)

# Question 13: Calculate electricity bill based on units consumed.
# Input: Enter units
# Output: Total bill amount
def electricity_bill2(units):
    if units <= 100:
        return units * 2.00
    else:
        return (100 * 2.00) + ((units - 100) * 4.00)
 
units2 = int(input("Enter units "))
print(f"Total bill: ₹{electricity_bill2(units2):.2f}")

# Question 14: Print all even numbers between 1 to N.
# Input: Enter N
# Output: Even numbers list
n2 = int(input("Enter N: "))
evens2 = list(range(2, n2 + 1, 2))
print(f"Even numbers: {evens2}")

# Question 15: Create a function to calculate simple interest.
# Input: Enter P, R, T
# Output: Simple Interest
def si2(p, r, t):
    si = (p * r * t) / 100
    total = p + si
    return si, total
 
p2 = float(input("Q15 | Enter P: "))
r2 = float(input("Q15 | Enter R: "))
t2 = float(input("Q15 | Enter T: "))
si2, total2 = si2(p2, r2, t2)
print(f"Simple Interest: {si2}  |  Total Amount: {total2}")