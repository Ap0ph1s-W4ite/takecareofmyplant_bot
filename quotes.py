import xml.etree.ElementTree as ET
import urllib2
import re
import time
import logfile
import reply_plant as rp
import best_api as ba
import another_api as ana

def quote(decision):
    control = ba.api()
    logfile.logger('debug', 'Best API analyzed to control...')
    while True:
        if (control == 'false'):
            quote = ana.api()
            logfile.logger('info', 'Another API selected')
        else:
            quote = ba.api()
            logfile.logger('info', 'Best API selected')

        print quote
        logfile.logger('info', 'Quote: ' + quote)

        if (quote == 'you are who you are and no one can change that. so be yourself because no one can do it better.'):
            quote = 'again the same quote?'
            logfile.logger('error', 'That stupid quote again!')

        if (re.search(r'\byes\b', quote, re.IGNORECASE) and re.search(r'\bno\b', quote, re.IGNORECASE)):
            quote = 'Quote not valid.'
            logfile.logger('error', 'Invalid quote.')

        if (decision == 'yes'):
            if re.search(r'\byes\b', quote, re.IGNORECASE) or re.search(r'\baye\b', quote, re.IGNORECASE):
                logfile.logger('debug', 'Quote selected to publish.')
                return quote
                break
        if (decision == 'no'):
            if re.search(r'\bno\b', quote, re.IGNORECASE):
                logfile.logger('debug', 'Quote selected to publish.')
                return quote
                break

def author():
    tree = ET.parse('quotes.xml')
    root = tree.getroot()

    author = root[0][1].text
    print author
    logfile.logger('debug', 'Author selected to publish.')
    return author

def action(res):
    logfile.logger('debug', 'Decision received!')
    qt = quote(res)
    aut = author()
    rp.reply(qt,aut)
    logfile.logger('debug', 'Quote and Author sent to the publisher script!')
