from selenium import webdriver
import random
import emoji

wordOptions = [['Omg','So','Absolutely','You are',],['the cutest','adorable','lovely','so sweet']]
emojiOptions = [':heart:',':heartpulse:',':two_hearts:',':kissing_heart:',':heart_eyes:','

def createComment():
  comment = None
  
  firstWord = wordOptions[0][random.randint(0,len(wordOptions[0])-1)]
  secondWord = wordOptions[1][random.randint(0,len(wordOptions[1])-1)]
  emoji = emojiOptions[random.randint(0,len(emojiOptions)-1)]
  
  comment = firstWord + ' ' + secondWord + ' ' + emoji
  return(comment)

def getNumberOfComments():



def getComments():



