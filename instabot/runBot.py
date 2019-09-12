# import third party and built in ibraries
import datetime
import argparse
import os.path
import random
import time
import sys

# instabot libraries
from instabot import instagramBot
from comment_util import create_comment
from comment_util import send_comment
import browser
import web_nav
import retrieve
import comment_util
import database_handler
import excel_writer
import config

# import third party and built in ibraries
import datetime
from datetime import date
import os.path
import random
import time
import sys

import emoji

today = datetime.date.today()
date_range = [(today - datetime.timedelta(days=i)) for i in range(config.days_to_refresh_username_lists, -1, -1)]

database_handler.create_database(config.db_path, config.db_name)

blacklist = database_handler.get_usernames_from_table_where('f2f_ratio', 'GREATER THAN', 
                                                            config.follower_to_following_ratio_limit)
old_usernames = database_handler.get_username_from_table_where('caldate', )
  
parser = argparse.ArgumentParser(description='Automated Bot for Instagram using Python and Selenium')
parser.add_argument('-u', '--username', metavar='USERNAME', type=str, default = config.USERNAME, help='Instagram username handle', dest='username')
parser.add_argument('-p', '--password', metavar='PASSWORD', type=str, default = config.PASSWORD, help='Password for Instagram account', dest='password')

args = parser.parse_args()

browser = browser.init_driver('/usr/local/bin/chromedriver')
#create the session by initializing the instagramBot object instance using the provided username and password
session = instagramBot(browser, args.username, args.password)
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

print(blacklist)

y = True

while y:
  print("L - like pictures")
  print("R - Run the Bot")
  print("X - exit app")

  choice = input("What would you like to do: ")

  #L to like a specified number of pictures in the users feed
  if choice == 'L':
    num = int(input("How many pictures would you like to like: "))
    
    web_nav.go_to_feed()
    liking.likePicInFeed(num) #NEED TO CHANGE THIS
    print("Done liking pics")

  #run the main function of the bot
  #The bot selects a random hashtag from the hashtag options (created above)
  #then goes to the most recent pictures and extracts the usernames
  #then goes to each username, comments on their latest pic and likes some of their pics
  elif choice == '8':
    web_nav.go_to_profile(browser)
    start_followers = retrieve.follower_count(browser)
    print('Today you started with {} followers'.format(start_followers))

    while comments_posted < config.max_comments_per_day and session.likes < config.max_likes_per_day:
      print(config.max_comments_per_day)
        
      #select random hashtag from list using random moddule
      tag = config.hashtag_list[random.randint(0,len(config.hashtag_list)-1)]
        
        if tag not in hashtags_used:
          hashtags_used.append(tag)
          not_visited = False
      
      web_nav.go_to_hashtag(browser, tag)

      print("Hashtags visited: {}".format(hashtags_used))

      session.delay()
      session.selectPicOnExplore('recent')
      profiles_explored = 0

      #this list will store the username which are extracted from the pics on this hashtag to loop through
      new_usernames = []

      #loop through a set number of recent pics and extract the username (here 8 has been arbitrarily picked)
      while profiles_explored < config.profiles_per_hash:
        usname = retrieve.username_from_profile(browser)
        
        #check if the username of this pic is not the users profiles (don't want to comment on our own stuff by accident)
        #if it isn't add the username to list of new_usernames to loop through and comment on
        valid, msg = validation.validate_username(usname, usernames)
        if valid:
          new_usernames.append(usname)
        else:
          print(msg)
          profiles_explored = profiles_explored - 1

        
        print('username: {}'.format(usname))

        caption = retrieve.pic_caption(browser)
        abort = validation.validate_caption(caption)
        if abort:
          print("Found bad word in comments --- avoiding this")
          try:
            new_usernames.remove(usname)
          except:
            pass
        #except:
          #print("error occurred with caption")

        time.sleep(1)
        web_nav.right_arrow(browser)
        profiles_explored = profiles_explored + 1

      #this line removes duplicates from the list so we don't go to the same username twice if they had two recent pics
      new_usernames = list(set(new_usernames))
      if session.email in new_usernames:
        new_usernames.remove(session.email)

      #loop through each username that was extracted
      for name in new_usernames:

        #go to the profile, see how many pics it has loaded, see how many followers/following and calculate the ratio
        print('username: {}'.format(name))
        
        followers, following_num, f_ratio = retrieve.follower_to_following_ratio(browser, name)
        print('Follower/following ratio: {} {} - {}'.format(followers, following_num, f_ratio))

        follow_stat = retrieve.follow_status()
        follow_back = False

        validation = validation.validate_engagement(browser)
        
        status = retrieve.follow_status()
        if status == 'Follow Back':
          follow_back = True
          print('Status is follow back. Disengage!')
          #continue
        elif status == 'Following':
          following = True
        else:
          following = False

        old_usernames.append[name]
        database_handler.add_data(config.db_path, name, (name, followers, following_num, f_ratio, follow_stat, today))

        pics = session.getPicturesFromProfile()
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
            elif session.check_for_hashtag_in_comments(tag) == False:
              pics_liked += 1
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

          comments = comment_util.get_comments_on_post(browser)
          mtype = retrieve.media_type(browser)
          print(mtype)
          session.likePic()
          web_nav.right_arrow(browser)
          pics_liked = pics_liked + 1
      
      #add the usernames we commented on to the list of profiles engaged already
      usernames.extend(new_usernames)
      pause = random.randint(60*(config.delay_time - config.delay_variance),60*(config.delay_time + config.delay_variance))
        
      session.print_bot_stats()
      print('Usernames engaged today: {}'.format(usernames))
      #print("Excel blacklist \n {}".format(blacklist))

      excel_writer.create_workbook(blacklist,'blacklist')
        
      today = date.today()
      todays_unames_already = excel_writer.get_usernames_list_with_details('usernames_' + str(today))

      if comments_posted > config.max_comments_per_day or pics_liked > config.max_likes_per_day:
        print("Posted {} comments and {} likes today".format(comments_posted, pics_liked))
        comments_posted = 0
        pics_liked = 0
        break

      print('\n####################################')
      print('####################################')
      print("Pausing for {} minutes".format(int(pause/60)))
      pause_with_progress(int(pause/60))

    session.goToProfile()
    end_followers = session.getFollowerCount()

    print("You have gained {} followers today!!!!".format(end_followers - start_followers))

  #exit the browser if the user sends X
  elif choice == 'X':
    session.close()
    print('Exiting...')
    y = False
