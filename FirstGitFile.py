from random import randint
numberofstudents = int(input("How many students are in the class?\n>> "))
listofstudents = [randint(1,365) for z in range(numberofstudents)]
occurrences = 0
countP = 0
countI = 0
for i in listofstudents[:len(listofstudents)-1]:
    countI += 1
    for p in listofstudents:
        countP += 1
        if i == p:
            print "{}, person {} in the sequence is equal to {} person {} ".format(i,countI,p,countP)
            occurrences += 1
print "The total number of occurrences is {} over the course of {} students.".format(occurrences - 1, numberofstudents)
