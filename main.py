import datetime

served = ["Delhi", "Jaipur"]
slots = ["Morning", "Afternoon", "Evening", "Night"]

def Request(time):
    name = input("Enter the student name: ")
    dest = input("Enter the destination: ")
    slot = input("Enter the slot: ")
    year = input("Enter the year the student is in: ")
    
class RideRequest:
    def __init__(self, name, dest, slot, year, time):
        self.name = name
        self.dest = dest
        self.slot = slot
        self.year = year
        self.time = time
        self.disptime = time.strftime("%H:%M:%S %d/%m/%Y")

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

while True:
    action = input("What would you like to do? \n" 
                   "V: View available cabs \n" 
                   "R: Request a cab \n" 
                   "Q: Quit the app").upper()    
    if action == "R":
        time = datetime.datetime.now()
        Request(time)
    
    if action == "V":
        pass
    if action == "Q":
        break