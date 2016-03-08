def print_invalid():
    os.system('cls')
    print "Input is invalid! Try again!"
    print "Enter hh.mm "
    return

import os
print "Enter hh.mm "
while True:
    input = raw_input()
    minutes_hours = input.split(".")

    if len(minutes_hours) != 2:
        print_invalid()
        continue
    if len(minutes_hours.__getitem__(0)) > 2 or len(minutes_hours.__getitem__(0)) == 0:
        print_invalid()
        continue
    elif len(minutes_hours.__getitem__(1)) > 2 or len(minutes_hours.__getitem__(1)) == 0:
        print_invalid()
        continue

    hours = 0
    minutes = 0
    try:
        hours = int(minutes_hours.__getitem__(0))
    except ValueError:
        print_invalid()
        continue

    try:
        minutes = int(minutes_hours.__getitem__(1))
    except ValueError:
        print_invalid()
        continue
    if hours > 23 or hours < 0:
        print_invalid()
        continue
    elif minutes > 59 or minutes < 0:
        print_invalid()
        continue
    else:
        print str(hours)+ "." + str(minutes) + " equals to " + str(60 * hours + minutes) + " minutes"
        break