from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name="login"),
    path('dashboard/', views.dashboard,name="dashboard"),

    path('home/<str:pk_stu>/', views.studash,name="stud_dashboard"),

    #Question Bank:
    path('new/',views.createQuestion,name="create_Question"),
    path('drafts/', views.drafts,name="drafts_"),
    path('show/<question_id>', views.showQuestion,name="show_Question"),
    path('update_question/<question_id>',views.updateQuestion,name="update_Question"),
    path('delete/<question_id>', views.deleteQuestion,name="delete_Question")
    
]
