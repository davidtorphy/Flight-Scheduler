#David Torphy
#5/1/17
#Airline flight scheduling project

#This program works with a file of airlines names, flight number, departure time, arrival time, and price
#it displays a list of options and asks the user to pick one
#each option has a corrsponding function


#Function to open the file
def openFile():
    #ask user for file name
    
    goodFile = False
    while goodFile == False:
        #create name for file
        #try given file name
        fname = input("Please enter the name of the data file: ")
        try:
            inFile = open(fname, 'r')
            goodFile = True
            #except error, try again

        except IOError:
            print("Invalid file name try again ... ")
    return inFile

#Function to make lists
def getData():
    #Calls openFile() to access file
    #creates lists for the 5 catagories in the file
    infile = openFile()
    airlines = []
    flights = []
    departs = []
    arrives = []
    prices = []
    #reads one line at a time
    #splits each line into 5 different variables at the commas
    #Adds each variable to the corresponding list
    #Returns the lists
    line = infile.readline()
    while line != "":
        line = line.strip()
        airline, flight, depart, arrive, price  = line.split(",")
        airlines = airlines + [airline]
        flights = flights+ [int(flight)]
        departs = departs+[depart]
        arrives = arrives + [arrive]
        prices = prices + [price]
        line = infile.readline()
    infile.close()
    return airlines, flights, departs, arrives, prices

#Function to convert the list of prices to a new list of integer prices
def priceInt (prices):
    newPrices = []
    for price in prices:
        newPrice = price.strip('$')
        newPrice = int(newPrice)
        newPrices.append(newPrice)
    return newPrices


#Function to convert a time with hours and minutes into minutes
#returns minutes as an integer
def timeInt(time):
    hours, minutes = time.split(":")
    intTime = (int(hours)*60)+int(minutes)
 
    return intTime

#Function to display all flights for a specified airline
def getFlights(airlines, flights, departs, arrives, prices):
    #asks the user for an airline
    airline = input("Enter an airline to view flights")
    print("The flights that meet your criteria are: ")
    
    print("Airline FLT# DEPT ARR PRICE")
    print("-----------------------------------------")
    #iterates through list of airlines
    #prints the flights that match the specified airline
    inList = False
    for i in range(len(airlines)):
        if airlines[i] == airline:
            print (airlines[i], flights[i], departs[i], arrives[i], prices[i])
            inList = True
    
    if inList == False:
        print("Invalid airline, try again")

#Function to find the cheapest flight
def cheapestFlight (airlines, flights, departs, arrives, newPrices):
    cheapest = newPrices[0]
    #Iterates through list of prices
    #finds lowest value
    #prints information about flight at the index of the cheapest flight
    for price in newPrices:
        if price < cheapest:
            cheapest = price
        i = newPrices.index(cheapest)
    print ("The cheapest flight is", airlines[i], "flight #",flights[i],"at $", newPrices[i])

#Function to print all flights below a specified price
def priceLimit(airlines, flights, departs, arrives, newPrices):
    #ask user for maximum price
    goodPrice = False
    while goodPrice ==False:
        try:
            limit = int(input("Enter your maximum price:"))
            goodPrice = True
        except ValueError:
            print("Invalid price, try again")
    #Checks if the cheapest flight is more than the maximum
    cheapest = newPrices [0]
    i= 0
    for price in newPrices:
        if price < cheapest:
            cheapest = price
    if limit < cheapest:
            
        print ("No flights cheaper than limit")
    
    else:
        print("The flights that meet your criteria are: ")
        print("Airline FLT# DEPT ARR PRICE")
        print("-----------------------------------------")
    #iterates through list of prices
    #prints information for all flights less than limit
    for price in newPrices:
        if price<limit:
            print(airlines[i], flights[i], departs[i], arrives[i], "$",newPrices[i])
        i = i+1

        
