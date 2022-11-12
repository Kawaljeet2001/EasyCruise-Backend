def performSeatAllocation(totalCapacity, remCapacity, cabinClass, numberOfTravellers):
    allotedSeats = []

    if cabinClass == "Economy":
        seatPrefix = "E"
    elif cabinClass == "Business":
        seatPrefix = "B"
    else:
        seatPrefix = "A"
    
    startNum = totalCapacity - remCapacity

    for i in range(startNum , startNum + numberOfTravellers):
        allotedSeats.append(seatPrefix + str(i))

    print(allotedSeats)
    return allotedSeats
