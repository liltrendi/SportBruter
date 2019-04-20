from requests import Session, get
from robobrowser import RoboBrowser as rbb
from lxml.html import fromstring
from itertools import cycle
from time import sleep as wait
from sys import exit as bye
from random import choice
from crayons import red,yellow,green
from progress.bar import IncrementalBar as Bar
import os

session=Session()
workingProxies=set()

url="http://httpbin.org/ip"

user_agent_list = [
	#Chrome
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
	'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
	#Firefox
	'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
	'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
	'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
	'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

def getProxies():
    url = 'https://free-proxy-list.net/'
    userAgent=choice(user_agent_list)
    headers={'User-Agent': userAgent}
    response = get(url,headers=headers)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def saveProxies(proxies):
	with open('proxy.lst','w') as start:
		for p in proxies:
			start.write(p+"\n")

def visit(bot,url,proxy):
	try:
		bot.open(url)
		workingProxies.add(proxy)
		print("\033[0;33m[+]Added proxy \033[0;32m'{}'".format(proxy)+"\033[0;33m to a list of working proxies")
	except:
		print("\033[1;31mConnection error with '\033[0;33m{}'\033[1;31m, skipping it...".format(proxy))

def test(proxyPool,url,proxy):
	for i in range(11):
		session.proxies={"http":proxy,"https":proxy}
		bot=rbb(session=session,parser="html.parser")
		if proxy.issubset(workingProxies):
			pass
		else:
			visit(bot,url,proxy)

def loader():
	proxyBar=Bar("Loading Proxies",max=100,suffix="%(percent)d%%")
	for num in range(101):
		wait(0.005)
		proxyBar.next()
	proxyBar.finish()
	print("\n")

proxies=getProxies()

while True:
	issetProxy=""
	if issetProxy != False or issetProxy != True:
		if proxies:
			if not os.path.isfile("proxy.lst"):
				if len(proxies) > 1:
					proxyPool=cycle(proxies)
					proxy=next(proxyPool)
					test(proxyPool,url,proxy)
					if workingProxies:
						saveProxies(workingProxies)
				else:
					print(red("\n[-] Unable to generate enough proxies for the attack. Continuing without proxies..."))
					issetProxy=False
					break
			else:
				print(green("\n[+] Found saved proxies in file, loading them...\n"))
				loader()
				with open("proxy.lst") as start:
					x=start.read().splitlines()
					if len(x) >=1:
						workingProxies=set(x)
						for proxy in workingProxies:
							proxy="\033[1;32m"+proxy+"\033[1;33m"
							wait(0.3)
							print("\033[0;33m"+"Loaded proxy '{}' from file".format(proxy)+"\033[0;37m")
					else:
						bye(red("File must have at least one proxy"))
			issetProxy=True
			break

		elif os.path.isfile("proxy.lst"):
			print(green("\n[+] Found saved proxies in file, loading them...\n"))
			loader()
			with open("proxy.lst") as start:
				x=start.read().splitlines()
				if len(x) >=1:
					workingProxies=set(x)
					for proxy in workingProxies:
						proxy="\033[1;32m"+proxy+"\033[1;33m"
						wait(0.3)
						print("\033[0;33m"+"Loaded proxy '{}' from file".format(proxy)+"\033[0;37m")
				else:
					bye(red("File must have at least one proxy"))
			issetProxy=True
			break

		else:
			print(red("\n[!] Cannot fetch proxies because your IP address has been blacklisted.\n[!]   The attack will continue without using proxies (No anonymity)"))
			wait(1.5)
			issetProxy=False
			break
