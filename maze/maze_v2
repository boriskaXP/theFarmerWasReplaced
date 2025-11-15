from symboLib import *

wayArray = []
directions = [South, North, West, East]
rightTurn = {South:West, North:East, West:North, East:South}
leftTurn = {South:East, North:West, West:South, East:North}
opposite = {South:North, North:South, West:East, East:West}

def findWayIndex(fx, fy, fieldWidth, fieldHeight):
	return fx * fieldWidth + fy 

def checkDoneArray(array, fieldWidth, fieldHeight):
	bool = True
	for ax in range(fieldWidth):
		for ay in range(fieldHeight):
			if array[findWayIndex(ax, ay, fieldWidth, fieldHeight)][2] == ' ':
				bool = False
	return bool

def findWay(fieldWidth, fieldHeight):
	
	global wayArray
	global directions
	
	searchX = 0
	searchY = 0
	found = False
	for ix in range(fieldWidth):
		if found:
			break
		for iy in range(fieldHeight):
			if found:
				break
			if (wayArray[findWayIndex(ix, iy, fieldWidth, fieldHeight)][2] != ' '):
				dir = availableDirections(wayArray[findWayIndex(ix, iy, fieldWidth, fieldHeight)][2])
				for n in range(len(dir)):
					if (dir[n] == South) and ((wayArray[findWayIndex(ix, iy - 1, fieldWidth, fieldHeight)][2] == ' ') and (wayArray[findWayIndex(ix, iy - 1, fieldWidth, fieldHeight)][2] != '•')):
						found = True
						searchX = ix
						searchY = iy - 1
						break
					if (dir[n] == North) and ((wayArray[findWayIndex(ix, iy + 1, fieldWidth, fieldHeight)][2] == ' ') and (wayArray[findWayIndex(ix, iy, fieldWidth, fieldHeight)][2] != '•')):
						found = True
						searchX = ix
						searchY = iy + 1
						break
					if (dir[n] == West) and ((wayArray[findWayIndex(ix - 1, iy, fieldWidth, fieldHeight)][2] == ' ') and (wayArray[findWayIndex(ix - 1, iy, fieldWidth, fieldHeight)][2] != '•')):
						found = True
						searchX = ix - 1
						searchY = iy
						break
					if (dir[n] == East) and ((wayArray[findWayIndex(ix + 1, iy, fieldWidth, fieldHeight)][2] == ' ') and (wayArray[findWayIndex(ix + 1, iy, fieldWidth, fieldHeight)][2] != '•')):
						found = True
						searchX = ix + 1
						searchY = iy
						break
	if found:
		return searchX, searchY
	else:
		return None, None

def shiftCoord(shiftX, shiftY, way):
	if way == South:
		shiftY -= 1
	if way == North:
		shiftY += 1
	if way == West:
		shiftX -= 1
	if way == East:
		shiftX += 1
	return shiftX, shiftY

def findRoute(wayArray, targetX, targetY, X, Y, fieldWidth, fieldHeight):

	global directions

	gone = []
	for ix in range(fieldWidth):
		for iy in range(fieldHeight):
			gone.append([ix+1, iy+1, ''])
	route = []
	cur = [[]]
	cur[0] = [X, Y]
	gone[findWayIndex(X, Y, fieldWidth, fieldHeight)][2] = 'X'
	found = False
	for n in range(fieldWidth * fieldHeight):
		if found:
			break
		num = len(cur)
		for nn in range(num):
			if nn < len(cur):
				deleteCount = []
				if found:
					break
				if (cur[nn][0] >= 0) and (cur[nn][0] < fieldWidth) and (cur[nn][1] >= 0) and (cur[nn][1] < fieldHeight):
					symbol = wayArray[findWayIndex(cur[nn][0], cur[nn][1], fieldWidth, fieldHeight)][2]
					directs = availableDirections(symbol)
				else:
					symbol = ''
					directs = []
				if len(directs) > 0:
					for nnn in range(len(directs) - 1):
						tmp = []
						for m in range(len(cur[nn])):
							tmp.append(cur[nn][m])
						cur.insert(nn + 1, tmp)
					for nnn in range(len(directs)):
						cur[nn + nnn][0], cur[nn + nnn][1] = shiftCoord(cur[nn + nnn][0], cur[nn + nnn][1], directs[nnn])
						if gone[findWayIndex(cur[nn + nnn][0], cur[nn + nnn][1], fieldWidth, fieldHeight)][2] != 'X':
							gone[findWayIndex(cur[nn + nnn][0], cur[nn + nnn][1], fieldWidth, fieldHeight)][2] = 'X'
							cur[nn + nnn].append(directs[nnn])
							if (cur[nn + nnn][0] == targetX) and (cur[nn + nnn][1] == targetY):
								found = True
								route = cur[nn + nnn]
								route.pop(0)
								route.pop(0)
								break
						else:
							deleteCount.append(nn+nnn)
					for d in deleteCount:
						cur.pop(d)
	return route, wayArray

