import retrieve
import validation
from time_functions import time_delay

from selenium.webdriver import ActionChains

def like_pic(browser):
    heart = retrieve.like_button(browser)
    time_delay()
    if validation.already_liked(heart):
      heart.click()

def like_pic_in_feed(browser, number = 1):
  loop = 1

  while loop <= number:
    hearts = retrieve.feed_like_buttons(browser)

    for h in range(len(hearts)):
      #print('liking the pic {}'.format(str(self.loop + 1)))
      time_delay()
      if validation.already_liked(hearts[h]):
        actions = ActionChains(browser)
        actions.move_to_element(hearts[h])
        actions.click(hearts[h])
        actions.perform()
        
      loop = loop + 1
      if loop > number:
        break
