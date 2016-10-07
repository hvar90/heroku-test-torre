from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
import home.views

# Examples:
# url(r'^$', 'heberthTestTorre.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', home.views.index, name='index'),  
    url(r'^admin/', include(admin.site.urls)),
	url(r"^api/1\.0/", include("apiV1.urls")),     
]
