import logging
logging.basicConfig(filename='log1.txt',
	level=logging.DEBUG, format="%(asctime)s->%(levelname)s->%(message)s")
logging.debug('debug')
logging.info('info')
logging.warn("warning")
logging.error('error')
logging.exception('exception')