def chooseSymbol(dir):
	symbol = ''
	if len(dir) == 0:
		symbol = ' '
	elif len(dir) == 1:
		if dir [0] == South:
			symbol = '↑'
		elif dir [0] == North:
			symbol = '↓'
		elif dir [0] == West:
			symbol = '→'
		elif dir [0] == East:
			symbol = '←'
	elif len(dir) == 2:
		if (dir[0] == South) and (dir[1] == North):
			symbol = '│'
		elif (dir[0] == West) and (dir[1] == East):
			symbol = '─'
		elif (dir[0] == North) and (dir[1] == East):
			symbol = '└'
		elif (dir[0] == South) and (dir[1] == West):
			symbol = '┐'
		elif (dir[0] == North) and (dir[1] == West):
			symbol = '┘'
		elif (dir[0] == South) and (dir[1] == East):
			symbol = '┌'
	elif len(dir) == 3:
		if (dir[0] == South) and (dir[1] == North) and (dir[2] == East):
			symbol = '├'
		elif (dir[0] == North) and (dir[1] == West) and (dir[2] == East):
			symbol = '┴'
		elif (dir[0] == South) and (dir[1] == North) and (dir[2] == West):
			symbol = '┤'
		elif (dir[0] == South) and (dir[1] == West) and (dir[2] == East):
			symbol = '┬'
	elif len(dir) == 4:
		symbol = '┼'
	return symbol

def availableDirections(symbol):
	dir = []
	if symbol == ' ':
		dir = []
	elif symbol == '↑':
		dir = [South]
	elif symbol == '↓':
		dir = [North]
	elif symbol == '→':
		dir = [West]
	elif symbol == '←':
		dir = [East]
	elif symbol == '│':
		dir = [South, North]
	elif symbol == '─':
		dir = [West, East]
	elif symbol == '└':
		dir = [North, East]
	elif symbol == '┐':
		dir = [South, West]
	elif symbol == '┘':
		dir = [North, West]
	elif symbol == '┌':
		dir = [South, East]
	elif symbol == '├':
		dir = [South, North, East]
	elif symbol == '┴':
		dir = [North, West, East]
	elif symbol == '┤':
		dir = [South, North, West]
	elif symbol == '┬':
		dir = [South, West, East]
	elif symbol == '┼':
		dir = [South, North, West, East]
	return dir
