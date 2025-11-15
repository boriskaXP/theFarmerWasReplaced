def collectUnlocks():
	unlocks = []
	unlocks.append(Unlocks.Loops)
	unlocks.append(Unlocks.Hats)
	unlocks.append(Unlocks.Speed)
	unlocks.append(Unlocks.Grass)
	unlocks.append(Unlocks.Expand)
	unlocks.append(Unlocks.Plant)
	unlocks.append(Unlocks.Carrots)
	unlocks.append(Unlocks.Debug)
	unlocks.append(Unlocks.Operators)
	unlocks.append(Unlocks.Speed)
	unlocks.append(Unlocks.Trees)
	unlocks.append(Unlocks.Debug_2)
	unlocks.append(Unlocks.Timing)
	unlocks.append(Unlocks.Senses)
	unlocks.append(Unlocks.Variables)
	unlocks.append(Unlocks.Fertilizer)
	unlocks.append(Unlocks.Sunflowers)
	unlocks.append(Unlocks.Pumpkins)
	unlocks.append(Unlocks.Simulation)
	unlocks.append(Unlocks.Lists)
	unlocks.append(Unlocks.Functions)
	unlocks.append(Unlocks.Mazes)
	unlocks.append(Unlocks.Cactus)
	unlocks.append(Unlocks.Polyculture)
	unlocks.append(Unlocks.Leaderboard)
	unlocks.append(Unlocks.Dictionaries)
	unlocks.append(Unlocks.Import)
	unlocks.append(Unlocks.Utilities)
	unlocks.append(Unlocks.Top_Hat)
	unlocks.append(Unlocks.Megafarm)
	unlocks.append(Unlocks.Dinosaurs)
	unlocks.append(Unlocks.Costs)
	unlocks.append(Unlocks.The_Farmers_Remains)
	unlocks.append(Unlocks.Auto_Unlock)
	
	upgrades = []
	for i in range(len(unlocks)):
		cost = get_cost(unlocks[i])
		upgrades.append([unlocks[i], cost])

	return upgrades

