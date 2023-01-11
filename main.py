#Defining all the functions

def add(a, b):
  sum = a + b
  return sum

def subtact(a, b):
  diff = a - b
  return diff

def multiply(a, b):
  prod = a * b
  return prod

def divide(a, b):
  div = a / b
  return div

#creating operations dict

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide

}

#creating variables

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

operation_symbol = input("What operation do you want to do? Enter '+' for Addition, '-' for subtraction, '*', for Multiplication and '/' for Division")