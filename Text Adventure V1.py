# Adventure Game V1 [Untitled]
# Aim of the Game - Reach the Mountain Top!
# Some events will rely on luck to overcome but your inventory will affect your "luckiness"
# GLHF

import random

Failure_to_Type = "You're not very good at this text adventure lark are you? Try again"

def YoN():
	while True:
		outcome = raw_input("[YES] or [NO]? \n >> ")
		if outcome == "YES" or outcome == "NO":
			return outcome

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
	pass

def SLOWER():
	pass

def WALK():
	print """As you walk around the mountain you narrowly avoid a landslide which blocks off your route back to the start.
	However ahead you see a gentle gradient leading up the mountain. As you walk up the slope you see a small crevice, do
	you want to investigate it?"""
	crevice_choice = YoN
	if crevice_choice == "NO":
		print """You ignore the crevice - what could possibly be in there you scoff - and continue up the slope finally
		reaching a new plateau where you can rest."""
		WALK_Second_Level()
	if crevice_choice == "YES":
		print """You crawl inside the crevice - it's dark and smells but in the corner you see a little pool of water
		and there's something glinting inside it. You can fish it out if you want?"""



def WALK_Second_Level():
	pass

Welcome_Player()
