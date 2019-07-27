#!/usr/bin/env python

from selenium.webdriver.common.keys import Keys

def right_arrow(browser):
    body = browser.find_element_by_tag_name('body')
    body.send_keys(Keys.ARROW_RIGHT)

def left_arrow(browser):
    body = browser.find_element_by_tag_name('body')
    body.send_keys(Keys.ARROW_LEFT)

def go_to_feed(browser):
    browser.get('https://www.instagram.com/')
                
def go_to_profile(bot, uname = None):
    if uname == None:
        uname = bot.email
    bot.browser.get('https://www.instagram.com/{}'.format(uname))

def go_to_hashtag(browser, hashtag):
    browser.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
  
