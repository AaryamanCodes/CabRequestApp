import datetime

served = ["DELHI", "JAIPUR"]
slots = ["MORNING", "AFTERNOON", "EVENING", "NIGHT"]
riderequests = []

def Request(time):
    name = input("Enter the student name: ")
    if name == "q" or name == "Q":
        print("Quitting")
        return
    while True:
        dest = input("Enter the destination (Delhi or Jaipur): ").upper()
        if dest == "q" or dest == "Q":
            print("Quitting")
            return
        if dest in served:
            break
        else:
            print("Enter a valid destination")
    while True:
        slot = input("Enter the slot (Morning, Afternoon, Evening or Night): ").upper()
        if slot == "q" or slot == "Q":
            print("Quitting")
            return
        if slot in slots:
            break
        else:
            print("Enter a valid slot")
    while True:
        year = input("Enter the year the student is studying in: ")
        if year == "q" or year == "Q":
            print("Quitting")
            return
        try:
            year = int(year)
            if 1 <= year <= 5:
                break
            else:
                print("Enter a number between 1 and 5")
        except ValueError:
            print("Invalid input")

    riderequests.append(RideRequest(name, dest, slot, year, time))
    
    
    
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
        if self.year > 5 or self.year < 1:
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
                   "Q: Quit the app at any time").upper()    
    if action == "R":
        time = datetime.datetime.now()
        Request(time)
    
    elif action == "V":
        pass
    elif action == "Q":
        break
    else:
        continue