def minRequiredResources(debug, current, required):
	data = collectUnlocks()
	resourcesRequired = []
	for i in range(len(data)):
		upgrades = data[i][1]
		for key in upgrades:
			resourcesRequired.append([key, upgrades[key]])

	for item in resourcesRequired:
		if (item[0] == Items.Hay) and (required[Items.Hay] != item[1]) and (item[1] != 0):
			required[Items.Hay] = item[1]
		elif (item[0] == Items.Wood) and (required[Items.Wood] != item[1]) and (item[1] != 0):
			required[Items.Wood] = item[1]
		elif (item[0] == Items.Carrot) and (required[Items.Carrot] != item[1]) and (item[1] != 0):
			required[Items.Carrot] = item[1]
		elif (item[0] == Items.Pumpkin) and (required[Items.Pumpkin] != item[1]) and (item[1] != 0):
			required[Items.Pumpkin] = item[1]
		elif (item[0] == Items.Cactus) and (required[Items.Cactus] != item[1]) and (item[1] != 0):
			required[Items.Cactus] = item[1]
		elif (item[0] == Items.Weird_Substance) and (required[Items.Weird_Substance] != item[1]) and (item[1] != 0):
			required[Items.Weird_Substance] = item[1]
		elif (item[0] == Items.Gold) and (required[Items.Gold] != item[1]) and (item[1] != 0):
			required[Items.Gold] = item[1]
		elif (item[0] == Items.Power) and (required[Items.Power] != item[1]) and (item[1] != 0):
			required[Items.Power] = item[1]

	chooseItem = Items.Hay
	mini = 0
	list = {}

	for key in required:
		if (current[key] < required[key]):
			list[key] = required[key]
		if mini < required[key]:
			mini = required[key]

	for key in list:
		if mini > list[key]:
			mini = list[key]

	for key in list:
		if mini == list[key]:
			chooseItem = key
	
	print('')
	
	if chooseItem == Items.Hay:
		required[Items.Hay] = required[Items.Hay]
		quick_print('Hay required: ', required[Items.Hay])
	elif chooseItem == Items.Wood:
		required[Items.Wood] = required[Items.Wood]
		quick_print('Wood required: ', required[Items.Wood])
	elif chooseItem == Items.Carrot:
		required[Items.Carrot] = required[Items.Carrot]
		required[Items.Wood] = get_cost(Entities.Carrot)[Items.Wood] * required[Items.Carrot]
		required[Items.Hay] = get_cost(Entities.Carrot)[Items.Hay] * required[Items.Carrot]
		quick_print('Carrot required: ', required[Items.Carrot])
		quick_print('Need Wood for Carrot: ', required[Items.Wood])
		quick_print('Need Hay for Carrot: ', required[Items.Hay])
		if current[Items.Hay] < required[Items.Hay]:
			chooseItem = Items.Hay
		elif current[Items.Wood] < required[Items.Wood]:
			chooseItem = Items.Wood
	elif chooseItem == Items.Pumpkin:
		required[Items.Pumpkin] = required[Items.Pumpkin]
		required[Items.Carrot] = get_cost(Entities.Pumpkin)[Items.Carrot] * required[Items.Pumpkin]
		required[Items.Wood] = get_cost(Entities.Carrot)[Items.Wood] * required[Items.Carrot]
		required[Items.Hay] = get_cost(Entities.Carrot)[Items.Hay] * required[Items.Carrot]
		quick_print('Pumpkin required: ', required[3])
		quick_print('Need Carrot for Pumpkin: ', required[Items.Carrot])
		quick_print('Need Wood for Carrot: ', required[Items.Wood])
		quick_print('Need Hay for Carrot: ', required[Items.Hay])
		if current[Items.Hay] < required[Items.Hay]:
			chooseItem = Items.Hay
		elif current[Items.Wood] < required[Items.Wood]:
			chooseItem = Items.Wood
		elif current[Items.Carrot] < required[Items.Carrot]:
			chooseItem = Items.Carrot
	elif chooseItem == Items.Cactus:
		required[Items.Cactus] = required[Items.Cactus]
		required[Items.Pumpkin] = get_cost(Entities.Cactus)[Items.Pumpkin] * required[Items.Cactus]
		required[Items.Carrot] = get_cost(Entities.Pumpkin)[Items.Carrot] * required[Items.Pumpkin]
		required[Items.Wood] = get_cost(Entities.Carrot)[Items.Wood] * required[Items.Carrot]
		required[Items.Hay] = get_cost(Entities.Carrot)[Items.Hay] * required[Items.Carrot]
		quick_print('Cactus required: ', required[Items.Cactus])
		quick_print('Need Pumpkin for Cactus: ', required[Items.Pumpkin])
		quick_print('Need Carrot for Pumpkin: ', required[Items.Carrot])
		quick_print('Need Wood for Carrot: ', required[Items.Wood])
		quick_print('Need Hay for Carrot: ', required[Items.Hay])
		if current[Items.Hay] < required[Items.Hay]:
			chooseItem = Items.Hay
		elif current[Items.Wood] < required[Items.Wood]:
			chooseItem = Items.Wood
		elif current[Items.Carrot] < required[Items.Carrot]:
			chooseItem = Items.Carrot
		elif current[Items.Carrot] < required[Items.Pumpkin]:
			chooseItem = Items.Pumpkin
	elif chooseItem == Items.Weird_Substance:
		required[Items.Weird_Substance] = required[Items.Weird_Substance]
		quick_print('WeirdSubstance required: ', required[Items.Weird_Substance])
	elif chooseItem == Items.Gold:
		required[Items.Gold] = required[Items.Gold]
		required[Items.Weird_Substance] = (get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)) * (required[Items.Gold] / get_world_size() / get_world_size())
		quick_print('Gold required: ', required[Items.Gold])
		quick_print('Need WeirdSubstance for Gold: ', required[Items.Weird_Substance])
		if current[Items.Weird_Substance] < required[Items.Weird_Substance]:
			chooseItem = Items.Weird_Substance
	elif chooseItem == Items.Power:
		quick_print('Power required: ', required[Items.Power])
		required[Items.Power] = required[Items.Power]
		required[Items.Carrot] = get_cost(Entities.Sunflower)[Items.Carrot] * required[Items.Power]
		quick_print('Power required: ', required[Items.Power])
		quick_print('Need Carrot for Power: ', required[Items.Carrot])
		if current[Items.Carrot] < required[Items.Carrot]:
			chooseItem = Items.Carrot

	if debug:
		quick_print('')
		quick_print('Current request of Hay: ' + str(required[Items.Hay]))
		quick_print('Current request of Wood: ' + str(required[Items.Wood]))
		quick_print('Current request of Carrot: ' + str(required[Items.Carrot]))
		quick_print('Current request of Pumpkin: ' + str(required[Items.Pumpkin]))
		quick_print('Current request of Cactus: ' + str(required[Items.Cactus]))
		quick_print('Current request of Weird_Substance: ' + str(required[Items.Weird_Substance]))
		quick_print('Current request of Gold: ' + str(required[Items.Gold]))
		quick_print('Current request of Power: ' + str(required[Items.Power]))

	return required, chooseItem

