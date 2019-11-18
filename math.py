import random
import operator

def operation(number1, number2, operator):
        if operator == '+':
           return number1 + number2
        elif operator == '-':
            return number1 - number2
        elif operator == '%':
            return number1 % number2

#print (random.randint(a,b))

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second one: "))
operator = input("Enter the operator: ")
print (operation(number1, number2, operator))