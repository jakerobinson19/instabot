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
      'comments_on_pic':"//a[@class='FPmhX notranslate TlrDj']",
      'comment':'//*/div/li/div/div[1]/div[2]/h3/a',
      'comment_section':"//div[@class='C4VMK']"
}         
      
xpath['like_button'] = {
    'like_button':"//span[@class='fr66n']",
    'heart_outline': "//span[@class='fr66n']",
    'heart_filled': "//span[@class='FY9nT fr66n']"
    # old x_paths
    # 'heart_outline': "//button/span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']",
    # 'heart_filled': "//button/span[@class='glyphsSpriteHeart__filled__24__red_5 u-__7']",
}

xpath['status'] = {
      'following':"//*/button[contains(text(), 'Follow')]",
      'unfollow':"//button[text()='Unfollow']"
}
      
xpath['notification_wall'] = {
      'not_now':"//button[text()='Not Now']",
      'turn_on':"//div/h2[text()='Turn on Notifications']"
}

xpath['buttons'] = {
      'first_next':'/html/body/div[3]/div[1]/div/div/a',
      'next': '/html/body/div[3]/div[1]/div/div/a[2]'
}

xpath['get_following_status'] = {
    "follow_button_XP":"//button[text()='Following' or \
                                  text()='Requested' or \
                                  text()='Follow' or \
                                  text()='Follow Back' or \
                                  text()='Unblock']"
}

xpath['post'] = {
    'video_identifier': '//video',
    'video_tag': "//div[@class'ZyFrc']",
    'timestamp':"//time[@class='_1o9PC Nzb55']"
}

selector = {}

selector['login_elem'] = {
      'username': 'form input',
      'login': 'form input'
}

selector['elements'] = {
      'comment_box': "textarea.Ypffh",
      'profile_username':'div.e1e1d',
      'datetime_stamp':'_1o9PC Nzb55'
}
