# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-05 10:10:43
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-05 11:22:28


from sys import exit

from random import randint


def death():

    quips = ["You died. You kinda suck at this.",
             "Nice job, you died ...jackass.",
             "such a luser.",
             "I have a small puppy that's better at this."]

    print quips[randint(0, len(quips)-1)]

    esit(1)


def central_corridor():

    print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"

    print "your entire crew. You are the last surviving meber and your last"

    print "mission is to get the meutron destruct bomb from the Weapons Armory,"

    print "put it in the bridge, and blow the ship up agter getting into an "

    print "escape pod."

    print "\n"

    print "You're running down the central corridor to the Weapons Aromry when"

    print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
