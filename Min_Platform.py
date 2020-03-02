def min_platform(arrivals, departures):
    arrivals.sort()
    departures.sort()
    platforms = [{"platformNumber":1,"arrivalTime":None,"departureTime":None, "is_empty":True}]
    arriving_train = 0
    departing_train = 0
    while arriving_train < len(arrivals) and departing_train < len(arrivals):
        if arriving_train == 0:
            platforms[0]["platformNumber"] = 1
            platforms[0]["arrivalTime"] = arrivals[0]
            platforms[0]["departureTime"] = departures[0]
            platforms[0]["is_empty"] = False
            arriving_train += 1
        elif  arrivals[arriving_train] < departures[departing_train]:
            platform = get_empty_platform(platforms)
            if platform:
                for i in range(len(platforms)):
                    if platforms[i]["platformNumber"] == platform:
                        platforms[i]["arrivalTime"] = arrivals[arriving_train]
                        platforms[i]["departureTime"] = departures[arriving_train]
                        platforms[i]["is_empty"] = False
            else:
                platformNumber = len(platforms)+1
                platforms.append({"platformNumber":platformNumber, "arrivalTime":arrivals[arriving_train],"departureTime":departures[arriving_train], "is_empty":False})
            arriving_train += 1
        elif arrivals[arriving_train] >= departures[departing_train]:
            #deleting data for departing train
            platforms[departing_train]["is_empty"] = True
            platforms[departing_train]["platformNumber"] = None
            platforms[departing_train]["arrivalTime"] = None
            platforms[departing_train]["departureTime"] = None
            # addind data for arriving train
            platform = get_empty_platform(platforms)
            if platform:
                for i in range(len(platforms)):
                    if platforms[i]["platformNumber"] == platform:
                        platforms[i]["arrivalTime"] = arrivals[arriving_train]
                        platforms[i]["departureTime"] = departures[arriving_train]
                        platforms[i]["is_empty"] = False
            else:
                platformNumber = len(platforms)+1
                platforms.append({"platformNumber":platformNumber, "arrivalTime":arrivals[arriving_train],"departureTime":departures[arriving_train], "is_empty":False})
            
            arriving_train +=1
            departing_train +=1
    print(platforms)
    count = 0
    for i in range(len(platforms)):
        if platforms[i]["is_empty"] == False:
            count+=1
    
    return count

def get_empty_platform(platforms):
    for p in range(len(platforms)):
        if platforms[p]["is_empty"] == True:
            return platforms[p]["platformNumber"]
    return None


arrivals = [200, 210, 300, 320, 350, 500]
departures = [230, 340, 320, 430, 400, 520]

print("Pass" if min_platform(arrivals, departures) == 2 else "Fail")

arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

print("Pass" if min_platform(arrivals, departures) == 3 else "Fail")

print(min_platform(arrivals, departures))
