"""selenium modules"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 

"""Exceptions"""
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException

from finder_function import read_xpath
from finder_function import read_selector

import web_nav


def username_from_profile(browser):
    try:
      wait = WebDriverWait(browser, 10)
      uname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, read_selector('elements','profile_username'))))
      uname = uname.text
      #uname = self.browser.find_element_by_class_name('BrX75').text
    except TimeoutException:
      print("Picture doesnt exist")
      uname = None

    return(uname)
    
def comments_on_post(browser):
    try:
      comms = WebDriverWait(self.browser, 10).until(
      EC.presence_of_all_elements_located((By.XPATH, read_xpath('comments','comment_section')))
      )
        
    except TimeoutException:
      print("No comments or caption on this post")
      comms = None

    return(comms)
      
def like_button(browser):
    wait = WebDriverWait(browser, 10)
    
    like_button = wait.until(EC.visibility_of_element_located((By.XPATH, read_xpath('like_button','like_button'))))
    return(like_button)

def heart_outline(element):
    return(element.find_element_by_xpath(read_xpath('like_button','heart_outline')))
    
def feed_like_buttons(browser):
    hearts = browser.find_elements_by_xpath("//span[@class='fr66n']")
    return(hearts)
    
def follower_count(browser):
    try:
        follower_element = browser.find_element_by_partial_link_text("followers").find_element_by_xpath('span')
        follower_count = int(follower_element.get_attribute('title').replace(',',''))
    
    except NoSuchElementException as e:
        print("error occurred: {}".format(e))
        follower_count = 1

    return(follower_count)

def following_count(browser):
    following_element = browser.find_element_by_partial_link_text("following").find_element_by_xpath('span')
    following_count = int(following_element.text.replace(',',''))

    return(following_count)
    
def pics_from_profile(browser):
    return(browser.find_elements_by_xpath(read_xpath('get_pic','all_shown')))

def pic_from_explore(browser, ptype):
    return(browser.find_element_by_xpath(read_xpath('get_pic','recent')))

def current_url(browser):
    """ Get URL of the loaded webpage """
    try:
        current_url = browser.execute_script("return window.location.href")

    except WebDriverException:
        try:
            current_url = browser.current_url

        except WebDriverException:
            current_url = None

    return current_url

def follow_status(browser):
    status = browser.find_element_by_xpath(read_xpath('get_following_status','follow_button_XP')).text
    return(status)

def follower_to_following_ratio(browser, username):
    web_nav.go_to_profile(browser, username)

    try:
      followers = follower_count(browser)
      following = following_count(browser)

    except NoSuchElementException:
      browser.execute_script("location.reload()")
      
      try:
        followers = follower_count(browser)
        following = following_count(browser)

      except NoSuchElementException:
        print("this user has no followers")
        following = 1

    f_ratio = round(followers/following,3)

    return(followers, following, f_ratio)

def pic_caption(browser):
    try:
      cap = WebDriverWait(browser, 10).until(
      EC.presence_of_all_elements_located((By.XPATH, read_xpath('comments','comment_section')))
      )   

    except TimeoutException:
      print("No caption on this post")
      cap = None
    
    if cap:
      cap = cap[0].text
      cap = cap.lower()
    
    return(cap)

def datetime_of_post(browser):
    t = browser.find_element_by_xpath(read_xpath('post','timestamp')).get_attribute('datetime')
    return(t)

def media_type(browser):
    type = 'pic'
    try:
        type = WebDriverWait(browser, 10).until(
          EC.visibility_of_element_located((BY.XPATH, read_xpath('post','video_identifier'))))
        type = type.get_attribute('type')
    except NoSuchElementException:
        pass

    return(type)