try:
    print("inside try")
    num1= int(input(" Enter the first number: "))
    num2= int(input(" Enter the second number: "))
    total = num1 / num2
    print("The division is ", total)
except:
    print("inside except block")
try:
    print("inside try")
    num1= int(input(" Enter the first number: "))
    num2= int(input(" Enter the second number: "))
    total = num1 + num2
    print("The addition is ", total)
finally:
    print("inside finally")