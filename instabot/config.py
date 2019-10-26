# Configuration parameters for how the bot will run and what profiles/pics it will engage with

# Enter username and password of account here 
# These can also be provided as arguments when running if desired
USERNAME = ''
PASSWORD = ''

# Set the number of likes and comments you would like to perform for run of the bot 
MAX_LIKES = 300
MAX_COMMENTS = 65

# How many profiles to interact with per hashtag and how many pics to like for each profile
PROFILES_PER_TAG = 5
LIKES_PER_PROFILE = 4

# Set number of hours you would like the bot to run for
RUN_TIME = 6
delay_time = 30
delay_variance = 25

COMMENT_IF_FOLLOWING = False
LIKE_IF_FOLLOWING = True
INTERACT_IF_FOLLOW_BACK = False
COMMENT_ON_VIDEOS = True
LIKE_VIDEOS = True
COMMENT_ON_PICS = True
LIKE_PICS = True

DAYS_TO_REFRESH_USERNAMES = 13

# Any profile above this limit will be added to the blacklist and not engaged with
FOLLOWER_TO_FOLLOWING_RATIO_LIMIT = 3

WORD_OPTIONS = [['Wow, ','So','Absolutely',"Holy fluff. You're", 'Awwww', "By our fluffy paws! You're ", 'Absocutely'],
               ['so cute','adorable','lovely','so sweet','so so adorable','fabulous'],
               ['! ','!! ','!!! ']]

EMOJI_OPTIONS = ['❤️', '❤️🥰❤️', '❤️❤️❤️', '💕💕💕', '🔥', '🔥🔥' ,'😍', '😍😍', '😍🥰', '🥰💕']

# Words that will cause the bot to avoid the post or not comment/like if found in the caption
BAD_WORDS = ['surgery','dead','rip','sad','death','tears','worst',
	     'pain','danger','terrible','awful','memory','killed']

# List of hashtags to explore and engage with profiles from
HASHTAG_LIST = ['dog', 'cat']

# Profiles that you never wish to interact with
USERNAMES_TO_IGNORE = []

# Set to False if you would like to see the username lists printed out in the command line to verify things are functioning
SUPPRESS_FULL_LOG = True

# Database configuration
DB_PATH = '/Users/new_bot/instabot/instabot/instabot_db.sqlite'
DB_NAME = 'instabot_db'

# Chromedriver path
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
