from django.conf.urls                import url

from .views import *

urlpatterns = [ 
	      
    url(r"^palindrome/(?P<x>\d+)/(?P<y>\d+)/$",
        PalindromeView.as_view(),prefix='api1.palindrome.views'),
]


