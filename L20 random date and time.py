import random
import time

def getRandomDate(startDate, endDate):
    print("printing random date between", startDate, "and", endDate)
    randomGenerator = random.random()

    dateFormat = "%m/%d/%Y"
    starttime = time.mktime(time.strptime(startDate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = starttime + randomGenerator * (endtime - starttime) 
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))

    return randomDate

result = getRandomDate("4/23/2025", "12/31/2025")
print("random date = ", result)