import random

def input_collect():
    try:
        value = int(input("$:Enter number between 1-100 "))
        if value > 0 and value < 101:
            return value
        else:
            return "OutOfRange"
        
    except ValueError:
        return "ValueError"
    
def guessing(value):
    real_value = random.randint(1,100)
    if real_value == value:
        return f"You guess the right number {real_value}"
    else:
        return f"You guess the wrong number,{real_value} is real number,the distance is {abs(real_value-value)}"
    
key_values = input_collect()

if key_values == "OutOfRange":
    print("Out of range 1-100!")
elif key_values == "ValueError":
    print("Enter integer only!")
else:
    print(guessing(key_values))