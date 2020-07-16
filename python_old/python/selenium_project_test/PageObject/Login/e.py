import logging


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logfile = 'E:/python/PageObject/Report/runlog.log'
fh = logging.FileHandler(logfile)
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s:%(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

for i in fh,ch:
    logger.addHandler(i)
# logger.addHandler(fh)
# logger.addHandler(ch)



# logging.basicConfig(level=logging.DEBUG, filename='E:/python/PageObject/Report/runlog.log',
# #                     format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s')
#
#
logger.debug('debug info')
logger.info('info')
logger.warning('warning info')
logger.error('error info')
logger.critical('critical info')
