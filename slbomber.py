#Script By Sandaru Ashen https://t.me/Sl_Sanda_Ru
from os import name,system
system('git tash && git pull')
from time import sleep
from sys import stdout
from random import randrange,choice,choices
from api import *
cle = 'clear' if name == 'posix' else 'cls'
run = 'python3 slbomber.py' if name == 'posix' else 'python.exe slbomber.py'
try:
	from colorama import Fore,init
except ModuleNotFoundError:
	system('pip3 install colorama')
	from colorama import Fore,init
init(autoreset=True)
system(cle)
#Colors
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
logo=f'{choice(fore)}\x1b[1m\t\t   _________.__\n                  /   _____/|  |\n                  \\_____  \\ |  |\n                  /        \\|  |__\n                 /_______  /|____/\n   __________            \\/___.\n   \\______   \\ ____   _____\\_ |__   ___________\n    |    |  _//  _ \\ /     \\| __ \\_/ __ \\_  __ \\\n    |    |   (  <_> )  Y Y  \\ \\_\\ \\  ___/|  | \\/\n    |______  /\\____/|__|_|  /___  /\\___  >__|\n           \\/             \\/    \\/     \\/ {choice(fore)}v.1.7\n\t\t{choice(fore)}[+] By Sandaru Ashen'
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
print(f'{bold}\t\t{lired}1.Start Bomber\n\t\t{liyel}2.Start Caller\n\t\t{gre}3.About\n\t\t{limag}4.Exit')
def prsent(count,num):
	stdout.write('\r' +choice(fore) +bold+'\t[*]'+' Bombing '+str(num)+'\t'+str(count)+' Sent')
	stdout.flush()
def spinner():
	l=['|','/','-','\\']
	for i in l+l+l:
		stdout.write('\r'+bold+liyel+'[*] Checking Your Internet Connection  '+choice(fore)+i)
		stdout.flush()
		sleep(0.2)
sleep(0.3)
while True:
	try:
		cho=int(input(cya+bold+'Enter Your Choice: '))
		if cho > 0 and cho <5:
			break
		else:
			Print(lired+bold+'[!] Please Enter A Correct Choice!')
	except:
			print(lired+bold+'[!] Incorrect Choice')
