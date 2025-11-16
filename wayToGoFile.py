from autoUnlock import *

def resetPosition(interval, current):
	x0 = interval[0]
	x1 = interval[1]
	y0 = interval[2]
	y1 = interval[3]
	while(get_pos_x() < x0):
			move(East)
	while(get_pos_x() > x0):
			move(West)
	while(get_pos_y() < y0):
			move(North)
	while(get_pos_y() > y0):
			move(South)
	current = currentAmounts(False, current)
	return current

def wayToGo(interval, currentWay, current):
	x0 = interval[0]
	x1 = interval[1]
	y0 = interval[2]
	y1 = interval[3]
	x = get_pos_x()
	y = get_pos_y()
	currentWayY = currentWay[0]
	currentWayX = currentWay[1]
	moveDone = False
	if (x < x0) or (x > x1) or (y < y0) or (y > y1):
		current = resetPosition(interval, current)
		moveDone = True

	x = get_pos_x()
	y = get_pos_y()

	if not moveDone and ((currentWayY == North) and (y < y1)) or ((currentWayY == South) and (y > y0)):
		move(currentWayY)
		moveDone = True
	if not moveDone and (currentWayY == North) and (y == y1):
		currentWayY = South
		if x == x1:
			current = resetPosition(interval, current)
		else:
			move(currentWayX)
		moveDone = True
	if not moveDone and (currentWayY == South) and (y == y0):
		currentWayY = North
		if x == x1:
			current = resetPosition(interval, current)
		else:
			move(currentWayX)
		moveDone = True
	
	currentWay[0] = currentWayY
	currentWay[1] = currentWayX
	
	return currentWay, current
		
def wayToGo2(fieldWidth, fieldHeight):
	global currentWayX
	global currentWayY
	moveDone = False
	if not moveDone and ((currentWayY == North) and (get_pos_y() < fieldHeight - 1)) or (((currentWayY == South) and (get_pos_y() > 0))):
		move(currentWayY)
		moveDone = True
	if not moveDone and (currentWayY == North) and (get_pos_y() == fieldHeight - 1):
		currentWayY = South
		move(currentWayX)
		moveDone = True
	if not moveDone and (currentWayY == South) and (get_pos_y() == 0):
		currentWayY = North
		move(currentWayX)
		moveDone = True
