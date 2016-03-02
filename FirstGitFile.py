from random import randint
numberofstudents = int(input("How many students are in the class\n >> "))
numberofruns = int(input("How many times do you want to run the test?\n >> "))
total_occurences = 0
for s in range(numberofruns):
    listofstudents = [randint(1,365) for z in range(numberofstudents)]
    occurrences = 0
    countI = 0
    for i in listofstudents[:len(listofstudents)-1]:
        countI += 1
        countP = 1
        for p in listofstudents[countI:]:
            countP += 1
            if i == p:
                occurrences += 1
    if occurrences >= 1:
        total_occurences += 1
chances_of_having_same_birthday = (float(total_occurences)/float(numberofruns))*100
print "The chance of sharing a birthday over the course of {} students, is {}%.".format(numberofstudents,
                                                                                       chances_of_having_same_birthday)
