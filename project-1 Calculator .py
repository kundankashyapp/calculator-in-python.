# Python program create a simple calculator.
# Q  3 steps to build a calculator program
#   1. Function for operation
#   2. User input    
#   3. Print Result

#create function

#function to add to numbers
def add(num1, num2):
    return num1 + num2

#funtion to substaction to numbers
def subtraction(num1, num2):
    return num1 - num2

# function to multiplication to numbers
def multiplication(num1, num2):
    return num1 * num2

# function to divide to marks
def divide(num1,num2):
    return num1 / num2

#function to agerage to number
def average(num1, num2):
    return (num1 + num2 )/2

#user input
print("Please select an operation: ")
print("1. addition")
print("2. Subtraction")
print("3. multiplication")
print("4. divide")
print("5. average ")

Select = int(input("select a operation from 1,2,3,4,5: "))

number1 =int(input("enter the first number: "))
number2 =int(input("enter the second number: "))

# step 3 print result

if Select == 1:
    print(number1, "+", number2, "=", add(number1, number2) )

elif Select == 2:
    print(number1, "-", number2, "=", subtraction(number1, number2))

elif Select == 3:
    print(number1, "*" ,number2, "=", multiplication(number1, number2))

elif Select == 4:
    print(number1, "/", number2, "=", multiplication(number1, number2))

elif Select == 5:
    print("(",number1, "+", number2,")","/","2", "=", average(number1, number2))
          
else:
    print("invalid operation! plz try again")