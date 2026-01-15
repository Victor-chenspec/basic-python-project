def input_collect():
    try:
        values = float(input("$: Enter temperature number "))
    except ValueError:
        return None
    
    default_unit = str(input("$: Enter default unit temperature (C F K) ")).strip().upper()
    new_unit = str(input("$: Enter new unit temperature (C F K) ")).strip().upper()

    return values,default_unit,new_unit

def calculation(package):
    if package != None:
        values,default_unit,new_unit = package
    else:
        return "Enter number only!"

    if default_unit in ("C", "F", "K") and new_unit in ("C", "F", "K"):  

        #Celsius
        if default_unit == "C":
            if new_unit == "K":
                return f"{values} Celsius is {values + 273.15} Kelvin"
            elif new_unit == "F":
                return f"{values} Celsius is {((values*9)/5)+32} Farenheit"
            else:
                return "Same unit"
            
        #Kelvin
        elif default_unit == "K":
            if new_unit == "C":
                return f"{values} Kelvin is {values - 273.15} Ceslius"
            elif new_unit == "F":
                return f"{values} Kelvin is {(((values - 273.15)*9)/5)+32} Farenheit"
            else:
                return "Same unit"
            
        #Farenheit
        else:
            if new_unit == "C":
                return f"{values} Farenheit is {((values-32)*5)/9} Celsius"
            elif new_unit == "K":
                return f"{values} Farenheit is {(((values-32)*5)/9)+273.15} Kelvin"
            else:
                return "Same unit"
    else:
        return "Please enter correct temperature unit!"
    
print(calculation(input_collect()))