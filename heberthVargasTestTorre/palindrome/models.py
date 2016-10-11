class PalindromeBinary(object) :	
	
	def get_palindrome_list(self,x,y):		
		self.num_cycles=0
		result=list(self._make_gen(x,y))	
		complexity="O({0})".format(self.num_cycles)
		"""la complejidad  esta dada  por la cantidad de
		numeros palindromes que hay contando desde el numero 1
		hasta el numero superior del rango dado
		la formula para hallar la cantidad de numeros palindromes desde 
		1 hasta nuestro limite de nuestro rango superior es  3·2(n-1)/2 – 2 ,
		ver : http://www.exploringbinary.com/counting-binary-and-hexadecimal-palindromes
		y n seria la cantidad de digitos binarios que tenga nuestro 
		limite superior de nuestro rango es decir len(bin(y))
		esto haria que la complejidad sea de orden exponencial respecto
		a la cantidad de digitos binarios de nuestro limite superior del rango		 
		osea tiene una complejidad exponencial O(a**n))
		donde a es 2 y n=len(bin(y))
		por ultimo si npal= numero total de palindromos en nuestro rango
		entonces a esto se le suma los ciclos de nuestros 2 ciclos While
		cada ciclo while es aproximadamente igual a la mitad 
		del total de numeros palindromos npal/2
		la complejidad tambien puede seri vista de orden logaritmico
		si nuestro n=y-x entonces la complejidad es O(log (y-x))"""		  
		return {"total_palindromes":len(result),
				"list_palindrome":result,
				"total_cycles":self.num_cycles,
				"complexity": complexity}	
		
	def _make_gen(self,start,end):
		gen=self._palgen_base2()	
		while True:
			self.num_cycles+=1	
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
			self.num_cycles+=1	
			for y in xrange(n, n2):
				s = format(y, 'b')
				self.num_cycles+=1			
				yield int(s+s[-2::-1], 2)
			for y in xrange(n, n2):
				s = format(y, 'b')
				self.num_cycles+=1				
				yield int(s+s[::-1], 2)
			x += 1
			n *= 2
			n2 *= 2
		
		
		
		

		
	
