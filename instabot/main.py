#!/usr/bin/env python

from time import sleep
from random import randint
from igBot import instabot

import sys
from . import config
from . import commenting_util
from . import nav

def main()
  
  try:
    uname = sys.argv[1]
    pword = sys.argv[2]
  except:
    uname = str(input("Please enter your username: "))
    pword = str(input("Please enter your password: "))

  session = instabot(uname, pword)
  session.delay()

  session.signIn()

  action = True

  while actiom:
    print("L - like pictures")
    print("8 - Run Bot")
    print("X - exit app")

    choice = input("What would you like to do: ")
 
    if choice == 'L':
      num = int(input("How many pictures would you like to like: "))
      #hearts = session.getLikeButtons()
      session.likePicInFeed(num) #NEED TO CHANGE THIS
      print("Done liking pics")

    elif choice == '8':
      tag = session.hashtagList[random.randint(0,len(session.hashtagList))]
      session.goToHashtag(tag)
      session.delay()
      session.selectRecentPicOnExplore()
      it = 0
      usernames = []

      while it < 10:
        usname = session.getUsername()
        if usname != uname:
          usernames.append(usname.text)
        print('username: {}'.format(usname.text))
        session.delay()
        session.rightArrow()
        it = it +1

      usernames = list(set(usernames))

      for name in usernames:
        session.goToProfile(name)
        session.delay()
        pics = session.getPicturesFromProfile()
        print('number of pics: {}'.format(len(pics)))
        pics[0].click()

        if len(pics) > 10:
          y = 10
        else:
          y = len(pics)
        x = 0
        while x < y:
          session.likePic()
          session.rightArrow()
          x = x + 1

    elif choice == 'X':
      session.close()
      print('Exiting...')
      y = False
