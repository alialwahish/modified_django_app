
from django.conf.urls import url,include


urlpatterns = [
   
    url(r'^',include('apps.blogs_app.urls')),
    url(r'^survey',include('apps.surveysApp.urls')),
    url(r'^',include('apps.users.urls')),
    url(r'^',include('apps.users.urls')),
      
]
