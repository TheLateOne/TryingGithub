from random import randint


def odds_of_shared_features(number_of_cases,number_of_tests,upper_range):
    total_occurrences = 0
    for s in range(number_of_tests):
        listofstudents = [randint(1,upper_range) for z in range(number_of_cases)]
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
            total_occurrences += 1
    chances_of_having_same_birthday = (float(total_occurrences)/float(numberofruns))*100
    print "The chance of sharing a birthday over the course of {} students, is {}%.".format(numberofstudents,
                                                                                           chances_of_having_same_birthday)
numberofstudents = int(input("How many students are in the class\n >> "))
numberofruns = int(input("How many times do you want to run the test?\n >> "))
upper_range_ints = int(input("What's the upper range of potential choices?\n >> "))
odds_of_shared_features(numberofstudents, numberofruns, upper_range_ints)