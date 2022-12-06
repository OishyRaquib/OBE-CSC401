from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user,name="login"),
    path('signout', views.signout, name="Signout"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('home/<str:pk_stu>/', views.studash,name="stud_dashboard"),
    #Question Bank:
    path('new/',views.createQuestion,name="create_Question"),
    path('drafts/', views.drafts,name="drafts_"),
    path('show/<question_id>', views.showQuestion,name="show_Question"),
    path('update_question/<question_id>',views.updateQuestion,name="update_Question"),
    path('delete/<question_id>', views.deleteQuestion,name="delete_Question"),
    path('pdf/', views.question_pdf,name="question_pdf"),
    # path('qpdf/<question_id>', views.ques_pdf,name="ques_pdf")

    #Course Outline:
    path('newOutline/', views.createCourseOutline, name="create_courseOutline"),
    path('outlineDrafts/', views.drafts_outline,name="drafts_Outline"),
    # path('view/<outline_id>', views.viewOutline,name="view_outline"),
    path('remove/<outline_id>', views.deleteOutline,name="delete_outline"),
    path('status/', views.showStatus,name="show_Status"),
    path('browse/', views.browseOutline, name="browseOutline"),
    path('edit/<courseOutline_id>/', views.editCourseOutline, name="edit_courseOutline"),
    path('pdf_co/', views.outlines_pdf,name="outlines_pdf")
]
