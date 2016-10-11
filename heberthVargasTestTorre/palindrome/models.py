class PalindromeBinary(object) :	
	
	def get_palindrome_list(self,x,y):		
		self.num_cycles=0
		result=list(self._make_gen(x,y))	
		complexity="O({0})".format(self.num_cycles)
		"""la complejidad  esta dada  por la cantidad de
		numeros numeros palindromes que hay contando desde el numero cero
		hasta el numero superior del rango dado
		osea tiene una complejidad lineal O(n)"""		  
		return {"total_palindromes":len(result),
				"list_palindrome":result,
				"total_cycles":self.num_cycles,
				"complexity": complexity}	
		
	def _make_gen(self,start,end):
		gen=self._palgen_base2()	
		while True:
			pal=next(gen)			
			if start<=pal<=end:
				yield pal
			elif pal>end:
				 break   
			
	def _palgen_base2(self): 
		"""este algoritmo esta creado basandose en la formula matematica
		para sacar secuencias de numeros binarios que sean palindromes
		ver: https://oeis.org/A006995"""  
		yield 0
		x, n, n2 = 1, 1, 2		
		while True:
			for y in range(n, n2):
				s = format(y, 'b')
				self.num_cycles+=1			
				yield int(s+s[-2::-1], 2)
			for y in range(n, n2):
				s = format(y, 'b')
				self.num_cycles+=1
				
				yield int(s+s[::-1], 2)
			x += 1
			n *= 2
			n2 *= 2
		
		
		
		

		
	
