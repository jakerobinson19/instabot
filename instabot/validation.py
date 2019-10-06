#!/usr/bin/env python

import config
import retrieve
import comment_functions

def validate_config_parameters():
  stop_bot = False
  msg = ''

  if len(config.HASHTAG_LIST) == 0:
    msg = 'No hashtags have been input for the bot to explore. Please add them to the HASHTAG_LIST in config.py'
    stop_bot = True

  elif len(config.WORD_OPTIONS) == 0:
    msg = ('No words have been input for the bot to comment with. Please add them to the WORD_OPTIONS in config.py')
    stop_bot = True

  return(stop_bot, msg)

def validate_username(usname, blacklist, old_usernames):

    if usname == config.USERNAME:
      msg = "----- This is your username -----"
      return(False, msg)

    elif usname in blacklist:
      msg = "------ Username is in the blacklist ------"
      return(False, msg)

    elif usname in old_usernames:
      msg = "------ Engaged with this username before ------"
      return(False, msg)

    else:
      return(True, None)

def validate_profile(browser, follow_status):
    disengage, cant_comment, cant_like = False, False, False
    msg = "Disengaging"

    if follow_status == 'Follow Back' and not config.INTERACT_IF_FOLLOW_BACK:
      msg = "Status is Follow Back. Disengage!"
      disengage = True
    
    elif follow_status == 'Following':
      
      if not config.COMMENT_IF_FOLLOWING:
        cant_comment = True
      
      if not config.LIKE_IF_FOLLOWING:
        cant_like = True

    if cant_comment and cant_like:
      disengage = True

    return(disengage, cant_comment, cant_like, msg)

def validate_engagement(browser, tag):
  comment_allowed, like_allowed = True, True

  media_type = retrieve.media_type(browser)
  caption_check = validate_caption(browser)
  comments = comment_functions.get_comments_on_post(browser)
  
  if not check_for_hashtag_in_comments(comments, tag):
    comment_allowed = False

  if caption_check:
    comment_allowed = False

  if media_type == 'mp4':
      
    if not config.COMMENT_ON_VIDEOS:
      comment_allowed = False
      
    if not config.LIKE_VIDEOS:
      like_allowed = False
    
  else:
      
    if not config.COMMENT_ON_PICS:
      comment_allowed = False
      
    if not config.LIKE_PICS:
      like_allowed = False

  return(comment_allowed, like_allowed)

def validate_caption(browser):
    caption = retrieve.pic_caption(browser)

    abort = False
    
    if caption:
      for word in config.BAD_WORDS:
        if word in caption:
          abort = True

    return(abort)

def already_liked(element):
    not_liked = True

    try:
      heart_button = retrieve.heart_outline(element)
    except:
      print('Picture already liked, moving on...')
      not_liked = False

    return(not_liked)

def already_commented_on(browser):
    already_commented = False

    comms = comment_functions.get_comments_on_post(browser)
    
    for c in comms:
      if c.text == config.USERNAME:
        already_commented = True

    return(already_commented)

def check_for_hashtag_in_comments(comments, tag):
    approved = False

    if comments:
      for c in comments:
        if tag in c.text:
          return(True)

    return(approved)
