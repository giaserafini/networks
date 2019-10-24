import random

print (random.randint(a,b))
print ("Please define an action to perform")
operator=char(input("Please input the character"))
print("The operation you have chosen is", operator)
def math():
    if operator == "A":
     return a % b
    elif operator == "D":
        return a+b
    elif operator == "M":
        return a*b