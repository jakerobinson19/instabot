from selenium.webdriver.common.keys import Keys

# import instabot modules
from finder_function import read_xpath
from finder_function import read_selector

import config
 
# import third party and built in ibraries
import datetime
from datetime import date
import os.path
import random
import time
import sys

class instagramBot():
  
  def __init__(self, browser, email, password):
    self.browser = browser
    
    self.email = email
    self.password = password
    self.likes = 0
    self.comments = 0
    self.profiles_engaged = 0
    self.errors_handled = 0
    self.total_comments = 0
    self.total_likes = 0

    self.begin_following = 0
    self.end_following = 0

    self.blacklist = None
    self.ignore_users = None

    self.follow_back_engage = config.INTERACT_IF_FOLLOW_BACK
    
    self.ignore_if_contains = None

    self.date_range = self.generate_date_range()

    self.start_time = datetime.datetime.now()
    
  def signIn(self):
    self.browser.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)
    self.emailInput = self.browser.find_elements_by_css_selector('form input')[0]
    self.passwordInput = self.browser.find_elements_by_css_selector('form input')[1]
    time.sleep(2)
    
    #send email and password to fill input sections
    self.emailInput.send_keys(self.email)
    time.sleep(2)
    self.passwordInput.send_keys(self.password)
    
    #press Enter
    self.passwordInput.send_keys(Keys.ENTER)
    print('Working on notification pop up...')
    time.sleep(3)
    
    try:
      #click the not now option for the notifications pop-up that appears immediately after logging in
      self.notnow = self.browser.find_element_by_xpath(read_xpath('notification_wall','not_now'))
      self.notnow.click()
    except:
      print("Could not locate notifications window. Perhaps a Suspicious Login was Detected")
    
    time.sleep(2)
    #self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    self.browser.maximize_window()

  def set_blacklist(self, users):
    self.blacklist = users
    return(self)

  def set_ignore_users(self, users=None):
    self.ignore_users = users

    return(self)

  def set_ignore_if_contains(self, words=None):
    """Ignores the don't likes if the description contains
    one of the given words"""
    self.ignore_if_contains = words or []

    return(self)

  def increment_comment_tally(self, num=1):
    self.comments += num
    self.total_comments += num

  def increment_like_tally(self, num=1):
    self.likes += num
    self.total_likes += num

  def increment_profiles_engaged_tally(self, num=1):
    self.profiles_engaged += num
  
  def reset_engagement_stats(self):
    self.comments = 0
    self.likes = 0
    self.profiles_engaged = 0

  def generate_date_range(self):
    date_range = []
    today = date.today()

    spread = config.DAYS_TO_REFRESH_USERNAMES

    for day in range(spread):
      d = today - datetime.timedelta(days=day+1)
      date_range.append(d)

    return(date_range)

  def get_time_delta(self):
    time_now = datetime.datetime.now()
    t_delta = time_now - self.start_time
    t_delta_in_mins = round(t_delta/datetime.timedelta(minutes=1),2)
    return(t_delta_in_mins)

  def print_bot_stats(self):
    time = self.get_time_delta()

    print('\n--------Stats----------')
    print('Liked {} pictures over {} minutes for a rate of {} likes/hour'.format(self.total_likes, round(time/60,2), round((self.total_likes/time)*3600,2)))
    print('{} comments created'.format(self.total_comments))
    print('{} profiles engaged'.format(self.profiles_engaged))
    print('\n####################################')
    print('####################################')

  def print_username_lists(self):
    print('\nBlacklist: {}'.format(self.blacklist))
    print('\nUsers To Ignore: {}'.format(self.ignore_users))
    print('\nIgnore Post If It Contains: {}'.format(self.ignore_if_contains))

  def check_list_for_name(self, container, name):

    for item in container:
      if name in item:
        return(True)

    return(False)
