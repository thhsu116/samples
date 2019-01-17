import logging

logger = logging.getLogger()

def init_logging1(logfile):
    format_str = '%(asctime)s | %(levelname)-8s | %(threadName)-10s | %(filename)s (%(lineno)d) | %(message)-s'
    date_format = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(format_str, date_format)
    logging.basicConfig(filename=logfile, level=logging.DEBUG, format=format_str)
    
    global logger
    
    # only show INFO level in stdout
    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(logging.INFO)
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    
    return logger

def init_logging2(debug=False):
    format_str = '%(asctime)s | %(levelname)-8s | %(threadName)-10s | %(filename)s (%(lineno)d) | %(message)-s'
    logging.basicConfig(format=format_str, level=logging.DEBUG)
    
    global logger
    
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
