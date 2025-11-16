from choosePlantFile import *
from wayToGoFile import *
from autoUnlock import *

clear()

fieldWidth = 16
fieldHeight = 16

current = {}
required = {}

current[Items.Hay] = 0				#Hay
current[Items.Wood] = 0				#Wood
current[Items.Carrot] = 0			#Carrot
current[Items.Pumpkin] = 0			#Pumpkin
current[Items.Cactus] = 0			#Cactus
current[Items.Weird_Substance] = 0	#WeirdSubstance
current[Items.Gold] = 0				#Gold
current[Items.Power] = 0			#Power

required[Items.Hay] = 100000				#Hay
required[Items.Wood] = 100000				#Wood
required[Items.Carrot] = 100000				#Carrot
required[Items.Pumpkin] = 100000			#Pumpkin
required[Items.Cactus] = 100000				#Cactus
required[Items.Weird_Substance] = 100000	#WeirdSubstance
required[Items.Gold] = 100000				#Gold
required[Items.Power] = 100000				#Power

def doHarvest():
	while can_harvest():
		harvest()

def main():
	global current
	global required
	global fieldWidth
	global fieldHeight
	allDone = False
	while not allDone:
		current, required, fieldWidth, fieldHeight, allDone = choosePlant(current, required, fieldWidth, fieldHeight)

if __name__ == "__main__":
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)
	main()

