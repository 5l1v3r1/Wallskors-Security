# Create python3
# Author Brody404

import urllib.request  as urllib2
import re
import sys,os,time
import random

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

def info():
  os.system('clear')
  print("\n[ OS: ]")
  os.system("uname -o")
  print(G+"""
   Wallskors Security
   Contact : brodywallskors@gmail.com
   """)

def heads():
    global head
    head = E + F + """
 ____  _____ ____  ____  _   _    _    _  _______ 
|  _ \| ____|  _ \/ ___|| \ | |  / \  | |/ | ____|
| |_) |  _| | | | \___ \|  \| | / _ \ | ' /|  _|  
|  _ <| |___| |_| |___) | |\  |/ ___ \| . \| |___ 
|_| \_|_____|____/|____/|_| \_/_/   \_|_|\_|_____|
                                                  
""" + E

def tol():
	print(G+'''
	NAVIGATEUR INTERNET
  	'''+F+'''
  	1) Navigateur lynx
  	2) Navigateur w3m
	3) Sortir
  	'''+W+'''(---------+---------)
'''+E)
	try:
		v = input(G+'Wallskors/navigateur-»')
		if (v != 3):
			b = input('Insérez le lien du site->')
		else:
			Index()
	except:
		print('Exception levée... Mauvaise insertion')
		exit()
	
	if v == 'help':
		info()
	elif int(v) == 1:
		os.system('lynx '+b)
	elif int(v) == 2:
		os.system('w3m '+b)
	else:
		tol()

def un():
	os.system('php def.php')

def deux():
	print(head)
	print(G+'''
	Menu Bruteforce
  	'''+G+'''
  	1) Bruteforce Facebook
  	2) Bruteforce Instagram
  	3) Bruteforce FTP
  	4) Bruteforce Cpanel
  	5) Bruteforce mail
    6) Bruteforce Revenu
    7) Sortir
  	'''+H+'''(---------+---------)
    Tapez 'help' pour savoir comment utiliser le guide.'''+E)
	try:
		g = input(G+'Wallskors/brute-»')
	except:
		print('Exception rencontrée lors de la saisie\nVeuillez réessayer..')
		deux()

	if g == 'help':
		info()
	elif int(g) == 1:
		br = input('ID_Cible->')
		os.system('''python2 modules/fb.py '''+br+''' pas.txt''')
	elif int(g) == 2:
		lr = input('Utilisateur-> ')
		os.system('''python2 modules/ig.py '''+lr+''' pas.txt''')
	elif int(g) == 3:
		brut_ftp()
	elif int(g) == 4:
		df = input('Lien cpanel-> ')
		os.system('''perl modules/cp.pl '''+df+''' pas.txt''')
	elif int(g) == 5:
		brut_mail()
	elif int(g) == 6:
		to = input('Utilisateur revenu-> ')
		os.system('''python2 modules/rf.py '''+to+''' pas.txt''')
	elif int(g) == 7:
		print('''Vous retournez en arrière.''')
		Index()
	else:
		print("La saisie n'est pas valide, veuillez réessayer")
		deux()

def trois():
	print(F+'Ouverture de Lazymux...')
	time.sleep(3)
	os.system('python2 lazymux.py')

def quatre():
	print(G+'Ouverture de l\'outil de cryptage...')
	time.sleep(4)
	os.system('python2 rwds.py')

def cinq():
	os.system('clear')
	print(head)
	print('Cible du site web :')
	site = input(B+'Wallskors/cible»'+E)
	print('''Entrez le type de dos:
		1) Hard Dos
 		2) Low Dos''')
	level = int(input(B+'Wallskors»Dos»Level»'+E))
	if level == 1:
		os.system('python3 modules/dos2.py '+site)
	if level == 2:
		os.system('python3 modules/dos.py '+site)

def six():
    f
    os.system('clear')
    print('INFORMATIONS DE L\'APPAREIL')
    print('[ Status: ]')
    os.system('uname -n\n')
    print('\n[ Noyau: ]')
    os.system("uname -s")
    print("\n[ Version du noyau: ]")
    os.system("uname -v")
    os.system("uname -r")
    print("\n[ OS: ]")
    os.system("uname -o")
    print("\n[ Matériel: ]")
    os.system("uname -m")
    print("\n[ Processeur: ]")
    os.system("uname -p")
    print("\n[ Status matériel: ]")
    os.system("uname -i")
    time.sleep(4)
    Index()

def brut_ftp():
	os.system('clear')
	print(head)
	print(F+'Bruteforce SSH,'+E)
	print(B+'Entrez l\'hôte :'+E)
	host = input(W+'Wallskors»Ftp»Hôte»'+E)
	print(B+'Utilisateur:'+E)
	print(F+'Par défaut : admin')
	user = input(W+'Wallskors»Ftp»Utilisateur»'+E)
	print(B+'Tapez (pas.txt) pour utiliser le fichier contenant les mots de passe par défaut'+E)
	password_list = input(W+'Wallskors»Ftp»MotsDePasse»'+E)
	if user == '':
		user = 'admin'
	if password_list == '':
		print(F+'Liste des mots de passe: pas.txt'+E)
		password_list = 'pas.txt'
	os.system('python3 modules/ftp.py '+host+' '+user+' '+password_list)


def brut_mail():
	os.system('clear')
	print(head)
	print(H+'Bruteforce compte mail'+E)
	print(B+'Email :'+E)
	mail = input(W+'Wallskors»Mail»Email»'+E)
	print(B+'Tapez (pas.txt):'+E)
	password = input(W+'Wallskors»Mail»MotsDePasse»'+E)
	if password == '':
		print(F+'Liste des mots de passe: pas.txt'+E)
		password = 'pas.txt'
	os.system('python3 modules/mail.py '+mail+' '+password)

def Index():
	print(head)
	print(G+'''
	Menu Wallskors Security
	'''+H+'''version Delta
	'''+W+'''
	<======= Primaire =======>
  	'''+F+'''
  	1) Deface
  	2) Bruteforce
  	3) Installer des outils
  	'''+W+'''
	<======= Secondaire =======>
	'''+H+'''
  	4) Cryptage de données
  	5) Attaques Dos
  	6) Mon système
    7) Outil de navigation
    8) Sortir
  	'''+W+'''(---------Informations---------)
     Tapez 'help' pour savoir comment utiliser le guide.
	'''+E)
	try:
		v = input(G+'Wallskors-»')
	except:
		print("Exception levée... Mauvaise insertion")
		exit()

	if v == 'help':
		info()
	elif int(v) == 1:
		un()
	elif int(v) == 2:
		deux()
	elif int(v) == 3:
		trois()
	elif int(v) == 4:
		quatre()
	elif int(v) == 5:
		cinq()
	elif int(v) == 6:
		six()
	elif int(v) == 7:
		tol()
	elif int(v) == 8:
		exit()
	else:
		print("Mauvaise insertion, veuillez réessayer.")
		Index()
heads()
Index()