#Function to find the shortest flight 
def shortest(airlines, flights, departs, arrives, newPrices):
    #create new list of times
    times = []
    #iterate through list of departure times
    for i in range(len(departs)):
        #convert times to minutes
        #subtract departure from arrival to find flight length
        
        times.append ( timeInt(arrives[i])-timeInt(departs[i]))
    #find the shortest flight in the new list of times
    #print information for the shortest flight
    shortest = times[0]
    for time in times:
        if time<shortest:
            shortest = time
    i = times.index(shortest)
    print("The shortest flight is", airlines[i], "flight",flights[i], "at", shortest, "minutes")

#Function to display all flights within a specified time range
def timeLimit(airlines, flights, departs, arrives, prices,):
    #asks for earliest  and latest departure times
    goodTime = False
    while goodTime == False:
        early = input("Enter the earliest allowed departure time:")
        late = input("Enter the latest allowede departure time:")
        #converts times into integers
 
        try:
            intEarly = timeInt(early)
            intLate = timeInt(late)
            print("The flights that meet your criteria are: ")
            print("Airline FLT# DEPT ARR PRICE")
            print("-----------------------------------------")
            #Loops through list of departure times and checks if it is within specified range
            #prints info for flights that meet the criteria
            for i in range(len(departs)):
                if  timeInt(departs[i])>=intEarly and timeInt(departs[i])<=intLate:
                    print(airlines[i], flights[i], departs[i], arrives[i], prices[i])
                goodTime = True
        #promts user to try again in case of value error
        except ValueError:
            print("Invalid time, please Try Again ")
 
#Function to display the average cost for a given airline
def average(airlines, flights, departs, arrives, prices, newPrices):
    goodName = False
    while goodName == False:
        #User enters name of airline
        airline = input("Enter the name of an airline to find the average price")
        #Loops through list of airlines
        #totals prices for all flights on specified airline
        #totals number of flights for specified airline
        #divides total cost by number of flights to get average
        total = 0
        divisor = 0
        try:
            for i in range(len(airlines)):
                if airlines[i] == airline:
                    divisor +=1
                    total = total +newPrices[i]
            average = total/divisor
            print ("The average price for", airline, "is $",average)
            goodName =True
            #Checks that airline name is in list of airlines
        except ZeroDivisionError:
            print("Invalid name, please try again")
            
        
 
#Function to display list of options for user to choose from 
#returns user's choice
def getChoice():
    print("PLease choose one of the following options:")
    print("1 -- Find all flights on a particular airline")
    print("2 -- Find the cheapest flight")
    print("3 -- Find all flights less than a specified price")
    print("4 -- Find the shortest flight")
    print("5 -- Find all flights that depart within a specified range")
    print("6 -- Find the Average price for a specified ariline")
    print("7 -- Quit")
    goodName = False
    while goodName == False:
        try:
    
            choice = int(input("Choice==>"))
            goodName = True
        except ValueError:
                print("Invalid Option, please try again")
                
    return choice
    
        
        
 
#Main function
#Runs functions to open file and make lists
#Gets new list of prices
#runs get choice
#runs the function corresponding to the users's choice
def main():
    airlines, flights, departs, arrives, prices = getData()
    newPrices = priceInt(prices)
    
    done =False
    
    while done ==False:
        choice = getChoice()
        if choice ==1:
            getFlights(airlines, flights, departs, arrives, prices)
        if choice ==2:
            cheapestFlight (airlines, flights, departs, arrives, newPrices)
        if choice ==3:
            priceLimit(airlines, flights, departs, arrives, newPrices)
        if choice == 4:
            shortest(airlines, flights, departs, arrives, newPrices)
        if choice == 5:
            timeLimit(airlines, flights, departs, arrives, prices)
        if choice ==6:
            average(airlines, flights, departs, arrives, prices, newPrices)
        if choice == 7:
            done =True
        if choice > 7 or choice <1:
            print("Invalid input, try again")
      
    
        
                
        
    

    
    

    




            
        
