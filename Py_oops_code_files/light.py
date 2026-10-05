# Exercise 7: Light Class with On/Off State Toggle
class Light():

    def __init__(self):
        self.is_on = False
   
    def turn_on(self):
        self.is_on = True
        print('Light is ON')

    def turn_off(self):
        self.is_on = False
        print('Light is OFF')

    def status(self):
        state = 'ON' if self.is_on else 'OFF'
        print('Current Status:', state)

lamp1 = Light()
lamp1.status()
lamp1.turn_on()
lamp1.status()
lamp1.turn_off()
lamp1.status()
