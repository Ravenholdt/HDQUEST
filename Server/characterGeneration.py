#!/usr/bin/env python

from random import random

import character
import dice

random.seed()

def generate_character()
	character = new_character()

	# 1. Grundläggande
	# Kön
	# Ras
	# Hemort
	# Kultur
	# Namn

	# 2. Attribut
	generate_attributes(character)

	# 3. Ålder
	generate_age(character)

	# 4. Karaktärsdrag
	# generate_personality(character) # Currently not in use.

	# 5. Bakgrundshistoria och Familj
	generate_bakground(character)
	generate_family(character)

	# 6. Bakgrundstabeller

	# 7. Härledda värden

	# 8. Familjens huvudnäring

	# 9. Yrke

	# 10. Grundchanser


def generate_attributes(character)
	character.attributes['STR'] = dice()
	character.attributes['TÅL'] = dice()
	character.attributes['RÖR'] = dice()

	character.attributes['PER'] = dice()
	character.attributes['SPY'] = dice()
	character.attributes['VIL'] = dice()

	character.attributes['BIL'] = dice()
	character.attributes['SYN'] = dice()
	character.attributes['HÖR'] = dice()

	for x in character.attributes
		if x < 6:
			x = 6


def generate_age(character)
	# Bil + ob3T6

	# Locked age sets the age to a predetermined value for all new characters.
	locked_age = True

	if locked_age:
		character.background['ålder'] = 18
	else:
		character.background['ålder'] = character.attributes['BIL'] + dice(6,3,1)
		if character.background['ålder'] >= 100:
			character.skills['valfri'] = 45
		elif character.background['ålder'] >= 90:
			character.skills['valfri'] += 40
		elif character.background['ålder'] >= 80:
			character.skills['valfri'] += 35
		elif character.background['ålder'] >= 70:
			character.skills['valfri'] += 30
		elif character.background['ålder'] >= 60:
			character.skills['valfri'] += 25
		elif character.background['ålder'] >= 50:
			character.skills['valfri'] += 20
		elif character.background['ålder'] >= 40:
			character.skills['valfri'] += 15
		elif character.background['ålder'] >= 30:
			character.skills['valfri'] += 10


def generate_personality(character)
	character.personality['Lojalitet']
	character.personality['Heder']
	character.personality['Amor']
	character.personality['Aggression']
	character.personality['Givmildhet']


def generate_bakground(character):
	vecka = random.randint(1, 5)
	if vecka == 1:
		character.background['vecka'] = 1
	elif vecka == 2:
		character.background['vecka'] = 2
	elif vecka == 3:
		character.background['vecka'] = 3
	elif vecka == 4:
		character.background['vecka'] = 4
	else:
		character.background['vecka'] = 0

	if character.background['vecka'] != 0:
		character.background['månad'] = dice(12,1)
		dag = random.randint(1,10)
		if dag >= 8:
			dag = 0
		character.background['veckodag'] = dag

	else:
		character.background['Födelsetidpunkt'] = random.randint(1,20)


def generate_family(character):
	# Generate sibling
	#younger = 