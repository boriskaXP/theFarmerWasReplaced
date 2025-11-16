from autoUnlock import currentAmounts, minRequiredResources, droneIntervals, checkIfCanUnlock
from wayToGoFile import wayToGo, resetPosition
from mappingMaze_v3 import searchMaze_v3

def tryHarvest():
	if can_harvest():
		harvest()

def checkWater(water):
	if (get_water() < water) and (num_items(Items.Water) > 100000):
		use_item(Items.Water)

def collectAllSunFlowers(interval, currentWay, current, drones, mainDrone):
	if mainDrone:
		change_hat(Hats.Wizard_Hat)
	else:
		change_hat(Hats.Sunflower_Hat)
	done = False
	counter = 0
	resetPosition(interval, current)
	while not done:
		counter += 1
		harvest()
		currentWay, current = wayToGo(interval, currentWay, current)
		done = (counter >= (interval[3] - interval[2] + 1) * (interval[1] - interval[0] + 1))
	if mainDrone:
		for drone in drones:
			wait_for(drone)

def callDronesToCollectAllSunFlowers(interval, currentWay, current, drones, mainDrone):
	def work():
		collectAllSunFlowers(interval, currentWay, current, drones, mainDrone)

	return spawn_drone(work)
	

def checkResources(current, required, fieldWidth, fieldHeight, numDrones):
	checkIfCanUnlock(current)
	current = currentAmounts(True, current)
	required, item = minRequiredResources(True, current, required)
	fieldWidth = get_world_size()
	fieldHeight = get_world_size()
	numDrones = droneIntervals(False, fieldWidth, fieldHeight)
	return current, required, fieldWidth, fieldHeight, numDrones, item

def plantWork(current, required, fieldWidth, fieldHeight, interval, currentWay, item, drones, numDrones, mainDrone):
	if len(drones) == 0:
		who = 'Main drone '
	else:
		who = str(drones[len(drones) - 1])
	if item == Items.Hay:
		quick_print(who, ': Planting Hay!')
		plantHay(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone)
	elif item == Items.Wood:
		quick_print(who, ': Planting Wood!')
		plantWood(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone)
	elif item == Items.Carrot:
		quick_print(who, ': Planting Carrot!')
		plantCarrot(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone)
	elif item == Items.Pumpkin:
		quick_print(who, ': Planting Pumpkin!')
		plantPumpkin(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone)
	elif item == Items.Cactus:
		quick_print(who, ': Planting Cactus!')
		plantCactus(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone)
	elif item == Items.Weird_Substance:
		quick_print(who, ': Planting WeirdSubstance!')
		plantWeirdSubstance(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone)
	elif item == Items.Gold:
		quick_print(who, ': Searching Gold!')
		plantGold(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone)
	elif item == Items.Power:
		quick_print(who, ': Planting SunFlowers!')
		plantSunFlower(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone)

def dronePlantWork(plantWork, current, required, fieldWidth, fieldHeight, interval, currentWay, id, drones, numDrones):
	def work():
		plantWork(current, required, fieldWidth, fieldHeight, interval, currentWay, id, drones, numDrones, False)
	return spawn_drone(work)

def plantSmth(current, required, fieldWidth, fieldHeight, numDrones, item):
	currentWay = [North, East]
	drones = []
	quick_print('')
	if (item != Items.Gold):	#Exclude Maze
		for i in range(len(numDrones) - 1):
			drones.append(dronePlantWork(plantWork, current, required, fieldWidth, fieldHeight, numDrones[i + 1], currentWay, item, drones, numDrones))

	plantWork(current, required, fieldWidth, fieldHeight, numDrones[0], currentWay, item, drones, numDrones, True)

	return current, required, fieldWidth, fieldHeight	

def plantHay(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone):
	if mainDrone:
		change_hat(Hats.Wizard_Hat)
	else:
		change_hat(Hats.Straw_Hat)
	done = False
	resetPosition(interval, current)
	while not done:
		tryHarvest()
		plant(Entities.Grass)
		currentWay, current = wayToGo(interval, currentWay, current)
		done = (current[Items.Hay] > required[Items.Hay]) or (current[Items.Power] < 1000)
	if mainDrone:
		for drone in drones:
			wait_for(drone)
		
def plantWood(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone):
	if mainDrone:
		change_hat(Hats.Wizard_Hat)
	else:
		change_hat(Hats.Tree_Hat)
	done = False
	done = False
	resetPosition(interval, current)
	while not done:
		tryHarvest()
		checkWater(0.5)
		if (get_pos_x() + get_pos_y()) % 2 == 1:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
		currentWay, current = wayToGo(interval, currentWay, current)
		done = (current[Items.Wood] > required[Items.Wood]) or (current[Items.Power] < 1000)
	if mainDrone:
		for drone in drones:
			wait_for(drone)
		
