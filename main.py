from time import sleep
from random import randint
from igBot import instabot

uname = input("Please enter username: ")
pword = input("Please enter password: ")

bot = instabot(Chrome,uname,pword)

bot.signIn()

sleep(randInt(3,6))
