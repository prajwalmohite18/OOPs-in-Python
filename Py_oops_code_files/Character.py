# Exercise 30: Character Class with Auto Level-Up Logic

class Character:
    def __init__(self,name, health):
        self.name = name
        self.health = health
        self.exp = 0
        self.level = 1

    def gain_exp(self, amount):
        if amount > 0 and isinstance(amount, (int, float)):
            if self.exp + amount < 100:
                self.exp += amount 
                print(f'{self.name} gained {amount} exp. (Total:{self.exp})')

            else:           
                level_up = (self.exp+amount)// 100 # logic to increment to many level_ups
                rem_exp = (self.exp+amount)%100 # remaining exp, after self.exp = 100 
                self.level += level_up
                self.exp = rem_exp
                print(f'{self.name} gained {amount} exp.Level Up! Now Level {self.level}. (Remaining exp: {rem_exp})')
        else:
            print('Enter a valid gain exp')

ch_Cj = Character('Cj', 100)
ch_Micheal = Character('Micheal', 100)

ch_Cj.gain_exp(60)
ch_Cj.gain_exp(60)

ch_Micheal.gain_exp(50)
ch_Micheal.gain_exp(460)