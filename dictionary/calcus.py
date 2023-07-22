# Calculator

def add(n1, n2):  # this function adds n1 and n2
    return n1 + n2


def subtract(n1, n2):  # this function subtract n2 from n1
    return n1 - n2


def multiply(n1, n2):  # this function multiplies n1 by n2
    return n1 * n2


def divide(n1, n2):  # this function divides n1 by n2
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = float(input("Enetr first number : "))
print("OPERATIONAL SIGNS")
for operator in operations:
    print(operator)

select_operator = input("Choose an operator from the list above: ")
num2 = float(input("Enter second number: "))

calcus_function = operations[select_operator]
result = calcus_function(num1, num2)
print(result)
