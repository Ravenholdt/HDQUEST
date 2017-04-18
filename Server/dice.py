#!/usr/bin/env python

from random import random

random.seed()

# type: Typ av tärning, d6, d10, d100 osv.
# Rolls: Antal tärningar som skall rullas.
# Ob: Om obegränsat antal tärningar skall användas.
# Target: Vilket värde som skall uppnås.
def dice(dietype = 6, rolls = 3, ob = 0, target = 0)
	
	total = 0
	rolls_init = rolls
	rolls_current = 0
	one = 0
	six = 0
	result = 0

	while rolls:

		roll = random.randint(1, dietype)
		rolls_current += 1


		if ob and roll == dietype:
			rolls += 1
			six += 1
		else:
			total += roll
			rolls -= 1

		if ob and roll == 1:
			one += 1

		if rolls_current == rolls_init and ob:
			if one >= (rolls_init -1):
				result = 1
			if six >= 2:
				result = -1

	return (total, result)