if cho==1:
	sleep(0.4)
	system(cle)
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	try:
		spinner()
		get('https://a9c3af23099293570b4ae5a5c60e0762.m.pipedream.net')
		print(ligre+bold+'\n[+] Connection Successful!')
		sleep(1.5)
		system(cle)
		print(bar+'\n')
		print(logo)
		print(bar+'\n')
	except Exception:
		sleep(0.4)
		print(lired+bold+'\n[!] You Aren\'t Connected To Internet Or Something Wrong With The Network!')
		sleep(0.3)
		print(lired+bold+'[!] Please Connect To Internet To Continue...')
		sleep(0.3)
		input(lired+bold+'[!] Exiting...\nPress Enter To Continue...')
		exit()
	while True:
		try:
			num=int(input(bold+'Enter The Target No(07xxxxxxxx): '))
			num='0'+str(num)
			if len(num) == 10 and str(num)[0:3] in ('070','071','072','074','075','076','077','078'):
				break
			else:
				print(lired + 'Please Enter A Correct Number!')
				continue
		except ValueError:
			print(lired + 'Please Enter A Phone Number Not Letters!')
			continue
	sleep(0.4)
	while True:
		times=input(bold+liyel+'How Many Messages (U) To Unlimited:')
		if times.isnumeric() or times == 'U' or	times == 'u':
			break
		else:
			print(bold+lired+'[!] Enter A Correct Amount Or \'U\' For Unlimited')
	sleep(0.4)
	while True:
		delay=input(bold+limag+'Enter Delay Time (In Seconds)\n\t\t[Recomended 5]:')
		if delay.isnumeric() and int(delay) > 0:
			delay=float(delay)
			break
		elif delay=='0':
			print(bold+lired+'[!] Value Must Be More Than 0')
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
	print(yel+bold+'\tPress Ctrl+c To Terminate The Bombing')
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
											eclass1(num,delay)
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
																		domin(num,delay)
																		count+=1
																		prsent(count,num)
																		if count< int(times):
																			eclass2(num,delay)
																			count+=1
																			prsent(count,num)
																			if count<int(times):
																				oli(num,delay)
																				count+=1
																				prsent(count,num)
																				if count<int(times):
																					eclass3(num,delay)
																					count+=1
																					prsent(count,num)
																					if count<int(times):
																						eclass4(num,delay)
																						count+=1
																						prsent(count,num)
																						if count<int(times):
																							eclass5(num,delay)
																							count+=1
																							prsent(count,num)
																							if count<int(times):
																								eclass6(num,delay)
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
				eclass2(num,count)
				count+=1
				prsent(count,num)
				kangaroo(num,delay)
				count+=1
				prsent(count,num)
				pat(num,delay)
				count+=1
				prsent(count,num)
				eclass1(num,delay)
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
				domin(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=1
				prsent(count,num)
				eclass3(num,count)
				count+=1
				prsent(count,num)
				eclass4(num,count)
				count+=1
				prsent(count,num)
				eclass5(num,count)
				count+=1
				prsent(count,num)
				eclass6(num,count)
				count+=1
				prsent(count,num)
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
																eclass1(num,delay)
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
																			domin(num,delay)
																			count+=1
																			prsent(count,num)
																			if count< int(times):
																				eclass2(num,delay)
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
																							if count<int(times):
																								eclass3(num,delay)
																								count+=1
																								prsent(count,num)
																								if count<int(times):
																									eclass4(num,delay)
																									count+=1
																									prsent(count,num)
																									if count<int(times):
																										eclass5(num,delay)
																										count+=1
																										prsent(count,num)
																										if count<int(times):
																											eclass6(num,delay)
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
				eclass1(num,delay)
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
				eclass2(num,count)
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
				domin(num,delay)
				count+=1
				prsent(count,num)
				moba(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=1
				prsent(count,num)
				eclass3(num,count)
				count+=1
				prsent(count,num)
				eclass4(num,count)
				count+=1
				prsent(count,num)
				eclass5(num,count)
				count+=1
				prsent(count,num)
				eclass6(num,count)
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
										  eclass1(num,delay)
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
  																		domin(num,delay)
  																		count+=1
  																		prsent(count,num)
  																		if count< int(times):
  																			eclass2(num,delay)
  																			count+=1
  																			prsent(count,num)
  																			if count<int(times):
  																				oli(num,delay)
  																				count+=1
  																				prsent(count,num)
  																				if count<int(times):
  																					eclass3(num,delay)
  																					count+=1
  																					prsent(count,num)
  																					if count<int(times):
  																						eclass4(num,delay)
  																						count+=1
  																						prsent(count,num)
  																						if count<int(times):
  																							eclass5(num,delay)
  																							count+=1
  																							prsent(count,num)
  																							if count<int(times):
  																								eclass6(num,delay)
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
				eclass2(num,count)
				count+=1
				prsent(count,num)
				kangaroo(num,delay)
				count+=1
				prsent(count,num)
				pat(num,delay)
				count+=1
				prsent(count,num)
				eclass1(num,delay)
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
				domin(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=1
				prsent(count,num)
				eclass3(num,count)
				count+=1
				prsent(count,num)
				eclass4(num,count)
				count+=1
				prsent(count,num)
				eclass5(num,count)
				count+=1
				prsent(count,num)
				eclass6(num,count)
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
									  eclass1(num,delay)
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
  																domin(num,delay)
  																count+=1
  																prsent(count,num)
  																if count< int(times):
  																	eclass2(num,delay)
  																	count+=1
  																	prsent(count,num)
  																	if count<int(times):
  																		oli(num,delay)
  																		count+=1
  																		prsent(count,num)
  																		if count<int(times):
  																			eclass3(num,delay)
  																			count+=1
  																			prsent(count,num)
  																			if count<int(times):
  																				eclass4(num,delay)
  																				count+=1
  																				prsent(count,num)
  																				if count<int(times):
  																					eclass5(num,delay)
  																					count+=1
  																					prsent(count,num)
  																					if count<int(times):
  																						eclass6(num,delay)
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
				eclass1(num,delay)
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
				eclass2(num,count)
				count+=1
				prsent(count,num)
				domin(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=1
				prsent(count,num)
				eclass3(num,count)
				count+=1
				prsent(count,num)
				eclass4(num,count)
				count+=1
				prsent(count,num)
				eclass5(num,count)
				count+=1
				prsent(count,num)
				eclass6(num,count)
				count+=1
				prsent(count,num)
	print('\n'+bar+'\n')
	sleep(0.8)
	print(f'{bold}{ligre}\t[+] Bombing Successful')
	sleep(0.6)
	ag=input(f'\t{bold}{choice(fore)}[?] Run The Bomber Again?(y/n) ')
	if ag == 'Y' or ag == 'y':
		system(run)
	else:
		exit()
elif cho == 2:
	sleep(0.5)
	system(cle)
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	try:
		spinner()
		post('https://a9c3af23099293570b4ae5a5c60e0762.m.pipedream.net')
		print(ligre+bold+'\n[+] Connection Successful!')
		sleep(1.3)
		system(cle)
		print(bar+'\n')
		print(logo)
		print(bar+'\n')
	except Exception:
		sleep(0.4)
		print(lired+bold+'\n[!] You Aren\'t Connected To Internet Or Something Wrong With The Network!')
		sleep(0.3)
		print(lired+bold+'[!] Please Connect To Internet To Continue...')
		sleep(0.3)
		input(lired+bold+'[!] Exiting...\nPress Enter To Continue...')
		exit()
	while True:
		try:
			num=int(input(bold+'Enter The Target No(0xxxxxxxxx): '))
			num='0'+str(num)
			if len(num) == 10 and str(num)[0:3] in ('070','031','011','071','072','074','075','076','077','078'):
				break
			else:
				print(lired + 'Please Enter A Correct Number!')
				continue
		except ValueError:
			print(lired + 'Please Enter A Phone Number Not Letters!')
			continue
	con(num)
	a=call(num)
	if a is True:
		print(bold+ligre+'[+] Call Sent')
		sleep(0.9)
		qq=input(bold+choice(fore)+'[?] Do You Want To Go To Main Menu? (y/n)')
		if qq == 'Y' or qq.lower() == 'y':
			system(run)
		else:
			exit()
	else:
		print(bold+lired+'[!] Call Limit Exceeded!')
		sleep(0.7)
		print(bold+red+'Try Again In 6 Hours!')
		qq=input(bold+choice(fore)+'[?] Do You Want To Go To Main Menu? (y/n)')
		if qq == 'Y' or qq.lower() == 'y':
			exit()
		else:
			system(run)
elif cho == 3:
	system(cle)
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	print(f'{bold}\t\t\tAbout\n{choice(fore)}[+] Special Thanks To Packet Sniffing Software\n{choice(fore)}[+] If You Have Any Complains Or Future Requests Contact Me @ https://t.me/Sl_Sanda_Ru\n{choice(fore)}[+] Never Use The Script To Cause Harm/Discomfort/Trouble To Others\n{choice(fore)}[!] If You Know More Websites And Apps That Use SMS Verification Please Inform Me')
	input(f'{bold}{choice(fore)}\t[+] Press ENTER To Go Back To Main Menu')
	system(run)
else:
	exit()
