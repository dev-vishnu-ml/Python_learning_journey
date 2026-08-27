#practice poly morphism
class TV:
    def power_button(self):
        print("Tv is on")

class AC:
    def power_button(self):
        print("AC is on ")

def power_function(device):
    device.power_button()

tv = TV()
ac = AC()

power_function(tv)
power_function(ac)
