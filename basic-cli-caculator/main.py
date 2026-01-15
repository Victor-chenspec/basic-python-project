number1 = int(input("$:Input first number "))
operator = str(input("$:Input operation such as (+) (-) (*) (/) "))
number2 = int(input("$:Input second number "))

def calculation(number1,operator,number2):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        try:
            return number1 / number2
        except ZeroDivisionError:
            return "can't divided with zero!"
    else:
        return "Please enter correct operetor!"

print(calculation(number1,operator,number2))