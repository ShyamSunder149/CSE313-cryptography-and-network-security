def encrypt():
	p = input("Enter Plaintext:")
	d = int(input("Enter depth:"))
	if d > len(p):
		print('attack not possible')
		exit()
	else:
		grid = [[" " for i in range(len(p))] for j in range(d)]
		flag = 0
		row = 0
		for i in range(len(p)):
			grid[row][i] = p[i]
			if row == 0:
				flag = 0
			elif row == d-1:
				flag = 1
			if flag == 0:
				row += 1
			else:
				row -= 1
	s = ''
	for i in range(d):
		s+= (''.join(grid[i]))
	print(s)

encrypt()
