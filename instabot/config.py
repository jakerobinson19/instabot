#configuration parameters for how the bot will run and what profiles/pics it will engage with
USERNAME = 'two_wieners'
PASSWORD = 'WEiner19!'

# Set the number of likes and comments you would like to perform for run of the bot 
MAX_LIKES = 500
MAX_COMMENTS = 65

#apparently 350 likes/hour is the limit
PROFILES_PER_TAG = 5
LIKES_PER_PROFILE = 3

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

FOLLOW_BACK = False
FOLLOW_PER_DAY = 10
FOLLOWER_TO_FOLLOWING_RATIO_LIMIT = 3

BAD_WORDS = ['surgery','dead','rip','sad','death','tears','worst',
			 'pain','danger','terrible','awful','memory','peace',
			 'killed','urgent','notice', 'losing','long sleeve', 't-shirt',
			 'international delivery', 'made in the usa','get it now','life threatening',
			 'horrific','life-threat']

HASHTAG_LIST = ['dachshund', 'dachshunds', 'dachshundsonly', 'dachshund_love',
                'doxiesofig', 'doxiefever', 'dachshundgram', 'dachshundlife',
                'dachshund_feature','dachshundnation','doxiesofig','sausagedogs',
                'dachshundsarethebest','dachshundobsessed','doxies', 'dogoftheday',
                'dachshundoftheday','dachshundmoments','fluffy','dogs',
                'dachshundlovers','dogphotography','dachshundappreciation','wienerdog',
                'wienerdogs','wienerdogworld','minisausagedog','weinerdogsofinstagram',
                'minidoxie','doxiepuppy','miniaturedachshund','dachshund_corner',
                'dachshundpuppy','dackel','doglover','petstagram','instadog','dogoftheday',
                'dogsofinstagram']

USERNAMES_TO_IGNORE = ['lovedachshund.mag', 'doxie.obsessed','dach_usa_love']

# database configuration
DB_PATH = '/Users/jakerobinson/Desktop/instabot_db.sqlite'
DB_NAME = 'instabot_db'

# chromedriver path
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
