#!/usr/bin/env python
# -*- coding: utf-8 -*-

xpath = {}

xpath['get_count'] {
      'followers':'span'
      'following':'span'
          
xpath['get_pic'] {
      'all_shown': "//div[@class='v1Nh3 kIKUG  _bz0w']",
      'recent': '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a',
      'top': '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a'
}
      
xpath['like_button'] {
      'like_button':"//span[@class='fr66n']"
}

xpath['status'] {
      'follow':"//*/button[contains(text(), 'Follow')]",
      
xpath['notification_wall'] {
      'not_now':"//button[text()='Not Now']",
      'turn_on':"//div/h2[text()='Turn on Notifications']"
}

xpath['buttons'] {
      'first_next':'/html/body/div[3]/div[1]/div/div/a',
      'next': '/html/body/div[3]/div[1]/div/div/a[2]'
}
      
selector['login_elem'] {
      'username': 'form input',
      'login': 'form input'
}

selector['elements'] {
      'comment_box': "textarea.Ypffh",
      'profile_username':'h2.BrX75'
}
