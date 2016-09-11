import logging

def logger(level, message):

    logging.basicConfig(filename='/home/pi/JeffPlant/logs/script.log', format='[%(asctime)s]%(levelname)s:%(message)s', level=logging.DEBUG)

    if (level == 'debug'):
        logging.debug("%s" % message)

    if (level == 'info'):
        logging.info('%s' % message)

    if (level == 'warning'):
        logging.warning('%s' % message)

    if (level == 'error'):
        logging.error('%s' % message)

    if (level == 'critical'):
        logging.critical('%s' % message)
