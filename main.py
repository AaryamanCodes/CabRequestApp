import datetime
import heapq
import csv

served = ["DELHI", "JAIPUR"]
slots = ["MORNING", "AFTERNOON", "EVENING", "NIGHT"]
waiting = {}
cabs = []

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
                print("Enter a year between 1 and 5")
        except ValueError:
            print("Enter a year between 1 and 5")

    if (dest, slot) not in waiting:
        waiting[(dest, slot)] = []
    heapq.heappush(waiting[(dest, slot)], (-year, time, RideRequest(name, dest, slot, year, time)))
    print("Request added to the waiting list")
    if FindCab(dest, slot) == None:
        print("There is no open cab for this trip right now")

def View():
    allreqs = []
    for key in waiting:
        for item in waiting[key]:
            allreqs.append((item[1], item[2]))
    allreqs.sort()
    print("\nWAITING STUDENTS")
    if len(allreqs) == 0:
        print("Nobody is waiting")
    for t, r in allreqs:
        print(f"{r.name:<20}{r.dest.title():<10}{r.slot.title():<12}Year {r.year}    {r.disptime}")
    print("\nCABS")
    for c in cabs:
        status = "Open"
        if c.left:
            status = "Left"
        print(f"{c.name:<20}{c.dest.title():<10}{c.slot.title():<12}{len(c.slist)}/{c.seats}    {status}")
        for s in c.slist:
            print("    -", s.name, "Year", s.year)

def LoadCabs():
    f = open("cabs.csv")
    for row in csv.reader(f):
        if row == [] or row[0].lower() == "driver":
            continue
        cabs.append(Cab(row[0], int(row[1]), row[2].upper(), row[3].upper()))
    f.close()

def FindCab(dest, slot):
    for c in cabs:
        if c.left == False and c.dest == dest and c.slot == slot:
            return c
    return None

def Matches():
    lines = {}
    for key in waiting:
        lines[key] = sorted(waiting[key])
    print("\nMATCHES (Seat not assginedyet )")
    for c in cabs:
        if c.left:
            continue
        line = lines.get((c.dest, c.slot), [])
        picked = line[:c.seats]
        lines[(c.dest, c.slot)] = line[c.seats:]
        print(f"{c.name} - {c.dest.title()}, {c.slot.title()} ({len(picked)}/{c.seats})")
        for item in picked:
            print("    -", item[2].name, "Year", item[2].year)

def Dispatch():
    dest = input("Enter the destination (Delhi or Jaipur): ").upper()
    slot = input("Enter the slot (Morning, Afternoon, Evening or Night): ").upper()
    if dest not in served or slot not in slots:
        print("That is not a valid destination and slot")
        return
    cab = FindCab(dest, slot)
    if cab == None:
        print("No open cab for this trip")
        return
    if (dest, slot) not in waiting or len(waiting[(dest, slot)]) == 0:
        print("Noone is waiting for this trip")
        return
    while len(cab.slist) < cab.seats and len(waiting[(dest, slot)]) > 0:
        item = heapq.heappop(waiting[(dest, slot)])
        cab.slist.append(item[2])
    cab.left = True
    print(f"{cab.name}'s cab left with {len(cab.slist)}/{cab.seats} seats used")

class RideRequest:
    def __init__(self, name, dest, slot, year, time):
        self.name = name
        self.dest = dest
        self.slot = slot
        self.year = year
        self.time = time
        self.disptime = time.strftime("%H:%M:%S %d/%m/%Y")

class Cab:
    def __init__(self, name, seats, dest, slot):
        self.name = name
        self.dest = dest
        self.slot = slot
        self.seats = seats
        self.left = False
        self.slist = []


LoadCabs()
while True:
    action = input("What would you like to do? \n"
                   "V: View waiting students and cabs \n"
                   "R: Request a cab \n"
                   "M: Find matches \n"
                   "D: Dispatch a cab \n"
                   "Q: Quit the app \n").upper()
    if action == "R":
        time = datetime.datetime.now()
        Request(time)
    elif action == "V":
        View()
    elif action == "M":
        Matches()
    elif action == "D":
        Dispatch()
    elif action == "Q":
        break
    else:
        print("Enter one of V, R, M, D or Q")