rooms = {"IF101": "Lab 1", "IF102": "R. 204", "IF103": "R. 301"}
codes = input("Course codes: ").split()
 
for code in codes:
    room = rooms.get(code)
    if room is not None:
        print(code, "->", room)
    else:
        print(code, "-> not found")
