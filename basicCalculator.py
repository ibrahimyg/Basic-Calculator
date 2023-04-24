print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")

userChoice =  input("Input your choice:")

def sum(firstValue , secondValue):
    resultSum = firstValue + secondValue
    print("Your sum result is" , resultSum)
def sub(firstValue , secondValue):
    resultSub = firstValue - secondValue
    print("Your subtract result is" , resultSub)
def mul(firstValue , secondValue):
    resultMul = firstValue * secondValue
    print("Your multiplication result is" , resultMul)
def div(firstValue , secondValue):
    resultDiv = firstValue / secondValue
    print("Your divide result is" , resultDiv)

if (userChoice == "a" or userChoice == "A" ):
    first = int(input("Input your first number:"))
    second = int(input("Input your second number:"))
    sum(first , second)
elif (userChoice == "b" or userChoice == "B" ):
    first = int(input("Input your first number:"))
    second = int(input("Input your second number:"))
    sub(first , second)
elif (userChoice == "c" or userChoice == "C" ):
    first = int(input("Input your first number:"))
    second = int(input("Input your second number:"))
    mul(first , second)
elif (userChoice == "d" or userChoice == "D" ):
    first = int(input("Input your first number:"))
    second = int(input("Input your second number:"))
    div(first , second)
elif (userChoice == "e" or userChoice == "E"):
    exit()
else:
    print("Please only use given letters")
    
