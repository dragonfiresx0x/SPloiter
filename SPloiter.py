import sys
import socket
import colorama
from colorama import Fore
import signal
import bruteforce
from bruteforce import FTP
import reverseip
from reverseip import ReverseIp
import subdomainenum
from subdomainenum import SubdomainEnum

host = None
port = None


print(Fore.RED+
	'''
   _____ _____  _       _ _
  / ____|  __ \| |     (_) |
 | (___ | |__) | | ___  _| |_ ___ _ __
  \___ \|  ___/| |/ _ \| | __/ _ \ '__|
  ____) | |    | | (_) | | ||  __/ |
 |_____/|_|    |_|\___/|_|\__\___|_|


					\n ''')
print(Fore.GREEN+"Coded BY NadarAthis v1.0 \n")


def Checking():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	result = s.connect_ex((host,port))
	if result == 0:
		return True
	else:
		return False

def Main():
	global host
	host = input(Fore.GREEN+"Enter the Target host: ")
	global port
	print(Fore.RED+"Please enter the default port 80 for Cross checking \n")
	port = int(input(Fore.GREEN+"Enter the target port: \n"))
	print('')
	if Checking()==True:
		print(Fore.GREEN+"HURRAH HOST IS ALIVE !!!\n")
	else:
		print(Fore.RED+"SORRY HOST IS NOT REACHABLE\n")
		exit()

Bruteforcers = {
	1: FTP
}

def BruteForcer(host,port):
	Option = 1
	while True:
		print('')
		print("1]FTP")
		print("2]MAIN MENU")
		Option = int(input(">>"))
		print('')
		if(Option < 2) and (Option >=0):
			Bruteforcers[Option](host,port)
		elif Option==2:
			MainMenu()
		else:
			print("HEY YOU CLICK ON A PROPER OPTION")

Vulnerabilities = {
	1: BruteForcer,
	2: ReverseIp,
	3: SubdomainEnum

}

def MainMenu():
	Option = 1
	while True:
		print('')
		print("1)BruteForcer")
		print("2)ReveseIp")
		print("3)Subdomain Enumeration")
		print("4)Exit")
		print('')
		Option = int(input(">>"))
		if (Option < 4) and (Option >=0):
			Vulnerabilities[Option](host,port)
		elif Option == 4:
			exit()
		else:
			print("HEY YOU CLICK ON A PROPER OPTION")


if __name__ == "__main__":
	Main()
	MainMenu()
