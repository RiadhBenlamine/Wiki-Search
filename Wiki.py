#!/usr/bin/python
# -*- coding:utf-8 -*-
#  Simple scrapper for wikipedia ,
# written in python 3.7 with GNU license .
# Github : https://www.github.com/RiadhBenlamine
# Blog : edatasec.wordpress.com


import requests
import re
import colorama
import sys
from bs4 import BeautifulSoup
from os import system
from time import sleep

__author__ = "Riadh Benlamine"
__email__ = "riadhriah03@gmail.com"
__version__ = 1.0

# Setting up colorama
reset = colorama.Fore.RESET
yellow = colorama.Fore.YELLOW
light_yellow = colorama.Fore.LIGHTYELLOW_EX
light_green = colorama.Fore.LIGHTGREEN_EX
red = colorama.Fore.RED
green = colorama.Fore.GREEN
blue = colorama.Fore.BLUE

class English:

    def __init__(self):

        self.site = 'https://en.m.wikipedia.org'
        self.keyword = str()
        self.data = {
                "search":self.keyword
                }

    def Entry(self):

        print(light_yellow,"Search For?",reset)
        self.keyword = str(input("Keyword>>> "))

    def Request(self):

        try:
            request = requests.post(self.site,data=self.data)
            if request.status_code == 200 or request.status_code == 301:
                return request.text
            else:
                print(red,"Error...(%s)"%(request.status),reset)
                sys.exit()
        except Exception:
            print(red,"No Network",reset)
            sys.exit()


    def Scraper(self):

        def Clean_html(raw_html):
            ''' From stackoverflow '''
            cleanr = re.compile('<.*?>')
            cleantext = re.sub(cleanr, '', raw_html)
            return cleantext

        html = self.Request()
        bs = BeautifulSoup(html,'html') # beautifulsoup Object
        p = bs.findAll('p')
        txt = []
        for index in range(0,3):
            x = Clean_html(index)
            txt.append(x)

        return txt

    def Output(self):

        print(green,self.keyword.title(),reset)
        for text in txt:
            print("|\t\t",text)
            if txt.index(text) == 3:
                print("|______",text)

class German:

    def __init__(self):

        self.site = 'https://de.m.wikipedia.org'
        self.keyword = str()
        self.data = {
                "search":self.keyword
                }
        
    def Entry(self):

        print("Suchen Sie?")
        self.keyword = str(input("Die Stichworte > "))

    def Request(self):

        try:
            request = requests.post(self.site,data=self.data)
            if request.status_code == 200 or request.status_code == 301:
                return request.text
            else:
                print(red,"Error...(%s)"%(request.status),reset)
                sys.exit()
        except Exception:
            print(red,"Kein Netzwerk",reset)
            sys.exit()

    def Scraper(self):

        def Clean_html(raw_html):
            ''' From stackoverflow '''
            cleanr = re.compile('<.*?>')
            cleantext = re.sub(cleanr, '', raw_html)
            return cleantext

        html = self.Request()
        bs = BeautifulSoup(html,'html') # beautifulsoup Object
        p = bs.findAll('p')
        txt = []
        for index in range(0,3):
            x = Clean_html(index)
            txt.append(x)

        return txt

    def Output(self):

        print(green,self.keyword.title(),reset)
        for text in txt:
            print("|\t\t",text)
            if txt.index(text) == 3:
                print("|______",text)


             
def Clear():
        ''' Clear function and platform detection '''
        if sys.platform == 'linux':
            system("clear")
        elif sys.platform == 'win32':
            system("cls")
        else :
            print(red,"[-] I didn't use MacOS Before lol replace the command here.")
            #system("<command>")

Clear()
print(light_yellow,"\tWiki ",light_green,"Search",reset)
print("\t________________",blue,str(__version__),reset,"\n")
print("1 -> English")
print("2 -> Deutsch")
language = int(input("Select language > "))

if language == 1:
    Clear()
    eng = English()
    eng.Entry()
    eng.Scraper()
    eng.Output()

if language == 2:
    Clear()
    de = German()
    de.Entry()
    de.Scraper()
    de.Output()
else:
    print(red,"only one from those",reset)
