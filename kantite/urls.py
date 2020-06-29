
from django.urls import path
from kantite import views

urlpatterns = [
    path('',views.home, name='home' ),
    path('chile',views.chile, name='chile' ),
    path('about',views.about, name='about' ),
]