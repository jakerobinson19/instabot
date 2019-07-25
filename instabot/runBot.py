#!/usr/bin/env python

from datetime import date
from time import sleep
from random import randint
from selenium import webdriver

from igBot import instagramBot

import sys
import config
import commenting_util
import nav

def runBot():
  today = date.today()

    if not os.path.isfile('blacklist.xlsx'):
      print('blacklist does not exist, creating one...')
      excel_writer([], 'blacklist')

  blacklist = excel_writer.get_usernames_list_from_sheet('blacklist')

  old_usernames = []

  for day_num in range(config.days_to_refresh_username_lists,-1,-1):
    date = str(today - datetime.timedelta(days=day_num))
    
    day_usernames = excel_writer.get_usernames_list_from_sheet('usernames_' + date)
    if day_usernames:
      old_usernames.extend(day_usernames)


  #in calling the program in cmd line, the username and password are passed as arguments and assigned here
  uname = sys.argv[1]
  pword = sys.argv[2]

  browser = webdriver.Chrome()
  #create the session by initializing the instagramBot object instance using the provided username and password
  session = instagramBot(browser, uname, pword)
  session.delay()
  session.set_blacklist(blacklist)
  session.set_ignore_users(old_usernames)
  session.set_ignore_if_contains(config.bad_words)

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
    elif choice == '8':
      while comments_posted < config.max_comments_per_day or pics_liked < config.max_pics_liked_per_day:
        print(config.max_comments_per_day)
        
        not_visited = True
        #select random hashtag from list using random module
        while not_visited:
          tag = config.hashtag_list[random.randint(0,len(config.hashtag_list)-1)]
        
          if tag not in hashtags_used:
            hashtags_used.append(tag)
            not_visited = False
      
        session.goToHashtag(tag)

        print("Hashtags visited: {}".format(hashtags_used))
      
        session.delay()
        session.selectPicOnExplore('recent')
        profiles_explored = 0

        #this list will store the username which are extracted from the pics on this hashtag to loop through
        new_usernames = []


        #loop through a set number of recent pics and extract the username (here 8 has been arbitrarily picked)
        while profiles_explored < config.profiles_per_hash:
          usname = session.getUsername()
          time.sleep(1)
        
          #check if the username of this pic is not the users profiles (don't want to comment on our own stuff by accident)
          #if it isn't add the username to list of new_usernames to loop through and comment on
          if usname != uname:
            if usname not in config.blacklist:
              if usname not in config.yesterdays_usernames:
                print("This is a new username we have yet to see...adding")
                new_usernames.append(usname)
              else:
                print("commented on this yesterday")
                continue
            else:
              print("Username in the black list")
              continue

        
          print('username: {}'.format(usname))
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
          try:
            followers = session.getFollowerCount()
            following = session.getFollowingCount()
          except NoSuchElementException:
            session.browser.execute_script("location.reload()")
            try:
              followers = session.getFollowerCount()
              following = session.getFollowingCount()
            except NoSuchElementException:
              print("this user has no followers")
              following = 1

          pics = session.getPicturesFromProfile()
          print('number of pics: {}'.format(len(pics)))
          
          f_ratio = round(followers/following,3)
          print('Follower/following ratio: {}'.format(f_ratio))

          if f_ratio > config.follower_to_following_ratio_limit:
            config.blacklist.append(name)

          following = checkIfFollowing(session.browser)
        
          # click on the first pic of the profile
          pics[0].click()

          #set the limit on how many pics to like. Max is 6 and if the profile has less than 6 pics we like them all
          if len(pics) > 6:
            pics_limit = 6
          else:
            pics_limit = len(pics)
        
          pics_liked = 0
          while pics_liked < pics_limit:
            if pics_liked == 0 and following == False:
              if session.already_commented_on():
                print("Already commented on this pic, moving on...")
                pics_liked = pics_limit
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
        pause = random.randint(60*(config.delay_time - config.delay_variance),60*(config.delay_time + config.delay_variance))
        
        session.printStats()
        print(usernames)
        print("Configs blacklist \n {}".format(config.blacklist))

        print("Pausing for {} minutes".format(int(pause/60)))
        
        pause_with_progress(int(pause/60))

    #print out stats of likes, comments, usernamees, etc. (will want to build this out more)
    elif choice == 'S':
      session.printStats()
      print(usernames)

    #exit the browser if the user sends X
    elif choice == 'X':
      session.close()
      print('Exiting...')
      y = False

if __name__ == '__main__':
 runBot()
