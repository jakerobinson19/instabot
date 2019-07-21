"""selenium modules"""
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
    
def comments_on_post(browser):
    return(browser.find_elements_by_xpath(read_xpath('comments','comments_on_pic')))
      
def like_button(browser):
    wait = WebDriverWait(browser, 10)
    
    like_button = wait.until(EC.visibility_of_element_located((By.XPATH, read_xpath('like_button','like_button'))))
    return(like_button)
    
def feed_like_buttons(browser):
    hearts = browser.find_elements_by_xpath("//span[@class='fr66n']")
    return(hearts)
    
def follower_count(browser):
    follower_element = browser.find_element_by_partial_link_text("followers").find_element_by_xpath('span')
    follower_count = int(follower_element.get_attribute('title').replace(',',''))

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
