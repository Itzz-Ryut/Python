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
def verifyAge(age):
    if age > 18:
        return True
    False

age = int(input("Enter age: "))
verify = verifyAge(age)
if verify:
    print("Eligible")
else:
    print("Not eligible")

# Question 3: Calculate electricity bill based on units consumed.
# Input: Enter units
# Output: Total bill amount
def electricityBill(n):
    costs = n * 8
    return costs

unit = int(input("Enter units: "))
print("Total bill amount: ", electricityBill(unit))

# Question 4: Print all even numbers between 1 to N.
# Input: Enter N
# Output: Even numbers list
def evenNum(n):
    evenNumber = []
    for i in range(1, n+1):
        if i  % 2 == 0:
            evenNumber.append(i)
    return evenNumber

num = int(input("Enter N "))
print("Even number list ", evenNum(num))