from django.urls import path
from .import views

urlpatterns = [
   
    path('',views.num,name='home'),
    path('article/<int:id>',views.next ,name='nextpage'),
    path('article/<int:id>/song_file',views.recodr ,name='page'),
    path('cont',views.contact_us,name="con"),
    path('about',views.about_us,name="abt"),
    path('help',views.solution,name='help')

    
]