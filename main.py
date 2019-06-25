from time import sleep
from igBot import instabot

uname = input("Please enter username: ")
pword = input("Please enter password: ")

bot = instabot(Chrome,uname,pword)

instabot.signIn()

time.sleep(3)
