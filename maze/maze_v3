from symboLib import *

wayArray = []
directions = [South, North, West, East]
rightTurn = {South:West, North:East, West:North, East:South}
leftTurn = {South:East, North:West, West:South, East:North}
opposite = {South:North, North:South, West:East, East:West}

def findWayIndex(fx, fy, fieldWidth, fieldHeight):
	return fx * fieldWidth + fy 

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
				symbol = wayArray[findWayIndex(cur[nn][0], cur[nn][1], fieldWidth, fieldHeight)][2]
				directs = availableDirections(symbol)
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
							posptfds=0
							deleteCount.append(nn+nnn)
					for d in range(len(deleteCount), 0, -1):
						cur.pop(deleteCount[d - 1])

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
			X = get_pos_x()
			Y = get_pos_y()
			direct = []
			for n in range(len(directions)):
				if can_move(directions[n]):
					direct.append(directions[n])
			wayArray[findWayIndex(X, Y, fieldWidth, fieldHeight)][2] = chooseSymbol(direct)

	completed = False
	if level == lvl:
		completed = True
		harvest()
	else:
		if (level == 1) or (level % 10 == 0):
			a = []
			quick_print('Print map')
			for iy in range(fieldWidth):
				a = ''
				for ix in range(fieldHeight):
					a += wayArray[findWayIndex(ix, fieldWidth - 1 - iy, fieldWidth, fieldHeight)][2]
				quick_print(a)
			quick_print('Map Done')
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
		level += 1

	return completed, level, wayArray

def searchMaze_v3(lvl, fieldWidth, fieldHeight):
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
				completed, level, wayArray = findTreasury(level, lvl, wayArray, fieldWidth, fieldHeight)
		else:
			completed, level, wayArray = findTreasury(level, lvl, wayArray, fieldWidth, fieldHeight)
