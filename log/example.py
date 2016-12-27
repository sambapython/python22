import logging
import mod1
#logging.info(mod1.fun())
logging.basicConfig(filename='log1.txt',
	level=logging.DEBUG, format="%(asctime)s->%(levelname)s->%(message)s")
logging.info(mod1.fun())
logging.info("program started")
a=raw_input("Enter number to divide 100: ")
if not a.isdigit():
	logging.warn("{0} is going to crash your application".format(a))
try:
	a=int(a)
	res = 100/a
	logging.info("res={0}".format(res))
	
except Exception as err:
	logging.exception(err)
logging.info("program ended")


