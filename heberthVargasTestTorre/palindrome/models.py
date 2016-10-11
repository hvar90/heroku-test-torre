"""la complejidad  esta dada  por la cantidad de
	numeros palindromes que hay contando desde el numero 1
	hasta el numero superior del rango dado			
	la complejidad puede ser vista de orden logaritmico
	si nuestro n=y-x donde X y Y son nuestros limites inferior y superior 
	en el rango de numeros para obtener numeros palindromos
	entonces la complejidad es O(log (y-x))	
	por ultimo si npal= numero total de palindromos en nuestro rango
	entonces a esto se le suma los ciclos de nuestros 2 ciclos While
	cada ciclo while es aproximadamente igual a la mitad 
	del total de numeros palindromos npal/2, por ser valores
	pequenos no afectan mucho a la complejidad del programa"""		  
class PalindromeBinary(object) :	
	
	def get_palindrome_list(self,x,y):		
		self.num_cycles=0
		result=list(self._make_gen(x,y))	
		complexity="{0}+O(log{1})".format(self.num_cycles-len(result),y-x)		
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
		
		
		
		

		
	
