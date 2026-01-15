import random

class r_p_c():
    def __init__(self):
        self.moveset = {0:"paper",1:"scissors",2:"rock"}
        self.bot_move = 0

    def play(self,plr_move):
        self.bot_move = random.randint(0,2)
  
        match plr_move:
            case 0:
                match self.bot_move:
                    case 0:
                        return f"tie with {self.moveset[plr_move]} Vs {self.moveset[self.bot_move]}"
                    case 1:
                        return f"lose to bot with {self.moveset[plr_move]} Vs {self.moveset[self.bot_move]}"
                    case 2:
                        return f"win to bot with {self.moveset[plr_move]} Vs {self.moveset[self.bot_move]}"
            case 1:
                match self.bot_move:
                    case 0:
                        return f"win to bot with {self.moveset[plr_move]} Vs {self.moveset[self.bot_move]}"
                    case 1:
                        return f"tie with {self.moveset[plr_move]} Vs {self.moveset[self.bot_move]}"
                    case 2:
                        return f"lose to bot with {self.moveset[plr_move]} Vs {self.moveset[self.bot_move]}"
            case 2:
                match self.bot_move:
                    case 0:
                        return f"lose to bot with {self.moveset[plr_move]} Vs {self.moveset[self.bot_move]}"
                    case 1:
                        return f"win to bot with {self.moveset[plr_move]} Vs {self.moveset[self.bot_move]}"
                    case 2:
                        return f"tie with {self.moveset[plr_move]} Vs {self.moveset[self.bot_move]}"

r_p_c = r_p_c()

while True:
    try:
        move = int(input("$: 0=paper,1=scissors,2=rock,3 to exit "))
    except ValueError:
        print('Enter only number!')
        continue
    if move > -1 and move < 3:
        print(r_p_c.play(move))
    elif move == 3:
        break
    else:
        print("out of range!")