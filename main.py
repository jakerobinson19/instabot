from time import sleep
from random import randint
from igBot import instabot
from . import config
from . import commenting_util
from . import nav

def main()
  uname = str(input("Please enter your username: "))
  pword = str(input("Please enter your password: "))

  session = instabot(uname, pword)
  session.delay()

  session.signIn()

  action = True

  while actiom:
    print("P - go to profile and select first image")
    print("L - like pictures")
    print("H - go to hashtag")
    print("C - generate comment")
    print("8")
    print("X - exit app")

    choice = input("What would you like to do: ")
    
    if choice == 'P':
      session.goToProfile()
      session.selectPic()

    elif choice == 'L':
      num = int(input("How many pictures would you like to like: "))
      #hearts = session.getLikeButtons()
      session.likePicInFeed(num) #NEED TO CHANGE THIS
      print("Done liking pics")

    elif choice == 'H':
      tag = str(input("What tag would you like to explore: "))
      session.goToHashtag(tag)
      ans = int(input("How many pics would you like to like: "))
      session.selectRecentPicOnExplore()
      for iter, i in enumerate(range(ans)):
        u = session.getUsername()
        print("username is {}".format(u))
        session.likePic()
        time.sleep(1)
        session.rightArrow()
        
      c = session.createComment()
      print(c)
      session.sendComment(emoji.emojize(c,use_aliases=True))

    elif choice == 'C':
      com = session.createComment()
      print(emoji.emojize(com,use_aliases=True))

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
