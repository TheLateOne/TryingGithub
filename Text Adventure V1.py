# Adventure Game V1 [Untitled]
# Aim of the Game - Reach the Mountain Top!
# Some events will rely on luck to overcome but your inventory will affect your "luckiness"
# GLHF

import random

Failure_to_Type = "You're not very good at this text adventure lark are you? Try again"
inventory = {}


def YoN():  # Speeds up the Yes or No process and uses a while loop to avoid incorrect input for every case
    while True:
        outcome = raw_input("[YES] or [NO]? \n >> ")
        if outcome == "YES" or outcome == "NO":
            return outcome


def Random_Choice(range1, range2):
    random_number = random.randint(range1, range2)
    if random_number == 1:
        return True
    else:
        return False


def Welcome_Player():
    global name
    name = raw_input("What is your character's name? \n >> ")
    print "Well {} your adventure awaits, you have to climb this mountain but beware, it will not be easy!".format(name)
    Lowest_Level()


def Lowest_Level():
    while True:
        print """You are faced with a vast, steep and slippery mountain slope. You have 3 choices:
Climb the steepest but fastest route
Climb the slower and better trodden route
Walk round the mountain looking for a better starting point"""
        route_choice = raw_input("Will you go [FASTER], [SLOWER] or [WALK]? \n >> ")
        if route_choice == "FASTER" or route_choice == "SLOWER" or route_choice == "WALK":
            break
        print Failure_to_Type
    eval(route_choice)()


def FASTER():
    print """You must be brave or foolish to try this route. However, try it you will! You must climb with only
your hands up the first stretch of rocks. Chances of slipping are high... As you begin to climb you place both hands
on a single boulder."""
    if Random_Choice(1, 4):
        print """The boulder holds your whole weight. You swing a foot out and place it in a rocky crevice. You see a
small scuttling movement."""
        if Random_Choice(1, 2):
            print "It's just a spider"
            print """Unphased you pull yourself higher. You make good progress and can nearly see the top of the cliff
face. However as you reach to grab the edge your other hand slips."""
            if Random_Choice(1, 3):
                print """Like a verifiable badass you launch off with your feet, grab the cliff edge and pull yourself up.
You are exhausted but glad to see that you've made significant progress and notice that the route from
here seems a little easier."""
                FASTER_Second_Level()
            else:
                print """As you fall you wonder what will be written on your tombstone. Perhaps
'In Their Haste, {} Forgot Self-Preservation'""".format(name)
        else:
            print """It's a spider!! You swing your foot out of the hole and the momentum causes you to slip and fall back
to the bottom of the rock face. Clearly you need to rethink your phobia of spiders and visit a psychologist instead
of continuing this fools errand of climbing a mountain."""

    else:
        print """Ah... the boulder isn't so stable after all. It slips and falls down smashing into the top of your head...
You feel disheartened (and bruised) and decide that perhaps mountain climbing isn't a sport you'd like to take up
after all. Defeated you head home."""


def FASTER_Second_Level():
    pass


def SLOWER():
    print """It seems that many people have gone down this route before; reassuring. As you stride up the hill you make
good progress. Although the ground is slippy when you look back you can tell you've gone a fair distance already. As
you continue there is a small woods to your left. Do you want to adventure into the woods (if not you'll continue up
the mountain)?"""
    woods_choice = YoN()
    if woods_choice == "YES":
        Into_the_Woods()
    else:
        print """You don't want to stray into the woods, there could be all kinds of things in there (good and bad).
Instead you press on along the path. You soon reach a viewing point where you can see both up and down the mountain.
Bad news: you're not as far up as you'd hoped. You've only climbed a quarter of the mountain so far. Good news: the
view is spectacular from up here."""


