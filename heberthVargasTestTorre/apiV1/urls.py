from django.conf.urls import url, include


urlpatterns = [
     url(r"^", include("apiV1.palindrome.urls")), 
]

