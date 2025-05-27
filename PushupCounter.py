target = int(input("Enter target number of pushups: "))
day = 1
total = 0

while total < target:
    pushups = int(input("Day {}: How many pushups did you do today? ".format(day)))
    total = pushups + total
    day = day + 1
print("You did a total of {} pushups.".format(total))
print("You hit your target in {} days!".format(day-1))