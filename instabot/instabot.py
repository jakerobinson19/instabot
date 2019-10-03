#!/usr/bin/env python

import argparse
import config
from run_bot import run_bot

# Selenium exception used when the bot is blocked
from selenium.common.exceptions import ElementClickInterceptedException

'''
File call to initiate run of the bot

Pass arguments to the program to change username, password, or desired 
comments and likes for the bot to perform (if it differs from config)

Options:
-u username
-p password
-l max pics to like
-c max comments to post

usage: instabot.py [-h] [-u username] [-p password] [-l likes] [-c comments]
'''

# Parse arguments from command line
parser = argparse.ArgumentParser(description='Automated Bot for Instagram using Python and Selenium')
parser.add_argument('-u', '--username', metavar='USERNAME', type=str, default = config.USERNAME, help='Instagram username handle', dest='username')
parser.add_argument('-p', '--password', metavar='PASSWORD', type=str, default = config.PASSWORD, help='Password for Instagram account', dest='password')
parser.add_argument('-l', '--likes', metavar='LIKES', type=int, default=config.MAX_LIKES, help='Number of Likes you want the bot to perform', dest='max_likes')
parser.add_argument('-c', '--comments', metavar='COMMENTS', type=int, default=config.MAX_COMMENTS, help='Number of Comments you want the bot to perform', dest='max_comments')

args = parser.parse_args()

try:
  run_bot(args.username, args.password, args.max_comments, args.max_likes)

except ElementClickInterceptedException:
  
    print (" It appears that the bot has been blocked :( ")
    print (" Please check that you're configuration parameters are reasonable")
    print (" We will pause until further notice")
  
except KeyboardInterrupt:
    
    print("Exiting. Goodbye :)")
