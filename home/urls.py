from django.urls import path,include
from . import views

urlpatterns = [
    path('sign_in/', views.render1 )
]
