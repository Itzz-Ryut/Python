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
price = float(input("Q1 | Enter price: "))
discount = float(input("Q1 | Enter discount %: "))
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
si = (principal * rate * time) / 100
print(f"Simple Interest: {si}")