def plantCarrot(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone):
	if mainDrone:
		change_hat(Hats.Wizard_Hat)
	else:
		change_hat(Hats.Carrot_Hat)
	done = False
	done = False
	resetPosition(interval, current)
	while not done:
		tryHarvest()
		checkWater(0.5)
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
		currentWay, current = wayToGo(interval, currentWay, current)
		done = (current[Items.Carrot] > required[Items.Carrot]) or (current[Items.Power] < 1000)
	if mainDrone:
		for drone in drones:
			wait_for(drone)

def plantPumpkin(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone):
	if mainDrone:
		change_hat(Hats.Wizard_Hat)
	else:
		change_hat(Hats.Pumpkin_Hat)
	done = False
	done = False
	counter = 0
	resetPosition(interval, current)
	while not done:
		if (get_pos_x() == interval[0]) and (get_pos_y() == interval[2]):
			counter = 0
		if get_entity_type() != Entities.Pumpkin:
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		if not can_harvest():
			plant(Entities.Pumpkin)
		else:
			counter += 1
		currentWay, current = wayToGo(interval, currentWay, current)
		done = (counter >= (interval[3] - interval[2] + 1) * (interval[1] - interval[0] + 1))
	if mainDrone:
		for drone in drones:
			wait_for(drone)
		harvest()
		
def plantCactus(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone):
	if mainDrone:
		change_hat(Hats.Wizard_Hat)
	else:
		change_hat(Hats.Cactus_Hat)
	done = False
	done = False
	resetPosition(interval, current)
	while not done:
		tryHarvest()
		checkWater(0.5)
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		currentWay, current = wayToGo(interval, currentWay, current)
		done = (current[Items.Cactus] > required[Items.Cactus]) or (current[Items.Power] < 1000)
	if mainDrone:
		for drone in drones:
			wait_for(drone)

def plantWeirdSubstance(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone):
	if mainDrone:
		change_hat(Hats.Wizard_Hat)
	else:
		change_hat(Hats.Purple_Hat)
	done = False
	done = False
	resetPosition(interval, current)
	while not done:
		tryHarvest()
		plant(Entities.Grass)
		use_item(Items.Fertilizer)
		currentWay, current = wayToGo(interval, currentWay, current)
		done = (current[Items.Gold] > required[Items.Gold]) or (current[Items.Power] < 1000)
	if mainDrone:
		for drone in drones:
			wait_for(drone)

def plantGold(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone):
	if mainDrone:
		change_hat(Hats.Wizard_Hat)
	else:
		change_hat(Hats.Gold_Hat)
	done = False
	done = False
	resetPosition(interval, current)
	while not done:
		randomX = random() * 7
		randomY = random() * 7
		for x in range(randomX):
			move(East)
		for y in range(randomY):
			move(North)
		if can_harvest():
			harvest()
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
		searchMaze_v3(300, fieldWidth, fieldHeight)
		done = current[Items.Weird_Substance] > required[Items.Weird_Substance]
	if mainDrone:
		for drone in drones:
			wait_for(drone)
		
def plantSunFlower(current, required, fieldWidth, fieldHeight, interval, currentWay, drones, numDrones, mainDrone):
	if mainDrone:
		change_hat(Hats.Wizard_Hat)
	else:
		change_hat(Hats.Sunflower_Hat)
	done = False
	quality = 16
	done = False
	counter = 0
	firstRun = True
	resetPosition(interval, current)
	while not done:
		if (get_pos_x() == interval[0]) and (get_pos_y() == interval[2]):
			counter = 0
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Sunflower)
		if get_entity_type() == Entities.Sunflower:
			if measure() < quality:
				if not firstRun:
					harvest()
				plant(Entities.Sunflower)
				checkWater(0.5)
			else:
				counter += 1
		
		currentWay, current = wayToGo(interval, currentWay, current)
		firstRun = False
		if quality < 16:
			done = (counter >= (interval[3] - interval[2] + 1) * (interval[1] - interval[0] + 1))
		else:
			done = current[Items.Power] > required[Items.Power]
	if mainDrone:
		if quality < 16:
			for drone in drones:
				wait_for(drone)
			drones = []
			for i in range(len(numDrones) - 1):
				drones.append(callDronesToCollectAllSunFlowers(numDrones[i + 1], currentWay, current, drones, mainDrone))
			collectAllSunFlowers(numDrones[0], currentWay, current, drones, mainDrone)
		else:
			for drone in drones:
				wait_for(drone)

def choosePlant(current, required, fieldWidth, fieldHeight):
	numDrones = [[0, 15, 0, 15]]
	current, required, fieldWidth, fieldHeight, numDrones, item = checkResources(current, required, fieldWidth, fieldHeight, numDrones)
	allDone = False
	if item != None:
		current, required, fieldWidth, fieldHeight = plantSmth(current, required, fieldWidth, fieldHeight, numDrones, item)
	else:
		allDone = True
		
	return current, required, fieldWidth, fieldHeight, allDone
