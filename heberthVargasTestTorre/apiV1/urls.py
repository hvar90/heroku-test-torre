from django.conf.urls import url, include


#urlpatterns = patterns("", url(r"^$", "api"),
  
    ##url(r"^", include("api1.message.urls")),
 
#)
urlpatterns = [
     url(r"^", include("apiV1.test.urls")), 
]

