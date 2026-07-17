"""
Old Jolly:
Mountaintop 1, FI-99999 Korvatunturi :: 555-1234567
"""

def tupleprint(data):
    part1, part2, part3 = data
    print(part1 + ":")
    print(part2 + " :: " + part3)

name = "Old Jolly"
address = "Mountaintop 1, FI-99999 Korvatunturi"
phone = "555-1234567"

datatuple = (name, address, phone)

tupleprint(datatuple)

#