

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

#getting the first number
n1 = int(input("What is the first number?: "))

#loop through the dictionnary
for symbol in operations:
  print(symbol)

#operations symbol 
operation_symbol = input("Pick an operation from the line above:")

#getting the second number
n2 = int(input("What is the second number?: "))

calculation_function = operations[operation_symbol]
first_answer = calculation_function(n1, n2)


print(f"{n1} {operation_symbol} {n2} = {first_answer}" )

#making another operation
operation_symbol = input("Pick another operation:")

n3 = int(input("What is the next number?: "))


operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operation_symbol]

second_answer = calculation_function(calculation_function(n1, n2), n3)

print(f"{first_answer} {operation_symbol} {n3} = {second_answer}" )