def Into_the_Woods():
    print """As you enter the woods you hear a dull thudding like an axe being swung at a tree. Do you want to walk towards
the noise?"""
    woods_noise = YoN()
    if woods_noise == "YES":
        print """You head towards to the noise. You eventually come to a clearing and as expected there is a woodsman
chopping down a tree. At the edge of the clearing is a wooden hut (presumably where the woodsman lives). Do you
want to talk to the woodsman or sneak around to his hut?"""
        while True:
            clearing_choice = raw_input("[HUT] or [WOODSMAN]? \n >> ")
            if clearing_choice == "HUT":
                print """You stick to the edge of the woods and make your way round to the hut. You try the door and it's
unlocked. Inside there is a rope hanging on the wall, walking boots, a climbing harness, a handheld axe and
a fur coat. Would you like to take anything?"""
                hut_item = raw_input("[ROPE], [BOOTS], [HARNESS], [AXE], [COAT], [NONE] \n >> ")
                if hut_item == "NONE":
                    print """You decide it's probably safest just to leave so you walk back into the clearing and into
the cover of the trees. You can still talk to the woodsman if you'd like. Would you like to talk
to him?"""
                    if YoN():
                        Woodsman_Interaction()
                    else:
                        """Do you want to talk to a man with an axe? Not today thank you, especially having just broken
                        into his hut. Instead {} decides to wander back into the woods, exploring further.""".format(
                            name)
                        Back_to_the_Woods()
                else:
                    count_items_taken = 0
                    while True:
                        try:
                            eval(hut_item)()
                            count_items_taken += 1

                        except NameError:
                            print Failure_to_Type

                        if Random_Choice(1, 10):
                            Woodsman_Surprise()

                        elif count_items_taken == 5:
                            print "You've taken all the items so you head back into the woods."
                            Back_to_the_Woods()

                        else:
                            hut_item = (raw_input("Do you want to take anything else? \n >> "))

            if clearing_choice == "WOODSMAN":
                Woodsman_Interaction()


def ROPE():
    inventory["Rope"] = random.randint(1, 8)
    print "Congratulations you pick up the rope and put it in your inventory!"


def BOOTS():
    inventory["Boots"] = random.randint(1, 8)
    print "Congratulations you pick up the boots and put it in your inventory!"


def HARNESS():
    inventory["Harness"] = random.randint(1, 8)
    print "Congratulations you pick up the harness and put it in your inventory!"


def AXE():
    inventory["Axe"] = random.randint(1, 8)
    print "Congratulations you pick up the axe and put it in your inventory!"


def COAT():
    inventory["Coat"] = random.randint(1, 8)
    print "Congratulations you pick up the coat and put it in your inventory!"


def Woodsman_Surprise():
    print """As you are ransacking the Woodsman's hut he bursts through the door, axe in hand, rage in his eyes.
You consider that perhaps stealing from a man who lives in the middle of nowhere may be a bad idea. The woodsman
goes all 'Little Red Riding Hood' on your ass and you are never heard from again!"""
    exit()


def Woodsman_Interaction():
    print """You talk to the woodsman and explain your goal of climbing the mountain. He seems slightly confused as to
why you're in the woods if your goal is to climb the mountain."""
    if Random_Choice(1, 8):
        print """The woodsman becomes so enfuriated with your pedantic and dull conversation he starts swearing and
gesturing with his axe. Sensing danger you back into the woods but the woodsman chases you. Fearing for your life
you run back down to the foot of the mountain and into the nearby village. You recount your tale over a glass of
ale and vow never to step foot on that mountain again."""
        exit()
    else:
        print """Sensing your complete inability to climb mountains in an efficient manner he invites you over to
his hut and hands you a rope and a fur coat, telling you that you must respect the mountain and exercise proper
safety measures especially when rock climbing. Emboldened by your new equipment you head back into the forest
in search of more useful gear."""
        inventory["Rope"] = 9
        inventory["Coat"] = 3
        Back_to_the_Woods()


def Back_to_the_Woods():
    pass


def WALK():
    print """As you walk around the mountain you narrowly avoid a landslide which blocks off your route back to the start.
However ahead you see a gentle gradient leading up the mountain. As you walk up the slope you see a small crevice, do
you want to investigate it?"""
    crevice_choice = YoN()
    if crevice_choice == "NO":
        print """{} ignores the crevice - what could possibly be in there you scoff - and continue up the slope finally
reaching a new plateau where you can rest.""".format(name)
        WALK_Second_Level()
    if crevice_choice == "YES":
        print """You crawl inside the crevice - it's dark and smells but in the corner you see a little pool of water
and there's something glinting inside it. You can fish it out if you want?"""
        WALK_pool_choice = YoN()
        if WALK_pool_choice == "YES":
            print "You try to fish the glinting object out"
            pool_outcome = Random_Choice(1, 4)
            if pool_outcome:
                print """Congratulations you managed to grab the metal hook from inside the pool of water, it will
be added to your inventory now!"""
                inventory["Hook"] = 5
            else:
                print """As you reach into the pool you slip and fall face first into the water; covered in slime and
water you decide that perhaps the pay-off isn't worth it after all and crawl back out of the crevice,
defeated."""
        if WALK_pool_choice == "NO":
            print """{} stares blankly around the crevice. There's nothing worth exploring in there except that pool
so you decide to leave now and continue on your journey. You crawl out of the crevice.""".format(name)
        print """As you come out of the crevice you see that the climb levels off just above so you climb to a small plateau
and admire the scenery"""
        WALK_Second_Level()


def WALK_Second_Level():
    pass


Into_the_Woods()
