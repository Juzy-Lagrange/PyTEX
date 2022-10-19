import sys

class __CORE():
	def __init__(self):
		self.__FILESTREAM = ""

	def StdOut(self,filename):
		self.__FILESTREAM = open("%s"%(filename), "w")
		sys.stdout = self.__FILESTREAM
		return self.__FILESTREAM 