import time

class logModule:
	def __init__(self):
		self.debugFlag = 0
	def info(self,act):
		print (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+ ' Info: ' + act + "\n")
	def debug(self,act):
                if self.debugFlag is 1:
                    print (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+ ' Debug: ' + act + "\n")
	def error(self,act):
		print (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+ ' Error: ' + act + "\n")

#logger = logModule()
#logger.info('test')
#logger.debug('test')
#logger.error('test')
