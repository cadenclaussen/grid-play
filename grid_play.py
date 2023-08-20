def ifwin(cordinants, cordinants2, charecter):
	if board[cordinants[0]][cordinants[1]] != charecter:
		return False
	if board[cordinants2[0]][cordinants2[1]] != charecter:
		return False
	return True

you_can_win = ifwin()


