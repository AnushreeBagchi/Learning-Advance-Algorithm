def min_platform(arrivals, departures):
    arrivals.sort()
    departures.sort()
    platforms = [{"platformNumber":1,"arrivalTime":None,"departureTime":None, "is_empty":True}]
    train = 0
    while train < len(arrivals):
        platform = get_empty_platform(platforms)
        if platform:
            for i in range(len(platforms)):
                if platforms[i]["platformNumber"] == platform:
                    platforms[i]["arrivalTime"] = arrivals[train]
                    platforms[platform]["departureTime"] = departures[train]
        else:
            platformNumber = len(platforms)
            platforms.append({"platformNumber":platformNumber, "arrivalTime":arrivals[train],"departureTime":arrivals[train], "is_empty":False})
        
        if train > 1 and arrivals[train] > departures[train-1]:
            previous_record = (train-1)-1
            platforms[previous_record]["is_empty"] == True
            platforms[previous_record]["platformNumber"] == None
            platforms[previous_record]["arrivalTime"] == None
            platforms[previous_record]["departureTime"] == None

        train +=1

def get_empty_platform(platforms):
    for p in range(len(platforms)):
        if platforms[p]["is_empty"] == True:
            return platforms[p]["platformNumber"]
    return None


arrivals = [200, 210, 300, 320, 350, 500]
departures = [230, 340, 320, 430, 400, 520]

print(min_platform(arrivals, departures))