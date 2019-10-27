#!/usr/bin/env python
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from config import WORD_OPTIONS
from config import EMOJI_OPTIONS

from finder_function import read_xpath
from finder_function import read_selector

import time
import random
  
def create_comment():
  comment = None
  
  for index in range(len(WORD_OPTIONS)):
    word = WORD_OPTIONS[index][random.randint(0,len(WORD_OPTIONS[index])-1)]
    
    if comment is None:
      comment = word
    
    else:
      comment = comment + word

  return(comment)

def get_usernames_from_comments(browser):
    comm_unames = WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, read_xpath('comments','comments_on_pic')))
  )   
    return(comm_unames)
  
def get_comments_on_post(browser):
    try:
      comms = WebDriverWait(browser, 10).until(
      EC.presence_of_all_elements_located((By.XPATH, read_xpath('comments','comment_section')))
      )   
    except TimeoutException:
      print("No comments or caption on this post")
      comms = None

    return(comms)

def get_number_of_comments(browser):
  num_of_comments = len(get_comments_on_post(browser)) - 1
  return(num_of_comments)

def get_username_on_comment(comments):
  comment_usernames = []
  
  for comm in comments:
    uname = comm.read_xpath(['comments']['username_of_comment'])
    comment_usernames.append(uname)
    
  return(comment_usernames)
  
def send_comment(browser, comm=None):
  if not comm:
    comm = create_comment()

  comment_box = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
  time.sleep(1)
  comment_box.click()
  comment_box = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
  browser.execute_script(
                "arguments[0].value = arguments[1];",
                comment_box, comm)

  time.sleep(1)
  #self.commentInputNew = self.browser.find_element_by_xpath("//div[@class='Mfkwx wUsz1']")
  comment_box.send_keys('\b')
  comment_box = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, read_selector('elements','comment_box'))))
  time.sleep(2)
  comment_box.send_keys(Keys.ENTER)

def is_commenting_disabled(browser):
    try:
      is_disabled = browser.execute_script("return window._sharedData.entry_data.PostPage[0].graphql.shortcode_media.comments_disabled")
    except:
      try:
        browser.execute_script("location.reload()")
        is_disabled = browser.execute_script("return window._sharedData.entry_data.PostPage[0].graphql.shortcode_media.comments_disabled")  
      except Exception as e:
            msg = ("Failed to check comments' status for verification!\n\t{}"
                   .format(str(e).encode("utf-8")))
            return False, msg
    
    if is_disabled is True:
      return True, 'Comment are disabled for this post'

    return False, "Comments Enabled"
