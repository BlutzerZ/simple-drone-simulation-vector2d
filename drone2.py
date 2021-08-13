'''
 SIMPLE DRONE SIMULATION 2

 Made By: BlutzerZ

 Features:
 	- Using Thread to simulate battery 
 	- Simulate loc of drone with simple (x,y)
 	- Shows a 2D vector image of the drone location [NEW]
 	- Controling drone with keyboard [NEW]

'''


from threading import Thread
import time, os, sys, keyboard

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def battery():
	i = 100
	global battery_status
	for x in range(i):
		i -= 1
		battery_status = i
		time.sleep(10)

		if battery_status == 0:
			print("\nbattery empty")
			time.sleep(1)
			print("turning off...")
			time.sleep(3)
			print("press ENTER to exit")
			sys.exit()

def limiter():
	global xy
	global reverse_y
	global fix_x
	global fix_y

	if xy[0] < 1:
		xy[0] = 1
	if xy[1] < 1:
		xy[1] = 1
		reverse_y = 25
	if xy[0] > fix_x:
		xy[0] = 25
	if xy[1] > fix_y:
		xy[1] = 25
		reverse_y = 1

def inputkeys():
	global xy
	global reverse_y

	if keyboard.is_pressed('d'):
		xy[0]+=1
	if keyboard.is_pressed('a'):
		xy[0]-=1
	if keyboard.is_pressed('w'):
		xy[1]-=1
		reverse_y +=1
	if keyboard.is_pressed('s'):
		xy[1]+=1
		reverse_y -=1

def command(command):
	global fly
	global batt

	if str(command) == "fly":
		fly = True
		batt = Thread(target = battery)
		batt.start()
		print('\n[>] flying your drone..')
		time.sleep(2)
		print('[>] Your drone now fly')
		time.sleep(1)
		print('[>] Now you can control with entering W, A, S, D')
		time.sleep(2)
		print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
		return

	else:
		print("\n[!] Wrong command or your drone aren't fly")
		print("[!] Please re-entering command or fly your drone")
		print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
		return

def main():
	global xy
	global fix_x
	global fix_y
	global reverse_y
	global fly
	global batt

	batt = 'idle'
	xy = [13,13]
	
	# To rotate y 180
	reverse_y = 13
	
	fix_x = 25
	fix_y = 25
	fly = False

	while True:

		clearConsole()
		
		if batt == 'idle':
			print("This is drone, input 'fly' to fly your drone")
			print("Use W,A,S,D to move drone")
			inputcommand = input("[COMMAND] = ") 
			command(inputcommand)

		elif batt.is_alive() == True:

			#INPUT KEY
			inputkeys()
			# LIMITER
			limiter()

			# DISPLAY
			print("\n\n\n\n\n")
			print("    /"+" /"*fix_x+" /")
			for i in range(fix_y):
				if xy[1] == i+1:
					print('    /'+"  "*(xy[0]-1)+' X'+('  ')*(fix_x-xy[0])+" /")
				else:
					print('    /'+"  "*fix_x+" /")
			print("    /"+" /"*fix_x+" /")

			print("     X = "+str(xy[0]))
			print("     Y = "+str(reverse_y))
			print("     [>] Remaining battery = "+ str(battery_status) +"%")

			continue
		else:
			sys.exit()

if __name__ == '__main__':
	main()