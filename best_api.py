import urllib2 
import time
import logfile
import os
import sys
from config import *
import xml.etree.ElementTree as ET
 
def api():
    logfile.logger('debug', 'Geting the data from API...')
    url = "http://www.stands4.com/services/v2/quotes.php?uid={0}&tokenid={1}&searchtype=RANDOM"
    url = url.format(MYUID, MYTOKEN)
        
    s = urllib2.urlopen(url)

    logfile.logger('debug', 'URL content downloaded!')
    contents = s.read()

    file = open("quotes.xml", "w")
    file.write(contents)
    logfile.logger('debug', 'Quotes.xml updated')
    file.close()

    tree = ET.parse('quotes.xml')
    logfile.logger('debug', 'XML Parsed')
    root = tree.getroot()

    control = root[0].text
    
    time.sleep(2)

    if (control == 'Daily Usage Exceeded'):
        print ("**ERROR** The best API it's not availabe!")
        logfile.logger('error', "The best API it's not available!")
        return ('false')
    else:
        quote = root[0][0].text
        return quote
        logfile.logger('debug', 'Quote script closed...')
