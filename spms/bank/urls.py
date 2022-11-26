from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login),
    path('dashboard/', views.dashboard),
    path('new/',views.createQuestion,name="create_Question"),
    path('bank/', views.bank),
    
]
