import random
from time import sleep
from os import system

a=[1,2,3,4,5,6,7,8,9]
def printboard():
	system('clear')
	print(a[0],'|',a[1],'|',a[2])
	print('------------')
	print(a[3],'|',a[4],'|',a[5])
	print('------------')
	print(a[6],'|',a[7],'|',a[8])
	print('------------')

def possibilities():
	I = []
	for i in a:
		if(i!='X' and i!='O'):
			I.append(i)
	return I

def compturn():
	temp = possibilities()
	k = random.choice(temp)
	return k

p1=true
while True:
	printboard()
	if p1:
		p = int(input("choose ur place"))
		if(p in a):
			print("player 1 chose",p)
			a[p-1]='X'
			p1 = not p1
	else:
		w=compturn()
		print("computer chose",w)
		sleep(3)
		a[int(w)-1]='O'
		p1 = not p1

	for i in (0,3,6):
		if(a[i]==a[i+1] and a[i]==a[i+2]):
			printboard()
			if(a[i]=='X'):
				print("player 1 wins")
				exit()
			else:
				print("computer wins")
				exit()

	for i in range(3):
		if(a[i]==a[i+3] and a[i]==a[i+6]):
			printboard()
			if(a[i]=='X'):
				print("player 1 wins")
				exit()
			else:
				print("computer wins")
				exit()

	if(a[0]==a[4] and a[0]==a[8])