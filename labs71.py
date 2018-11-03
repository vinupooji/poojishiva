import random
r={1:'r',2:'p',3:'s'}
c=r[random.randint(1,3)]
a=0
p=0
while a<3 and p<3
	b=input("enter your choice r/p/s")
	print("you choose",b,"computer chose",c)
	if(b==c):
		print("draw")
	elif((b=='r') and (c=='p')):
		print("u loose")
		
	elif((b=='r') and (c=='s')):
		print("u win")
	elif((b=='p') and (c=='r')):
		print("u win")
	elif((b=='p') and (c=='s')):
		print("u loose")
	elif((b=='s') and (c=='r')):
		print("u lose")
	elif((b=='s') and (c=='p')):
		print("u win")
	else:
		break