def currentAmounts(debug, current):
	current[Items.Hay] = num_items(Items.Hay)
	current[Items.Wood] = num_items(Items.Wood)
	current[Items.Carrot] = num_items(Items.Carrot)
	current[Items.Pumpkin] = num_items(Items.Pumpkin)
	current[Items.Cactus] = num_items(Items.Cactus)
	current[Items.Weird_Substance] = num_items(Items.Weird_Substance)
	current[Items.Gold] = num_items(Items.Gold)
	current[Items.Power] = num_items(Items.Power)
	
	if debug:
		quick_print('')
		quick_print('Current amount of Hay: ' + str(current[Items.Hay]))
		quick_print('Current amount of Wood: ' + str(current[Items.Wood]))
		quick_print('Current amount of Carrot: ' + str(current[Items.Carrot]))
		quick_print('Current amount of Pumpkin: ' + str(current[Items.Pumpkin]))
		quick_print('Current amount of Cactus: ' + str(current[Items.Cactus]))
		quick_print('Current amount of Weird_Substance: ' + str(current[Items.Weird_Substance]))
		quick_print('Current amount of Gold: ' + str(current[Items.Gold]))
		quick_print('Current amount of Power: ' + str(current[Items.Power]))
	
	return current

def checkIfCanUnlock(current):
	data = collectUnlocks()
	item = []
	upgrades = []
	quick_print('')
	for i in range(len(data)):
		item = data[i][0]
		upgrades = data[i][1]
		length = len(upgrades)
		for key in upgrades:
			ready = 0
			if (key == Items.Hay):
				if (current[Items.Hay] > upgrades[Items.Hay]):
					ready += 1
			if (key == Items.Wood):
				if (current[Items.Wood] > upgrades[Items.Wood]):
					ready += 1
			if (key == Items.Carrot):
				if (current[Items.Carrot] > upgrades[Items.Carrot]):
					ready += 1
			if (key == Items.Pumpkin):
				if (current[Items.Pumpkin] > upgrades[Items.Pumpkin]):
					ready += 1
			if (key == Items.Cactus):
				if (current[Items.Cactus] > upgrades[Items.Cactus]):
					ready += 1
			if (key == Items.Weird_Substance):
				if (current[Items.Weird_Substance] > upgrades[Items.Weird_Substance]):
					ready += 1
			if (key == Items.Gold):
				if (current[Items.Gold] > upgrades[Items.Gold]):
					ready += 1
			if (key == Items.Power):
				if (current[Items.Power] > upgrades[Items.Power]):
					ready += 1
			if ready == length:
				unlock(item)
				quick_print('Unlocked: ', item)

def checkIfSquare(num):
	bool = False
	for i in range(num, 0 , -1):
		if i**2 == num:
			bool = True
	return bool

def droneIntervals(fieldWidth, fieldHeight):
	maxDrones = max_drones()
	array = []
	mapPrint = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
	if maxDrones > 1:
		if checkIfSquare(maxDrones):
			divX = fieldWidth / maxDrones**0.5
			divY = fieldHeight / maxDrones**0.5
			for i in range(maxDrones):
				array.append([i%maxDrones**0.5*divX, (i%maxDrones**0.5+1)*divX - 1, i//maxDrones**0.5*divY, (i//maxDrones**0.5+1)*divY - 1])
		else:
			divX = fieldWidth / (maxDrones / 2)
			divY = fieldHeight / 2
			for i in range(maxDrones):
				array.append([i%(maxDrones/2) * divX, (i%(maxDrones/2)+1) * divX - 1, i//(maxDrones/2) * divY, (i//(maxDrones/2)+1) * divY - 1])
		
	else:
		array.append([0, fieldWidth - 1 ,0 , fieldHeight - 1])

	if False:
		for y in range(fieldHeight):
			for x in range(fieldWidth):
				for i in range(len(array)):
					if x >= array[i][0] and x <= array[i][1] and y >= array[i][2] and y <= array[i][3]:
						mapPrint[x] = i
			quick_print(mapPrint)
		quick_print(array)

	return array
