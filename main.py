""" You must face boring mathematics in your student life like====  If 15 workers cultivate 18 acres area
    in 5 days then, how many days will take 10 workers to cultivate 12 acres area ? 
    So I've created this tool to preserve your times for chating in Social Medias....LOL,Just kidding.'"""

import time
time.sleep(2.2)
print('<<<<<====================================>>>>>')
print("----------[Welcome to my Math Class]----------")
print('<<<<<====================================>>>>>')
print('')
time.sleep(1.3)
arij_constant = 1
while True:
	
	print('(((===========================)))')
	print('   What solution do you want ?')
	print('(((===========================)))')
	time.sleep(1.2)
	print('[1] Workers                    [99] Exit')
	time.sleep(0.8)
	print('[2] Time ')
	time.sleep(0.8)
	print('[3] Worked_Place')
	time.sleep(0.8)
	print('')
	time.sleep(1.0)
	choice_first = int(input("👨‍💻️==> Enter the Choice[1 to 4 or 99]: "))
	print('')
	time.sleep(1.3)
	if choice_first == 1:
		print('==> Enter the given examples of Workers,Time & Worked_Place:')
		a = int(input('==> Enter Workers: '))
		print('')
		b = int(input('==> Enter Time: '))
		print('')
		c = int(input('==> Enter Worked_Place: '))
		print('')
		k = (b*a)/c
		time.sleep(0.8)
		print('==> Enter the value of 2nd_Time & 2nd_Worked_Place:')
		print('')
		b2 = int(input('==> Enter 2nd_Time: '))
		print('')
		c2 = int(input('==> Enter 2nd_Worked_Place: '))
		print('')
		print('The amount of Workers is:')
		time.sleep(0.8)
		a2 = (k*c2)/b2
		print(a2)
		print('')
	elif choice_first == 2 :
		print('==> Enter the given examples of Workers,Time & Worked_Place:')
		print('')
		a = int(input('==> Enter Workers: '))
		print('')
		b = int(input('==> Enter Time: '))
		print('')
		c = int(input('==> Enter Worked_Place: '))
		print('')
		k = (b*a)/c
		time.sleep(0.8)
		print('==> Enter the value of 2nd_Workers & 2nd_Worked_Place:')
		print('')
		a2 = int(input('==> Enter 2nd_Workers: '))
		print('')
		c2 = int(input('==> Enter 2nd_Worked_Place: '))
		print('')
		b2 = (k*c2)/a2
		print('The amount of Time is:')
		time.sleep(0.8)
		print(b2)
		print('')
	elif choice_first == 3 :
		print('==> Enter the given examples of Workers,Time & Worked_Place:\n')
		print('')
		a = int(input('==> Enter Workers: '))
		print('')
		b = int(input('==> Enter Time: '))
		print('')
		c = int(input('==> Enter Worked_Place: '))
		print('')
		k = (b*a)/c
		time.sleep(0.8)
		print('==> Enter the value of 2nd_Workers & 2nd_Time:\n')
		print('')
		a2 = int(input('==> Enter 2nd_Workers: '))
		print('')
		b2 = int(input('==> Enter 2nd_Time: '))
		print('')
		c2 = (a2*b2)/k
		print('The amount of 2nd_Worked_Place is :')
		time.sleep(0.8)
		print(c2)
		print('')
		
	elif choice_first == 99:
		print('Exiting....')
		time.sleep(2.0)
		exit()
		
	else :
		print('Error! Invalid Input. Try again...')

arij_constant += 1



