import praw
import re
import datetime
import quotes
import logfile
from config import *

if __name__ == "__main__":
    now = datetime.datetime.now()
    day = now.day
    day = str(day)

    votes = []

    f = open('/home/pi/JeffPlant/logs/vote.log', 'r+')

    user_agent = ("NukeWifeGuy vote to water!")
    r = praw.Reddit(user_agent=user_agent)
    
    logfile.logger('info', 'Logging in...')
    r.login(REDDIT_USERNAME, REDDIT_PASS)
    logfile.logger('debug', 'Logged in!')

    subreddit = r.get_subreddit('takecareofmyplant')
    logfile.logger('debug', 'Sub-Reddit analyzed.')
    for submission in subreddit.get_hot(limit=5):
        if re.search(day, submission.title, re.IGNORECASE):
            body = submission.selftext
            logfile.logger('debug', 'Body from the daily thread downloaded.')
    words = re.compile(r'\bYES\b | \bNO\b', flags=re.I | re.X)
    logfile.logger('debug', 'Body analized')
    votes = words.findall(body)

    if (votes[8] == 'yes' and votes[9] == 'no' and votes[10] == 'no' and votes[11] == 'no'):
        f.write('yes')
        f.close()
        quotes.action('yes')
        logfile.logger('info', 'The decision was "yes"')
    elif (votes[8] == 'no' and votes[9] == 'yes' and votes[10] == 'no' and votes[11] == 'no'):
        f.write('yes')
        f.close()
        quotes.action('yes')
        logfile.logger('info', 'The decision was "yes"')
    else:
        f.write('no')
        f.close()
        quotes.action('no')
        logifle.logger('info', 'The decision was "no"')
