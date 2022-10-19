from Core__ import __CORE
from DocumentClass import Document


class Tensor(__CORE): 

	def __init__ (self, *args, printStyle = "LaTEX"):
		self.tensor = list(i for i in args[0])
		self.printStyle = printStyle
		self.__size = [len(self.tensor),len(self.tensor[0])]
		self.tensorView = "()"
		self.__FILESTREAM = ' '

	def __mul__ (self,second):
		if (type(self) == type(second)):
			if (self.__size[1] == second.__size[0]):
				__newSize = [self.__size[0],second.__size[1]]
				__newTensor = [[0 for i in range(__newSize[1])] for i in range(__newSize[0])]

				for i in range(self.__size[0]):
					for j in range(self.__size[0]):
						for k in range(self.__size[1]):
							__newTensor[i][j] += self.tensor[i][k] * second.tensor[k][j]
			return Tensor(__newTensor)


		elif (type(second) == '__main__.Vector'):
			pass


		elif (type(second) == type(int())):
			__newTensor = [[i for i in self.tensor[j]] for j in  range(self.__size[0])]
			for i in range(self.__size[0]):
				for j in range(self.__size[1]):
					__newTensor[i][j] *= second
			return Tensor(__newTensor)


		else: 
			print(type(second))
			return "Uncorrect Type"


	def _SizePyTEX(self):
		print(self.__size)
		return "Don't use print, just write in code"

	def _PrintSizeLaTEX(self):
		print(self.__GenerateStringSize())
		return "Don't use print(_Print...), just write in code"

	def __GenerateStringSize(self):
		return "{%d}\\times{%d}"%(self.__size[0],self.__size[1])

	def __GenerateStringOutput (self):
		if (self.printStyle == "LaTEX"):
			__stringOutput = ""
			__stringOutput = __stringOutput + "\\left%s\n"%(self.tensorView[0])
			__stringOutput = __stringOutput + "\t\\begin{array}{%s}\n"%("c"*self.__size[1])
			for rows in self.tensor:
				countOfRows = len(rows)
				__stringOutput += "\t\t"
				for coloumn in range(countOfRows):
					if (countOfRows - 1 == coloumn):
						__stringOutput = __stringOutput + "%d "%rows[coloumn]
					else:
						__stringOutput = __stringOutput + "%d & "%rows[coloumn]
				__stringOutput = __stringOutput + "\\\\\n"
			__stringOutput = __stringOutput +  "\t\\end{array}\n"
			__stringOutput = __stringOutput +"\\right%s"%(self.tensorView[1])
			
		return __stringOutput


	def __str__ (self):
		__stringOutput = self.__GenerateStringOutput()
		return __stringOutput 


class Vector:

	def __init__ (self, *args, vectorType = "horizontal", printStyle = "LaTEX"):

		self.vector = list(map(int, args))
		self.firstElement = self.vector[0]
		self.lastElement = self.vector[-1]
		self.type = vectorType
		self.printStyle = printStyle


	def SetPrintType (self,type):
		if (type in "horizontal hor H h"):
			self.type = "horizontal"

		elif (type in "vertical vert V h"):
			self.type = "vertical"


	def __GenerateStringOutput (self):

		if (self.printStyle == "LaTEX"):
			__stringOutput = ""
			__stringOutput = __stringOutput + str(self.vector[0])

			if (self.type in "horizontal hor H h"):
				for vectorElement in self.vector[1:]:
					__stringOutput = __stringOutput + " & %d"%(vectorElement)

				return __stringOutput

			elif (self.type in "vertical vert V h"):
				__stringOutput += " \\\\\n"
				for vectorElement in self.vector[1:]:
					__stringOutput = __stringOutput + "%d \\\\\n"%(vectorElement)

				return __stringOutput

		elif (self.printStyle == "PyTex"):
			__stringOutput = "[ "
			__stringOutput = __stringOutput + str(self.vector[0])


			if (self.type in "horizontal hor H h"):
				for vectorElement in self.vector[1:-1]:
					__stringOutput = __stringOutput + ", %d"%(vectorElement)

				__stringOutput += " ]"

				return __stringOutput

			elif (self.type in "vertical vert V h"):
				__stringOutput += ",\n"
				for vectorElement in self.vector[1:-2]:
					__stringOutput = __stringOutput + "  %d,\n"%(vectorElement)
				else:
					__stringOutput = __stringOutput + "  %d ]"%(self.vector[-1])

				return __stringOutput

	def __str__ (self):
		__stringOutput = self.__GenerateStringOutput()
		return __stringOutput 

	
if __name__ == '__main__':
	pass