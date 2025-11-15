from autoUnlock import currentAmounts, minRequiredResources, droneIntervals, checkIfCanUnlock
from wayToGoFile import wayToGo
from mappingMaze_v3 import searchMaze_v3

def tryHarvest():
	if can_harvest():
		harvest()

def checkWater(water):
	if (get_water() < water) and (num_items(Items.Water) > 100000):
		use_item(Items.Water)

def checkResources(current, required, fieldWidth, fieldHeight, numDrones):
	if (get_pos_x() == 0) and (get_pos_y() == 0):
		checkIfCanUnlock(current)
		current = currentAmounts(True, current)
		required, item = minRequiredResources(True, current, required)
		fieldWidth = get_world_size()
		fieldHeight = get_world_size()
		numDrones = droneIntervals(fieldWidth, fieldHeight)
	return current, required, fieldWidth, fieldHeight, numDrones, item

def plantWork(current, required, fieldWidth, fieldHeight, interval, currentWay, item, drones):
	if len(drones) == 0:
		who = 'Main drone '
	else:
		who = str(drones[len(drones) - 1])
	if item == Items.Hay:
		quick_print(who, ': Planting Hay!')
		plantHay(current, required, fieldWidth, fieldHeight, interval, currentWay, drones)
	elif item == Items.Wood:
		quick_print(who, ': Planting Wood!')
		plantWood(current, required, fieldWidth, fieldHeight, interval, currentWay, drones)
	elif item == Items.Carrot:
		quick_print(who, ': Planting Carrot!')
		plantCarrot(current, required, fieldWidth, fieldHeight, interval, currentWay, drones)
	elif item == Items.Pumpkin:
		quick_print(who, ': Planting Pumpkin!')
		plantPumpkin(current, required, fieldWidth, fieldHeight, interval, currentWay, drones)
	elif item == Items.Cactus:
		quick_print(who, ': Planting Cactus!')
		plantCactus(current, required, fieldWidth, fieldHeight, interval, currentWay, drones)
	elif item == Items.Weird_Substance:
		quick_print(who, ': Planting WeirdSubstance!')
		plantWeirdSubstance(current, required, fieldWidth, fieldHeight, interval, currentWay, drones)
	elif item == Items.Gold:
		quick_print(who, ': Searching Gold!')
		plantGold(current, required, fieldWidth, fieldHeight, interval, currentWay, drones)
	elif item == Items.Power:
		quick_print(who, ': Planting SunFlowers!')
		plantSunFlower(current, required, fieldWidth, fieldHeight, interval, currentWay, drones)

def dronePlantWork(plantWork, current, required, fieldWidth, fieldHeight, interval, currentWay, id, drones):
	def work():
		plantWork(current, required, fieldWidth, fieldHeight, interval, currentWay, id, drones)
	return spawn_drone(work)

def plantSmth(current, required, fieldWidth, fieldHeight, numDrones, item):
	currentWay = [North, East]
	drones = []
	counter = 0
	quick_print('')
	if (item != Items.Gold):	#Excluse Maze
		for i in range(len(numDrones) - 1):
			drones.append(dronePlantWork(plantWork, current, required, fieldWidth, fieldHeight, numDrones[i + 1], currentWay, item, drones))

	plantWork(current, required, fieldWidth, fieldHeight, numDrones[0], currentWay, item, drones)

	return current, required, fieldWidth, fieldHeight	

def plantHay(current, required, fieldWidth, fieldHeight, interval, currentWay, drones):
	done = False
	while not done:
		tryHarvest()
		plant(Entities.Grass)
		currentWay, current = wayToGo(interval, currentWay, current)
		done = current[Items.Hay] > required[Items.Hay]
	for drone in drones:
		wait_for(drone)
		
def plantWood(current, required, fieldWidth, fieldHeight, interval, currentWay, drones):
	done = False
	while not done:
		tryHarvest()
		checkWater(0.5)
		if (get_pos_x() + get_pos_y()) % 2 == 1:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
		currentWay, current = wayToGo(interval, currentWay, current)
		done = current[Items.Wood] > required[Items.Wood]
	for drone in drones:
		wait_for(drone)
		
def plantCarrot(current, required, fieldWidth, fieldHeight, interval, currentWay, drones):
	done = False
	while not done:
		tryHarvest()
		checkWater(0.5)
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
		currentWay, current = wayToGo(interval, currentWay, current)
		done = current[Items.Carrot] > required[Items.Carrot]
	for drone in drones:
		wait_for(drone)

def plantPumpkin(current, required, fieldWidth, fieldHeight, interval, currentWay, drones):
	done = False
	while not done:
		tryHarvest()
		checkWater(0.5)
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
		currentWay, current = wayToGo(interval, currentWay, current)
		done = current[Items.Pumpkin] > required[Items.Pumpkin]
	for drone in drones:
		wait_for(drone)
		
def plantCactus(current, required, fieldWidth, fieldHeight, interval, currentWay, drones):
	done = False
	while not done:
		tryHarvest()
		checkWater(0.5)
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		currentWay, current = wayToGo(interval, currentWay, current)
		done = current[Items.Cactus] > required[Items.Cactus]
	for drone in drones:
		wait_for(drone)

def plantWeirdSubstance(current, required, fieldWidth, fieldHeight, interval, currentWay, drones):
	done = False
	while not done:
		tryHarvest()
		plant(Entities.Grass)
		use_item(Items.Fertilizer)
		currentWay, current = wayToGo(interval, currentWay, current)
		done = current[Items.Gold] > required[Items.Gold]
	for drone in drones:
		wait_for(drone)

def plantGold(current, required, fieldWidth, fieldHeight, interval, currentWay, drones):
	done = False
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
	for drone in drones:
		wait_for(drone)
		
def plantSunFlower(current, required, fieldWidth, fieldHeight, interval, currentWay, drones):
	done = False
	while not done:
		tryHarvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Sunflower)
		currentWay, current = wayToGo(interval, currentWay, current)
		done = current[Items.Power] > required[Items.Power]
	for drone in drones:
		wait_for(drone)

def choosePlant(current, required, fieldWidth, fieldHeight):
	numDrones = [[0, 15, 0, 15]]
	current, required, fieldWidth, fieldHeight, numDrones, item = checkResources(current, required, fieldWidth, fieldHeight, numDrones)
	current, required, fieldWidth, fieldHeight = plantSmth(current, required, fieldWidth, fieldHeight, numDrones, item)
		
	return current, required, fieldWidth, fieldHeight
