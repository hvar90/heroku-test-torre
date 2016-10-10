class PalindromeBinary(object) :	
	def get_palindrome_list(self,x,y):		
		is_palindrome=self._is_palindrome
		result=[num for num in xrange(x,y)
				  if is_palindrome(bin(num)[2:])]
		complexity="O({0})".format(y-x)	
		"""la complejidad  esta dada  por la cantidad de
		numeros totales a analizar osea (y-x)
		osea tiene una complejidad lineal O(y-x)"""	  
		return {"total_palindromes":len(result),
				"list_palindrome":result,
				"total_cycles":y-x,
				"complexity": complexity}	
		
	def _is_palindrome(self,word):						
			return word[::-1]==word
		
		
		
		
		

		
	
