
from .import views
from django.urls import path

# urlpatterns = [
   
#     path('',include('weatherlookup.url')),
# ]

urlpatterns = [
   
    path('',views.home, name="home"),
    path('about.html',views.about, name="about"),

    #path('about.html', views.home, name="home")

]