def getMap(fast, wayArray, fieldWidth, fieldHeight):
	forward = North
	startX = get_pos_x()
	startY = get_pos_y()

	for direction in directions:
		if can_move(direction):
			forward = direction
	move(forward)

	counter = 0
	completed = False
	while counter < 2:
		X = get_pos_x()
		Y = get_pos_y()
		trX, trY = measure()
		
		if fast:
			if (trX == X) and (trY == Y):
				completed = True
				harvest()
				break

		direct = []
		for n in range(len(directions)):
			if can_move(directions[n]):
				direct.append(directions[n])
		wayArray[findWayIndex(X, Y, fieldWidth, fieldHeight)][2] = chooseSymbol(direct)

		if (X == startX) and (Y == startY):
			counter += 1
		if can_move(rightTurn[forward]):
			forward = rightTurn[forward]
		elif not can_move(forward):
			if can_move(leftTurn[forward]):
				forward = leftTurn[forward]
			else:
				forward = opposite[forward]
		move(forward)

	a = []
	quick_print('Print map')
	for iy in range(fieldWidth):
		a = ''
		for ix in range(fieldHeight):
			a += wayArray[findWayIndex(ix, fieldWidth - 1 - iy, fieldWidth, fieldHeight)][2]
		quick_print(a)
	quick_print('Map Done')

	return completed, wayArray

def findTreasury(level, lvl, wayArray, fieldWidth, fieldHeight):
	X = get_pos_x()
	Y = get_pos_y()
	trX, trY = measure()
	quick_print('Treasury coords: ', trX, trY)
	
	route, wayArray = findRoute(wayArray, trX, trY, X, Y, fieldWidth, fieldHeight)
	if len(route) > 0:
		for n in range(len(route)):
			move(route[n])

	completed = False
	if level == lvl:
		completed = True
		harvest()
	else:
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
		level += 1

	return completed, level

def searchMaze_v2(lvl, fieldWidth, fieldHeight):
	level = 1
	completed = False
	wayArray = []
	for x in range(fieldWidth):
		for y in range(fieldHeight):
			wayArray.append([x+1, y+1, ' '])
	while not completed:
		quick_print('Level:' + str(level))
		if level == 1:
			completed, wayArray = getMap(level == lvl, wayArray, fieldWidth, fieldHeight)
			if not completed:
				completed, level = findTreasury(level, lvl, wayArray, fieldWidth, fieldHeight)
		else:
			completed, level = findTreasury(level, lvl, wayArray, fieldWidth, fieldHeight)

def searchMaze(fieldWidth, fieldHeight):
	
	global wayArray
	global directions

	wayArray = []

	i = 0
	for x in range(fieldWidth):
		for y in range(fieldHeight):
			wayArray.append([x+1, y+1, ' '])
			i += 1

	done = False
	while not done:
		X = get_pos_x()
		Y = get_pos_y()

		treasureX, treasureY = measure()

		if (X == treasureX) and (Y == treasureY):
			harvest()
			break

		direct = []
		for n in range(len(directions)):
			if can_move(directions[n]):
				direct.append(directions[n])
		wayArray[findWayIndex(X, Y, fieldWidth, fieldHeight)][2] = chooseSymbol(direct)

		sX, sY = findWay(fieldWidth, fieldHeight)
		route, wayArray = findRoute(sX, sY, X, Y, fieldWidth, fieldHeight)
		if len(route) > 0:
			for n in range(len(route)):
				move(route[n])
		done = checkDoneArray(wayArray, fieldWidth, fieldHeight)

	if done:
		X = get_pos_x()
		Y = get_pos_y()
		treasureX, treasureY = measure()
		route, wayArray = findRoute(treasureX, treasureY, X, Y, fieldWidth, fieldHeight)
		if len(route) > 0:
			for n in range(len(route)):
				move(route[n])

		a = []
		print('Print map')
		for iy in range(fieldWidth):
			a = ''
			for ix in range(fieldHeight):
				a += wayArray[findWayIndex(ix, fieldWidth - 1 - iy, fieldWidth, fieldHeight)][2]
			print(a)
		print('Map Done')

		harvest()
	
