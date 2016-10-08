from rest_framework.views	         import APIView
from rest_framework					 import status
from rest_framework.response		 import Response
from home.models                     import PalindromeBinary
from json import dumps

class ValidationError(Exception):
	pass
	
class PalindromeView(APIView):	
	def get(self, request,x,y, *args, **kwargs):	
		try:			
			result =dumps(
					PalindromeBinary().get_palindrome_list(int(x),int(y))) 
		except ValidationError as e:
			return Response(
					{"detail": e.message},status.HTTP_400_BAD_REQUEST, )	   
		return Response(result)   
	
	
