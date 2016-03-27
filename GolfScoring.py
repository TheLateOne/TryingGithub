def settings_for_golf():
    holes = input("How many holes are you playing today? ")
    par = input("What is the par for the course? ")
    return holes, par


def get_score_name(net_score, score_for_hole):
    if score_for_hole == 1:
        score_name = "a bloody hole-in-one, astounding"
    elif net_score == -1:
        score_name = "a birdie"
    elif net_score == -2:
        score_name = "an eagle"
    elif net_score == -3:
        score_name = "an albatross"
    elif net_score == 1:
        score_name = "a bogey"
    elif net_score == 2:
        score_name = "a double bogey"
    elif net_score == 3:
        score_name = "a triple bogey"
    elif net_score > 3:
        score_name = "a bit of a disaster"
    else:
        score_name = "a spectacular score"
    return score_name


def golf_score(holes, par):
    total_score = 0
    for a in range(holes):
        par_for_hole = input("What is the par for hole {}? ".format(a+1))
        score = input("What was your score for hole {}? ".format(a+1))
        net_score = score - par_for_hole
        score_name = get_score_name(net_score, score)

        if net_score < 0:
            print "Well done that's {} under par! That's {}.".format(net_score, score_name)
        elif net_score == 0:
            print "Well done that's par!"
        elif net_score > 0:
            print "Unlucky that's {} over par. That's {}.".format(net_score, score_name)

        total_score += score
        while True:
            carry_on = raw_input("Are you ready to move on to the next hole [Y/N]? ")
            if carry_on.lower() == "y":
                break
    average = total_score/float(holes)
    return "Your total score was {} vs. the course par of {} and your average score per hole was {}.".format(total_score,
                                                                                                           par, average)
holes, par = settings_for_golf()
print golf_score(holes, par)
