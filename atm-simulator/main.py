class ATM():
    def __init__(self):
        self.DataBase = {}

    def new_user(self,user_name,pin_num,money):
        self.DataBase[user_name] = { "pin_num":pin_num
                                    ,"money":money
                                    ,"history":[]
                                    }
        
    def view_user(self):
        return self.DataBase
    
    def withdraw(self,values,user_name):
        self.DataBase[user_name]["history"].append(f"User withdraw {values} , Old remaining {self.DataBase[user_name]['money']} , New remaining {self.DataBase[user_name]['money'] - values} ")
        self.DataBase[user_name]["money"] -= values
        
    def deposit(self,values,user_name):
        self.DataBase[user_name]["history"].append(f"User deposit {values} , Old remaining {self.DataBase[user_name]['money']} , New remaining {self.DataBase[user_name]['money'] + values} ")
        self.DataBase[user_name]["money"] += values

    def authenticate(self,pin_num,user_name):
        if user_name in self.DataBase.keys():
            if self.DataBase[user_name]["pin_num"] == pin_num:
                return True
            else:
                return False
        else:
            return False
        
ATM_1 = ATM()

while True:
    key = str(input("$: ")).strip().lower()
    if key == "add new user":
        user_name = str(input("$: Enter user name "))
        try:
            pin_num = int(input("$: Enter 4 digit number "))
        except ValueError:
            print("Enter only the number")
            continue
        pin_num = str(pin_num)
        if len(pin_num) != 4 :
            print("Please enter 4 digit")
            continue
        money = float(input("$: Enter user monney "))
        ATM_1.new_user(user_name,pin_num,money)
    elif key == "view user":
        print(ATM_1.view_user())
    elif key == "deposit":
        user_name = str(input("$: Enter User Name "))
        pin_num = str(input("$: Enter User pin "))
        if ATM_1.authenticate(pin_num,user_name) == True:
            values = float(input("$: Enter deposit money "))
            ATM_1.deposit(values,user_name)
        else:
            print("wrong username or pin")
            continue
    elif key == "withdraw":
        user_name = str(input("$: Enter User Name "))
        pin_num = str(input("$: Enter User pin "))
        if ATM_1.authenticate(pin_num,user_name) == True:
            values = float(input("$: Enter withdraw money "))
            ATM_1.withdraw(values,user_name)
        else:
            print("wrong username or pin")
            continue
    elif key == "exit":
        break
    else:
        print("$: Enter the right command")

    

