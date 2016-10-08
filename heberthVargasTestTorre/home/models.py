

class PalindromeBinary(object) :	
	def get_palindrome_list(self,x=1,y=1000001):
		global num_cycles
		num_cycles=0
		is_palindrome=self._is_palindrome
		result=[num for num in xrange(x,y)
				  if is_palindrome(bin(num)[2:])]
		complexity="{0}*O({1})".format(
								(y-x), len(str(bin((y))[2:])))	
		"""la complejidad esta dada por el tamano del mayor numero en binario
		osea len((bin(y)) esto se multiplica por la cantidad de
		numeros totales a analizar osea (y-x)"""	  
		return {"total_palindromes":len(result),
				"list_palindrome":result,
				"total_cycles":num_cycles+y-x,
				"complexity": complexity}
		
		
		
	def _is_palindrome(self,word):
		global num_cycles
		inverseWord = word[::-1]
		for index,letter in enumerate(word) :
			num_cycles+=1
			if inverseWord[index] != letter:
				return False 
		return True
		
		
		
		

		
	
