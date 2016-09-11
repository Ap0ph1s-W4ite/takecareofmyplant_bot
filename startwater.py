import praw
import re
import datetime
import os
import sys
import logging
from config import *

if __name__ == "__main__":
    now = datetime.datetime.now()
    day = now.day
    day = str(day)

    logging.basicConfig(filename='/home/pi/JeffPlant/logs/failsafe.log', format='[%(asctime)s]%(levelname)s:%(message)s', level=logging.DEBUG)

    logging.info('Today is ' + day + ' and the script will start!')
   
    user_agent = ("NukeWifeGuy vote to water (failsafe)!")
    r = praw.Reddit(user_agent=user_agent)
    
    logging.info('Logging in...')
    r.login(REDDIT_USERNAME, REDDIT_PASS)
    logging.debug('Logged in!')

    commented = 0

    subreddit = r.get_subreddit('takecareofmyplant')
    logging.debug('Sub-Reddit analyzed.')
    for submission in subreddit.get_hot(limit=5):
        logging.debug('Submission downloaded.')
        if re.search(day, submission.title, re.IGNORECASE):
            logging.debug('Today submission selected.')
            flat_comments = praw.helpers.flatten_tree(submission.comments)
            already_done = set()
            for comment in flat_comments:
                if re.search(r'\bNukeWifeGuy\b', comment.author.name, re.IGNORECASE):
                    commented = 1
                    logging.info(comment.author.name + ' comment found. Nothing to do here...')
                else:
                    logging.info(comment.author.name + ' comment found.')
                    continue
            if (commented == 1):
                logging.debug('Comment found, the script will close.')
                continue
            else:
                logging.debug('Comment not found, the script will restart.')
                os.system("sudo python /home/pi/JeffPlant/auto_water.py")
                logging.debug('Script closed')
                sys.exit()

        else:
            logging.error('Not the valid submission.')
