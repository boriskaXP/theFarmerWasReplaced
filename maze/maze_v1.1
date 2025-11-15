from wayToGoFile import *
from symboLib import *

wayArray = []
directions = [South, North, West, East]

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
			if (wayArray[findWayIndex(ix, iy, fieldWidth, fieldHeight)][2] != ' ') and (wayArray[findWayIndex(ix, iy, fieldWidth, fieldHeight)][2] != '•'):
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

def findRoute(targetX, targetY, X, Y, fieldWidth, fieldHeight):
	
	global wayArray
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
			deleteCount = []
			if found:
				break
			if (cur[nn][0] >= 0) and (cur[nn][0] < fieldWidth) and (cur[nn][1] >= 0) and (cur[nn][1] < fieldHeight):
				symbol = wayArray[findWayIndex(cur[nn][0], cur[nn][1], fieldWidth, fieldHeight)][2]
				directs = availableDirections(symbol)
			else:
				symbol = ''
				directs = []
			if (wayArray[findWayIndex(get_pos_x(), get_pos_y(), fieldWidth, fieldHeight)][2] == '•'):
				for nnn in range(4):
					if can_move(directions[nnn]):
						found = True
						route = [directions[nnn]]
						break
			elif len(directs) > 0:
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
	
