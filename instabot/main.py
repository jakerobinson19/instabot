#!/usr/bin/env python

from time import sleep
from random import randint
from igBot import instabot

import sys
from . import config
from . import commenting_util
from . import nav

def main()
 
  #in calling the program in cmd line, the username and password are passed as arguments and assigned here
  uname = sys.argv[1]
  pword = sys.argv[2]

  #create the session by initializing the instagramBot object instance using the provided username and password
  session = instagramBot(uname, pword)
  session.delay()

  #sign in 
  session.signIn()

  #create an empty list to store all the usernames which the bot engages with while running
  #this is primarily for reference to make sure it doesn't like and comment on the same profile in a day
  usernames = []
  hashtags_used = []
  comments_posted = 0

  y = True

  while y:
    print("L - like pictures")
    print("8 - Run the Bot")
    print("U - Unfollow a User")
    print("S - get statistics")
    print("X - exit app")

    choice = input("What would you like to do: ")

    #L to like a specified number of pictures in the users feed
    if choice == 'L':
      num = int(input("How many pictures would you like to like: "))
      #hearts = session.getLikeButtons()
      session.likePicInFeed(num) #NEED TO CHANGE THIS
      print("Done liking pics")

    elif choice == 'U':
      inp = input("What user would you like to unfollow? ")
      session.unfollow_user(inp)

    #run the main function of the bot
    #The bot selects a random hashtag from the hashtag options (created above)
    #then goes to the most recent pictures and extracts the usernames
    #then goes to each username, comments on their latest pic and likes some of their pics
    elif choice == '2':
      while comments_posted < session.max_comments_per_day or pics_liked < session.max_pics_liked_per_day:
        print(session.max_comments_per_day)
        
        not_visited = True
        #select random hashtag from list using random module
        while not_visited:
          tag = session.hashtagList[random.randint(0,len(session.hashtagList)-1)]
        
          if tag not in hashtags_used:
            hashtags_used.append(tag)
            not_visited = False
      
        session.goToHashtag(tag)

        print("Hashtags visited: {}".format(hashtags_used))
      
        session.delay()
        session.selectRecentPicOnExplore()
        profiles_explored = 0

        #this list will store the username which are extracted from the pics on this hashtag to loop through
        new_usernames = []


        #loop through a set number of recent pics and extract the username (here 8 has been arbitrarily picked)
        while profiles_explored < 8:
          usname = session.getUsername()
          time.sleep(1)
        
          #check if the username of this pic is not the users profiles (don't want to comment on our own stuff by accident)
          #if it isn't add the username to list of new_usernames to loop through and comment on
          if usname != uname or usname not in blacklist:
            new_usernames.append(usname.text)
        
          print('username: {}'.format(usname.text))
          time.sleep(1)
          session.rightArrow()
          profiles_explored = profiles_explored +1

        #this line removes duplicates from the list so we don't go to the same username twice if they had two recent pics
        new_usernames = list(set(new_usernames))
        if session.email in new_usernames:
          new_usernames.remove(session.email)

        #loop through each username that was extracted
        for name in new_usernames:
        
          #check that we haven't already commented on this profile today by reference the stored username bank
          if name in usernames:
            print("Already commented and liked this profile today")
            #if we have already engaged with this profile, skip it
            continue

          #otherwise go to the profile, see how many pics it has loaded, see how many followers/following and calculate the ratio
          session.goToProfile(name)
          session.delay()
          pics = session.getPicturesFromProfile()
          print('number of pics: {}'.format(len(pics)))
          followers = session.getFollowerCount()
          following = session.getFollowingCount()
          print('Follower/following ratio: {}'.format(round(followers/following,3)))
          session.checkIfFollowing()
        
          # click on the first pic of the profile
          pics[0].click()

          #set the limit on how many pics to like. Max is 6 and if the profile has less than 6 pics we like them all
          if len(pics) > 6:
            pics_limit = 6
          else:
            pics_limit = len(pics)
        
          pics_liked = 0
          while pics_liked < pics_limit:
            if pics_liked == 0:
              if session.already_commented_on():
                print("Already commented on this pic, moving on...")
                pics_liked = pics_liked + 1
                continue
              else:  
                try:
                  newComment = session.createComment()
                  session.sendComment(newComment)
                  comments_posted = comments_posted + 1
                except:
                  print("Error occurred: unabled to post comment - Checking if comments are disabled")
                  comment_status_disabled, msg  = session.is_commenting_disabled()
                  print(msg)
                  if comment_status_disabled:
                    continue


            session.likePic()
            session.rightArrow()
            pics_liked = pics_liked + 1
      
        #add the usernames we commented on to the list of profiles engaged already
        usernames.extend(new_usernames)
        pause = random.randint(120,150)
        print("Pausing for {} seconds".format(pause))
        time.sleep(pause)
        session.printStats()

    #print out stats of likes, comments, usernamees, etc. (will want to build this out more)
    elif choice == 'S':
      session.printStats()
      print(usernames)

    #exit the browser if the user sends X
    elif choice == 'X':
      session.close()
      print('Exiting...')
      y = False
