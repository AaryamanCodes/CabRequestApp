served = ["Delhi", "Jaipur"]
slots = ["Morning", "Afternoon", "Evening", "Night"]
while True:
    action = input("What would you like to do? \n" 
                   "V: View available cabs \n" 
                   "R: Request a cab \n" 
                   "Q: Quit the app").upper()    
    if action == "R":
        pass
    if action == "V":
        pass
    if action == "Q":
        break

class RideRequest:
    def __init__(self, name, dest, slot, year, time):
        self.name = name
        self.dest = dest
        self.slot = slot
        self.year = year
        self.time = time

"""
    def valid(self):
        if self.year > 4:
            return False
        elif self.dest not in served:
            return False
        elif self.slot not in slots:
            return False
        else:
            return True
"""        

class Cab:
    def __init__(self, name, seats, left, dest, slist):
        self.name = name
        self.dest = dest
        self.seats = seats
        self.left = left
        self.slist = slist


"""
    def valid(self):
        if self.dest not in served:
            return False
        elif self.slot not in slots:
            return False
        else:
            return True
"""