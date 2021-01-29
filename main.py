

#some functions of our project

#add
def add(num1, num2):
  return num1 + num2 

#subst
def substract(num1, num2):
  return num1 - num2

#multiply
def multiply(num1, num2):
  return num1 * num2

#division
def division(num1, num2):
  return num1 / num2

#storing functions in the dictionnary

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": division
}

n1 = int(input("What is the first number?: "))
n2 = int(input("What is the second number?: "))

#loop through the dictionnary
for symbol in operations:
  print(symbol)

#operations symbol 
operation_symbol = input("Pick an operation from the line above:")

calculation_function = operations[operation_symbol]
answer = calculation_function(n1, n2)


print(f"{n1} {operation_symbol} {n2} = {answer}" )






