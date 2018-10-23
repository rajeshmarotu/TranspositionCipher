import random
import math

class TranspositionCipher():
	def __init__(self,dimension):
		self.dimension = dimension
		self.size = dimension*dimension
		self.key = self.permuteKey(self.size)
		self.encrypted=""
		self.decrypted=""
	

	def permuteKey(self, size):
		a=[i for i in range(0,size)]
		random.shuffle(a)
		return a
	
	
	def encryptMessage(self,plainText):
		l = len(plainText)
		for i in range(0,l,self.size):
			matrix = self.convertPlainTextToMatrix(plainText,i)
			self.encrypted += self.encryptIndividualMatrix(matrix)
		return self.encrypted

	
	def convertPlainTextToMatrix(self,plainText,index):
		a=[]
		plainText=plainText[index:index+self.size]
		l=len(plainText)
		for i in range(self.dimension):
			a.append([])
			for j in range(self.dimension):
				if(i*self.dimension+j>=l):
					a[i].append("*")
				else:	
					a[i].append(plainText[i*self.dimension+j])	
		return a
	def encryptIndividualMatrix(self,matrix):
		encryptedText = ""
		for k in range(self.size):
			i=int(self.key[k]/self.dimension)
			j=int(self.key[k]%self.dimension)
			encryptedText += matrix[i][j]
	
		return encryptedText	

	
	def decryptMessage(self,cipherText):
		l=len(cipherText)
		for j in range(0,l,self.size):
			convertedMatrix = self.convertCypherTextToMatrix(cipherText,j)
			self.decrypted += self.readMatrixRowWise(convertedMatrix)
		return self.decrypted.replace("*","")	

	def convertCypherTextToMatrix(self,cipher,index):
		cipher=cipher[index:index+self.size]
		matrix = [[0,0,0],[0,0,0],[0,0,0]]
		for k in range(self.size):
			i=int(self.key[k]/self.dimension)
			j=int(self.key[k]%self.dimension)
			matrix[i][j]=cipher[k]
		return matrix

	def readMatrixRowWise(self,convertedMatrix):
		text=""
		for i in range(self.dimension):
			for j in range(self.dimension):
				text += convertedMatrix[i][j]
		return text


if __name__=="__main__":
	t = TranspositionCipher(3)
	plainText = input("Enter plain Text\n")
	encryptedMessage = t.encryptMessage(plainText)
	print("Encrypted message:\n")
	print(encryptedMessage.replace("*",""))
	print("\n")
	decryptedMessage = t.decryptMessage(encryptedMessage)
	print("Decrypted message:")
	print(decryptedMessage)
	
