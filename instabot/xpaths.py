#!/usr/bin/env python
# -*- coding: utf-8 -*-

xpath = {}

xpath['get_count'] = {
      'followers':'span',
      'following':'span'
}
          
xpath['get_pic'] = {
      'all_shown': "//div[@class='v1Nh3 kIKUG  _bz0w']",
      'recent': '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a',
      'top': '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a'
}

xpath['comments'] = {
      'comments_on_pics':"//ul[@class='Mr508']",
      'username_on_comment':'//*/div/li/div/div[1]/div[2]/h3/a'
}
      
xpath['like_button'] = {
      'like_button':"//span[@class='fr66n']",
      'heart_outline': "//button/span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']",
      'heart_filled': "//button/span[@class='glyphsSpriteHeart__filled__24__red_5 u-__7']"
}
      
xpath['notification_wall'] = {
      'not_now':"//button[text()='Not Now']",
      'turn_on':"//div/h2[text()='Turn on Notifications']"
}

xpath['buttons'] = {
      'first_next':'/html/body/div[3]/div[1]/div/div/a',
      'next': '/html/body/div[3]/div[1]/div/div/a[2]'
}

xpath['get_status'] = {
    "follow_button_XP":"//button[text()='Following' or \
                                  text()='Requested' or \
                                  text()='Follow' or \
                                  text()='Follow Back' or \
                                  text()='Unblock']"
}

selector = {}
      
selector['login_elem'] = {
      'username': 'form input',
      'login': 'form input'
}

selector['elements'] = {
      'comment_box': "textarea.Ypffh",
      'profile_username':'h2.BrX75'
}
