a=[1,2,3,4,5,6,7,8,9]
def printboard():
	print(a[0],'|',a[1],'|',a[2],'|')
	print("-----------")
	print(a[3],'|',a[4],'|',a[5],'|')
	print("-----------")
	print(a[6],'|',a[7],'|',a[8],'|')

playeroneturn = True
while True:
	printboard()
	p=int(input("choose your place >>"))
	if(p in a):
		if playeroneturn:
			#p = input("choose your place, player 1>>")
			a[p-1] = 'X'
			playeroneturn = not playeroneturn
		else:
			#p = input("choose your place, player 2>>")
			a[p-1] = 'O'
			playeroneturn = not playeroneturn
			#checking winning conditions
		#checking for row winning conditions
		for i in (0,3,6):
			if(a[i]==a[i+1] and a[i]==a[i+2]):
				if a[i]=='X':
					print("player 1 wins!!")
					exit()
				else:
					print("player 2 wins!!")
					exit()
		#checking for column winning conditions
		for i in range(3):
			if(a[i]==a[i+3] and a[i]==a[i+6]):
				if a[i]=='X':
					print("player 1 wins!!")
					exit()
				else:
					print("player 2 wins!!")
					exit()
		#checking for diagonal winning conditions
		for i in range(0,4,8):
			if(a[i]==a[i+4] and a[i]==a[i+8]):
				if a[i]=='x':
					print("player one wins")
					exit()
				else:
					print("player 2 wins")
					exit()
		for i in range(2,4,6):
			if(a[i]==a[i+2] and a[i]==a[i+4]):
				if a[i]=='x':
					print("player one wins")
					exit()	
				else:
					print("player 2 wins")
					exit()
		#checking for draw condition
	else:
		continue