from django.urls import path,include
from sre import views
urlpatterns = [
    path('',views.index,name='Homepage')


]
