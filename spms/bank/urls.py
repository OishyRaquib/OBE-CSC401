from django.urls import path
from . import views

urlpatterns = [
    
    path('dashboard/', views.dashboard, name="dashboard"),
    path('new/',views.createQuestion,name="create_Question"),
    path('bank/', views.bank),
    path('', views.Login),
    path('signout', views.signout),
]
