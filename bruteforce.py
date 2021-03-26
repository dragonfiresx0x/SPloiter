import paramiko
import requests
import socket
import ftplib
from ftplib import FTP


def FTP(host,port):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	port = 21
	result = s.connect_ex((host,port))
	s.settimeout(7)
	if result == 0:
		print("HURRAH PORT IS OPEN !!!")
		s.close()
		wordlist = input("Enter the wordlist location(Press Enter for default wordlist): ")
		if wordlist == '':
			x = open("src/wordlists.txt","r")
			x1= x.readlines()
		for x in x1:
			y = x.split(':')
			username = y[0].strip(":")
			password = y[1].strip("\n")
			ftp = FTP(host)
			print("Checking Username and Password")
			try:
				ftp.login(user='username', password ='password')
				flag = 0
				pass

			except exception as e:
				flag = 1
				print("Invalid Credentials")
			except socekt.error as e :
				flag = 2
				print(e)
			except KeyboardInterrupt():
				print("User Keyboard interuption") 
				exit()
			if flag == 0:
				print("Credentials found")
				print("Username : %s" % username)
				print("Password : %s" % password)
			elif flag == 1:
				print("Invalid Credentials")
				exit()

	elif result !=0:
		print("Port is Closed")
		exit()

