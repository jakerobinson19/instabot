#!/usr/bin/env python

from selenium.webdriver.common.keys import Keys
import retrieve
import config

web = {}

web['url'] = {
    'login':'https://www.instagram.com/accounts/login/',
    'feed': 'https://www.instagram.com/',
    'hashtag':'https://www.instagram.com/explore/tags/'
}

def right_arrow(browser):
    body = browser.find_element_by_tag_name('body')
    body.send_keys(Keys.ARROW_RIGHT)

def left_arrow(browser):
    body = browser.find_element_by_tag_name('body')
    body.send_keys(Keys.ARROW_LEFT)

def go_to_url(browser, page):
    browser.get(page)

def go_to_feed(browser):
    browser.get(web['url']['feed'])
                
def go_to_profile(browser, uname = None):
    if uname == None:
        uname = config.USERNAME
    browser.get('https://www.instagram.com/{}'.format(uname))

def go_to_hashtag(browser, hashtag):
    browser.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))

def select_pic_on_explore_page(browser, ptype):
    pic = retrieve.pic_from_explore(browser, ptype)
    pic.click()