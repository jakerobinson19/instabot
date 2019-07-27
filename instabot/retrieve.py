"""selenium modules"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

"""Exceptions"""
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException

from finder_function import read_xpath
from finder_function import read_selector


def username_from_profile(browser):
    wait = WebDriverWait(browser, 10)
    uname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, read_selector('elements','profile_username'))))
   
    return(uname)
    
def get_usernames_from_comments(self):
    comm_unames = WebDriverWait(self.browser, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, read_xpath('comments','comments_on_pic')))
    )   
    return(comm_unames)
  
def get_comments_on_post(self):
    comms = WebDriverWait(self.browser, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, read_xpath('comments','comment_section')))
    )   
    return(comms)

def like_button(browser):
    wait = WebDriverWait(browser, 10)
    
    like_button = wait.until(EC.visibility_of_element_located((By.XPATH, read_xpath('like_button','like_button'))))
    return(like_button)
    
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
    following_count = int(following_element.get_attribute('title').replace(',',''))

    return(following_count)
    
def pics_from_profile(browser):
    return(browser.find_elements_by_xpath(read_xpath('get_pic','all_shown')))

def get_current_url(browser):
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

def follower_to_following_ratio(browser, my_name, username):
    web_nav.go_to_profile(my_name, username)

    try:
      followers = follower_count()
      following = following_count()
    except NoSuchElementException:
      browser.execute_script("location.reload()")
      try:
        followers = follower_count()
        following = following_count()
      except NoSuchElementException:
        print("this user has no followers")
        following = 1

    f_ratio = round(followers/following,3)
    return(f_ratio)
