import praw
import re
import datetime
import logfile
from config import *

def reply(quote, author):
    now = datetime.datetime.now()
    day = now.day
    day = str(day)

    user_agent = ("NukeWifeGuy vote to water")
    r = praw.Reddit(user_agent=user_agent)

    r.login(REDDIT_USERNAME, REDDIT_PASS)
    logfile.logger('debug', 'Logged in')

    subreddit = r.get_subreddit('takecareofmyplant')
    for submission in subreddit.get_hot(limit=5):
        if re.search(day, submission.title, re.IGNORECASE):
            submission.add_comment('"' + quote + '"' +' - ' +  '**' + author + '**')
            logfile.logger('debug', 'Quote was sent to Reddit!')
            logfile.logger('info', 'Script finished')

