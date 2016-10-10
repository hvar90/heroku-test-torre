class PalindromeBinary(object) :	
	
	def get_palindrome_list(self,x,y):			
		result=[num for num in xrange(x,y)
				  if lambda x: x[::-1]==x (bin(num)[2:]) ]
		complexity="O({0})".format(y-x)	
		"""la complejidad  esta dada  por la cantidad de
		numeros totales a analizar osea (y-x)
		osea tiene una complejidad lineal O(y-x)"""	  
		return {"total_palindromes":len(result),
				"list_palindrome":result,
				"total_cycles":y-x,
				"complexity": complexity}	
		

		
		
		
		
		

		
	
