#!/usr/bin/env python

import config
import retrieve
import comment_util

def validate_username(usname):
    records = databse_handler.select_username_from_table(usname)

    if usname == config.USERNAME:
      return(False, msg)
    elif records:
      for r in records:
        if r[4] > config.follower_to_following_ratio_limit:
          msg = "------ Username is in the blacklist ------"
          return(False, msg)
        
        elif r[6] in date_range:
          msg = "------ Engaged with this username before ------"
          return(False, msg)
        
        else:
          return(True, None)
    else:
      return(True, None)

def validate_engagement(browser, post):
    follow_stat = retrieve.follow_status(browser)
    media_type = retrieve.media_type(browser)

    if follow_stat:
      pass

    return(exit, comment_allowed, like_allowed)

def validate_caption(browser):
    caption = retrieve.pic_caption(browser)

    abort = False
    
    for word in config.ignore_if_contains:
      if word in caption:
        print("Bad word in the caption ({})".format(word))
        abort = True

    return(abort)

def already_liked(element):
    not_liked = True

    try:
      heart_button = retrieve.heart_button(element)
    except NoSuchElementException:
      print('Picture already liked, moving on...')
      not_liked = False

    return(not_liked)

def already_commented_on(bot):
    already_commented = False

    comms = comment_util.get_comments_on_post()
    
    for c in comms:
      if c.text == config.USERNAME:
        already_commented = True

    return(already_commented)
