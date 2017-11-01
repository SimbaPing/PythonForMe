# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-07 20:46:13
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-07 21:56:47
from sys import exit
from random import randint


class Game(object):

    def __init__(self, start):
        self.quips = [
            "You died. You kinda suck at this.",
            "Your mom would be prouad. If she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this."
        ]
        self.start = start

    def play(self):
        next = self.start

        while True:
            print "\n---------"
            room = getattr(self, next)
            next = room()

    def death(self):
        print self.quips[randint(0, len(self.quips) - 1)]
        exit(1)

    def central_corridor(self):
        print "The Gothons of Plant Percal #25 have invaded your ship and destroyed"
        print "escape pod."
        print "\n"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster  and fire it at the Gothon."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right"
            return 'death'

        elif action == "tell a joke":
            print 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTER!"
            return 'central_corridor'

    def laser_weapon_armory(self):
        print "get the bomb. The code is 3 digits."
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "ship from their ship and you die."
            return 'death'

    def the_bridge(self):
        print "arm and don't want to set it off."
        action = raw_input("> ")

        if action == "throw the bomb":
            print "it goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "get off this tin can."
            return 'excape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return 'the_bridge'

    def escape_pod(self):
        print "do you take?"

        good_pod = randint(1, 5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "into jam jelly."
            return 'death'
        else:
            print "time, You won!"
            exit(0)

a_game = Game("central_corridor")
a_game.play()
