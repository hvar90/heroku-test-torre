

class PalindromeBinary(object) :	
	def get_palindrome_list(self,x=1,y=1000001):
		self._num_cicles=0
		is_palindrome=self._is_palindrome
		result=[num for num in xrange(x,y)
				  if is_palindrome(bin(num)[2:])]
		complexity="{0}*O({1})".format(
						(y-x), len(str(bin((y))[2:])))	
		"""la complejida esta dada por el tamano del mayor numero en binario
		osea len((bin(y)) esto se multiplica por la cantidad de
		numeros totales a analizar osea (y-x)"""	  
		return {"total_palindromes":len(result),
				"list_palindrome":result,
				"total_cycles":self._num_cicles+y-x,
				"complexity": complexity}
		
		
		
	def _is_palindrome(self,word):
		inverseWord = word[::-1]
		for index,letter in enumerate(word) :
			self._num_cicles+=1
			if inverseWord[index] != letter:
				return False 
		return True
		
		
		
		

		
	
