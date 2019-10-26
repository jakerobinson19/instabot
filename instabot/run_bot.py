# instabot libraries
from InstagramBot import instagramBot
from comment_functions import create_comment
from comment_functions import send_comment
from comment_functions import is_commenting_disabled
from time_functions import time_delay
from time_functions import pause_with_progress
from validation import *
import comment_functions
import browser
import web_nav
import retrieve
import liking
import database_handler
import config

# Selenium exception for if you get blocked
from selenium.common.exceptions import ElementClickInterceptedException

# import third party and built in ibraries
import datetime
from datetime import date
import os.path
import random
import time
import sys

def run_bot(username, password, max_comments, max_likes):

  today = datetime.date.today()
  date_range = [(today - datetime.timedelta(days=i)) for i in range(config.DAYS_TO_REFRESH_USERNAMES, -1, -1)]

  database_handler.create_database(config.DB_PATH, config.DB_NAME)

  blacklist = database_handler.select_blacklist_from_usernames(config.DB_PATH, config.FOLLOWER_TO_FOLLOWING_RATIO_LIMIT) + config.USERNAMES_TO_IGNORE

  old_usernames = database_handler.select_usernames_for_date_range(config.DB_PATH, date_range)

  web_browser = browser.init_driver(config.CHROMEDRIVER_PATH)
  #create the session by initializing the instagramBot object instance using the provided username and password
  session = instagramBot(web_browser, username, password)
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
  
  run = True

  while run == True:
    print("L - like pictures")
    print("R - Run the Bot")
    print("X - exit app")

    choice = input("What would you like to do: ")

    #L to like a specified number of pictures in the users feed
    if choice == 'L':
      num = int(input("How many pictures would you like to like: "))
    
      web_nav.go_to_feed(web_browser)
      liking.like_pic_in_feed(web_browser, num) #NEED TO CHANGE THIS
      session.likes += 1

      print("Done liking pics")

    # Run the main function of the bot
    # The bot selects a random hashtag from the hashtag options (created above)
    # then goes to the most recent pictures and extracts the usernames
    # then goes to each username, comments on their latest pic and likes some of their pics
    elif choice == 'R':
      try: 
        web_nav.go_to_profile(web_browser, username)
        start_followers = retrieve.follower_count(web_browser)
        print('Today you started with {} followers'.format(start_followers))

        while session.comments < max_comments and session.likes < max_likes:

          not_visited = True
          while not_visited:
          # select random hashtag from list using random moddule
            tag = config.HASHTAG_LIST[random.randint(0,len(config.HASHTAG_LIST)-1)]
        
            if tag not in hashtags_used:
              hashtags_used.append(tag)
              not_visited = False
      
              web_nav.go_to_hashtag(web_browser, tag)

          print("Hashtags visited: {}".format(hashtags_used))

          time_delay()
          web_nav.select_pic_on_explore_page(web_browser, 'recent')
          profiles_explored = 0

          # this list will store the username which are extracted from the pics on this hashtag to loop through
          new_usernames = []

          # loop through a set number of recent pics and extract the username (here 8 has been arbitrarily picked)
          while profiles_explored < config.PROFILES_PER_TAG:
            usname = retrieve.username_from_profile(web_browser)
        
            # check if the username of this pic is not the users profiles (don't want to comment on our own stuff by accident)
            # if it isn't add the username to list of new_usernames to loop through and comment on
            valid, msg = validate_username(usname, blacklist, old_usernames)
            if valid:
              new_usernames.append(usname)
            else:
              print(msg)
              profiles_explored = profiles_explored - 1

            print('username: {}'.format(usname))

            abort = validate_caption(web_browser)
            if abort:
              print("Found bad word in comments --- avoiding this")
              try:
                new_usernames.remove(usname)
              except:
                pass

            time_delay()
            web_nav.right_arrow(web_browser)
            profiles_explored = profiles_explored + 1

          # this line removes duplicates from the list so we don't go to the same username twice if they had two recent pics
          new_usernames = list(set(new_usernames))

          # loop through each username that was extracted
          for name in new_usernames:

            # go to the profile, see how many pics it has loaded, see how many followers/following and calculate the ratio
            print('username: {}'.format(name))
        
            followers, following_num, f_ratio = retrieve.follower_to_following_ratio(web_browser, name)
            print('Follower/following ratio: {} {} - {}'.format(followers, following_num, f_ratio))
            follow_stat = retrieve.follow_status(web_browser)

            disengage, cant_comment, cant_like, msg = validate_profile(web_browser, follow_stat)

            database_handler.add_data(config.DB_PATH, "usernames", (name, followers, following_num, f_ratio, follow_stat, today))
          
            if disengage:
              print(msg)
              continue

            session.increment_profiles_engaged_tally()

            pics = retrieve.pics_from_profile(web_browser)
            # click on the first pic of the profile
            pics[0].click()

            # set the limit on how many pics to like. Max is 6 and if the profile has less than 6 pics we like them all
            if len(pics) > config.LIKES_PER_PROFILE:
              pics_limit = config.LIKES_PER_PROFILE
            else:
              pics_limit = len(pics)
        
            pics_liked = 0

            while pics_liked < pics_limit:
        
              commenting_allowed, liking_allowed = validate_engagement(web_browser, tag)
          
              if pics_liked == 0 and commenting_allowed and not cant_comment:
            
                if already_commented_on(web_browser):
                  print("Already commented on this pic, moving on...")
                  pics_liked = pics_limit
                  continue

                else:

                  try:
                    send_comment(web_browser)
                    session.increment_comment_tally()
              
                  except:
                    comment_status_disabled, msg  = comment_util.is_commenting_disabled(browser)
                  
                    if comment_status_disabled:
                      print(msg)

              if liking_allowed and not cant_like:
                liking.like_pic(web_browser)
                session.increment_like_tally()

              web_nav.right_arrow(web_browser)
              pics_liked = pics_liked + 1
      
          # add the usernames we commented on to the list of profiles engaged already
          old_usernames.extend(new_usernames)
          usernames.extend(new_usernames)
          session.print_bot_stats()

          if not config.SUPPRESS_FULL_LOG:
            print('Usernames engaged today: {}'.format(usernames))
            session.print_username_lists()

          if session.comments > max_comments or session.likes > max_likes:
            database_handler.add_data(config.DB_PATH, "activityRecord", (today, session.get_time_delta(), session.profiles_engaged, session.comments, session.likes))
            session.reset_engagement_stats()
            break

          else:
            pause = random.randint(60*(config.delay_time - config.delay_variance),60*(config.delay_time + config.delay_variance))

            print("Pausing for {} minutes".format(int(pause/60)))
            pause_with_progress(int(pause/60))

      except ElementClickInterceptedException:
        print ("\n\n It appears that the bot has been blocked :( ")
        print (" Please check that you're configuration parameters are reasonable")
        print (" We will pause until further notice")

      except KeyboardInterrupt:

        print("\n\n ####################")
        print(" Exiting. Goodbye :)")
        run = False
        break

      except Exception as e:

        print(" Unexpected exception error occurred: {}".format(e))

      finally:

        web_nav.go_to_profile(web_browser, username)
        end_followers = retrieve.follower_count(web_browser)
        following_num = retrieve.following_count(web_browser)

        print("You have gained {} followers today!!!!".format(end_followers - start_followers))
        database_handler.add_data(config.DB_PATH, "accountProgress", (today, end_followers, following_num, round(end_followers/following_num, 3)))
    
    # exit the browser if the user sends X
    elif choice == 'X':
      browser.close(web_browser)
      print('Exiting...')
      break
