# instabot libraries
from instabot import instagramBot
from comment_util import create_comment
from comment_util import send_comment
from time_functions import time_delay
from time_functions import pause_with_progress
from validation import *
import browser
import web_nav
import retrieve
import liking
import comment_util
import database_handler
import excel_writer
import config

# import third party and built in ibraries
import datetime
from datetime import date
import argparse
import os.path
import random
import time
import sys


today = datetime.date.today()
date_range = [(today - datetime.timedelta(days=i)) for i in range(config.DAYS_TO_REFRESH_USERNAMES, -1, -1)]

database_handler.create_database(config.DB_PATH, config.DB_NAME)

blacklist = database_handler.select_blacklist_from_usernames(config.DB_PATH, config.FOLLOWER_TO_FOLLOWING_RATIO_LIMIT) + config.USERNAMES_TO_IGNORE

old_usernames = database_handler.select_usernames_for_date_range(config.DB_PATH, date_range)

# Parse arguments from command line
parser = argparse.ArgumentParser(description='Automated Bot for Instagram using Python and Selenium')
parser.add_argument('-u', '--username', metavar='USERNAME', type=str, default = config.USERNAME, help='Instagram username handle', dest='username')
parser.add_argument('-p', '--password', metavar='PASSWORD', type=str, default = config.PASSWORD, help='Password for Instagram account', dest='password')
parser.add_argument('-l', '--likes', metavar='LIKES', type=int, default=config.MAX_LIKES, help='Number of Likes you want the bot to perform', dest='max_likes')
parser.add_argument('-c', '--comments', metavar='COMMENTS', type=int, default=config.MAX_COMMENTS, help='Number of Comments you want the bot to perform', dest='max_comments')

args = parser.parse_args()

browser = browser.init_driver(config.CHROMEDRIVER_PATH)
#create the session by initializing the instagramBot object instance using the provided username and password
session = instagramBot(browser, args.username, args.password)
time_delay()
session.set_blacklist(blacklist)
session.set_ignore_users(old_usernames)
session.set_ignore_if_contains(config.BAD_WORDS)

#sign in 
session.signIn()

#create an empty list to store all the usernames which the bot engages with while running
#this is primarily for reference to make sure it doesn't like and comment on the same profile in a day
usernames = []
hashtags_used = []

while True:
  print("L - like pictures")
  print("R - Run the Bot")
  print("X - exit app")

  choice = input("What would you like to do: ")

  #L to like a specified number of pictures in the users feed
  if choice == 'L':
    num = int(input("How many pictures would you like to like: "))
    
    web_nav.go_to_feed(browser)
    liking.like_pic_in_feed(browser, num) #NEED TO CHANGE THIS
    session.likes += 1

    print("Done liking pics")

  #run the main function of the bot
  #The bot selects a random hashtag from the hashtag options (created above)
  #then goes to the most recent pictures and extracts the usernames
  #then goes to each username, comments on their latest pic and likes some of their pics
  elif choice == 'R':
    web_nav.go_to_profile(browser)
    start_followers = retrieve.follower_count(browser)
    print('Today you started with {} followers'.format(start_followers))

    while comments_posted < args.max_comments and session.likes < args.max_likes:

      not_visited = True
      while not_visited:
      #select random hashtag from list using random moddule
        tag = config.HASHTAG_LIST[random.randint(0,len(config.HASHTAG_LIST)-1)]
        
        if tag not in hashtags_used:
          hashtags_used.append(tag)
          not_visited = False
      
          web_nav.go_to_hashtag(browser, tag)

      print("Hashtags visited: {}".format(hashtags_used))

      time_delay()
      session.selectPicOnExplore('recent')
      profiles_explored = 0

      #this list will store the username which are extracted from the pics on this hashtag to loop through
      new_usernames = []

      #loop through a set number of recent pics and extract the username (here 8 has been arbitrarily picked)
      while profiles_explored < config.PROFILES_PER_TAG:
        usname = retrieve.username_from_profile(browser)
        
        #check if the username of this pic is not the users profiles (don't want to comment on our own stuff by accident)
        #if it isn't add the username to list of new_usernames to loop through and comment on
        valid, msg = validate_username(usname, blacklist, old_usernames)
        if valid:
          new_usernames.append(usname)
        else:
          print(msg)
          profiles_explored = profiles_explored - 1

        print('username: {}'.format(usname))

        abort = validate_caption(browser)
        if abort:
          print("Found bad word in comments --- avoiding this")
          try:
            new_usernames.remove(usname)
          except:
            pass

        time_delay()
        web_nav.right_arrow(browser)
        profiles_explored = profiles_explored + 1

      #this line removes duplicates from the list so we don't go to the same username twice if they had two recent pics
      new_usernames = list(set(new_usernames))

      #loop through each username that was extracted
      for name in new_usernames:

        #go to the profile, see how many pics it has loaded, see how many followers/following and calculate the ratio
        print('username: {}'.format(name))
        
        followers, following_num, f_ratio = retrieve.follower_to_following_ratio(browser, name)
        print('Follower/following ratio: {} {} - {}'.format(followers, following_num, f_ratio))
        follow_stat = retrieve.follow_status(browser)

        disengage, cant_comment, cant_like, msg = validate_profile(browser, follow_stat)

        if disengage:
          print(msg)
          continue

        database_handler.add_data(config.DB_PATH, "usernames", (name, followers, following_num, f_ratio, follow_stat, today))

        pics = retrieve.pics_from_profile(browser)
        # click on the first pic of the profile
        pics[0].click()

        #set the limit on how many pics to like. Max is 6 and if the profile has less than 6 pics we like them all
        if len(pics) > config.LIKES_PER_PROFILE:
          pics_limit = config.LIKES_PER_PROFILE
        else:
          pics_limit = len(pics)
        
        pics_liked = 0
        while pics_liked < pics_limit:
          time_delay()
          commenting_allowed, liking_allowed = validate_engagement(browser, tag)
          
          if pics_liked == 0 and commenting_allowed and not cant_comment:
            
            if already_commented_on(browser):
              print("Already commented on this pic, moving on...")
              pics_liked = pics_limit
              continue

            else:

              try:
                comment_util.send_comment(browser)
                session.comments += 1
              
              except:
                print("Error occurred: unabled to post comment - Checking if comments are disabled")
                comment_status_disabled, msg  = comment_util.is_commenting_disabled()

          comments = comment_util.get_comments_on_post(browser)

          if liking_allowed and not cant_like:
            liking.like_pic(browser)
            session.likes += 1

          web_nav.right_arrow(browser)
          pics_liked = pics_liked + 1
      
      #add the usernames we commented on to the list of profiles engaged already
      old_usernames.extend(new_usernames)
      session.print_bot_stats()
      print('Usernames engaged today: {}'.format(usernames))

      if comments_posted > args.max_comments or pics_liked > args.max_likes:
        comments_posted = 0
        pics_liked = 0
        break

      else:
        pause = random.randint(60*(config.delay_time - config.delay_variance),60*(config.delay_time + config.delay_variance))

        print('\n####################################')
        print('####################################')
        print("Pausing for {} minutes".format(int(pause/60)))
        pause_with_progress(int(pause/60))

    web_nav.go_to_profile(browser)
    end_followers = retrieve.follower_count(browser)
    following_num = retrieve.following_count(browser)

    print("You have gained {} followers today!!!!".format(end_followers - start_followers))
    database_handler.add_data(config.DB_PATH, "accountProgress", (today, end_followers, following_num, round(end_followers/following_num, 3)))

  #exit the browser if the user sends X
  elif choice == 'X':
    session.close()
    print('Exiting...')
    y = False
