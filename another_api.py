import urllib2
import xml.etree.ElementTree as ET
import time
import logfile

def api():
    url = "http://api.forismatic.com/api/1.0/?method=getQuote&format=xml&lang=en"

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

    quote = root[0][0].text
    
    time.sleep(2)

    return quote
    logfile.logger('debug', 'Quote script closed...')
