# Adventure Game V1 [Untitled]
# Aim of the Game - Reach the Mountain Top!
# Some events will rely on luck to overcome but your inventory will affect your "luckiness"
# GLHF

import random

Failure_to_Type = "You're not very good at this text adventure lark are you? Try again"
inventory = {}

def YoN(): # Speeds up the Yes or No process and uses a while loop to avoid incorrect input for every case
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
	route_choice = ""
	while True:
		print """You are faced with a vast, steep and slippery mountain slope. You have 3 choices: 
		Climb the steepest but fasteest route
		Climb the slower and better trodden route
		Walk round the mountain looking for a better starting point"""
		route_choice = raw_input("Will you go [FASTER], [SLOWER] or [WALK]? \n >> ")
		if route_choice	== "FASTER" or route_choice	== "SLOWER" or route_choice	== "WALK":
			break
		print Failure_to_Type
	route_as_function = eval(route_choice)
	route_as_function()

def FASTER():
	print """You must be brave or foolish to try this route. However, try it you will! You must climb with only
	your hands up the first stretch of rocks. Chances of slipping are high... As you begin to climb you place both hands
	on a single boulder."""
	if Random_Choice(1,4):
		print """The boulder holds your whole weight. You swing a foot out and place it in a rocky crevice. You see a 
		small scuttling movement."""
		if Random_Choice(1,2):
			print "It's just a spider"
			print """Unphased you pull yourself higher. You make good progress and can nearly see the top of the cliff 
			face. However as you reach to grab the edge your other hand slips."""
			if Random_Choice(1,5):
				print """Like a verifiable badass you launch off with your feet, grab the cliff edge and pull yourself up. 
				You are exhausted but glad to see that you've made significant progress and notice that the route from
				here seems a little easier."""
			else:
				print """As you fall you wonder what will be written on your tombstone. Perhaps 
				'In Haste {} Forgot Self-Preservation'""".format(name)
		else:
			print """It's a spider!! You swing your foot out of the hole and the momentum causes you to slip and fall back
			to the bottom of the rock face. Clearly you need to rethink your phobia of spiders and visit a psychologist instead
			of continuing this fools errand of climbing a mountain."""

	else:
		print """Ah... the boulder isn't so stable after all. It slips and falls down smashing into the top of your head...
		You feel disheartened (and bruised) and decide that perhaps mountain climbing isn't a sport you'd like to take up
		after all. Defeated you head home."""

def SLOWER():
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
		if WALK_pool_choice	== "YES":
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
		if WALK_pool_choice	== "NO":
			print """{} stares blankly around the crevice. There's nothing worth exploring in there except that pool
			so you decide to leave now and continue on your journey. You crawl out of the crevice.""".format(name)
		print """As you come out of the crevice you see that the climb levels off just above so you climb to a small plateau
		and admire the scenery"""
		WALK_Second_Level()


def WALK_Second_Level():
	pass

Welcome_Player()
