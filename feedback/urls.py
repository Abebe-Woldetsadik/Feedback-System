from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . views import feedback, teacher_feedback, director_feedback

app_name = 'feedback'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', feedback, name='feedback'),
    path('teacher_feedback/', teacher_feedback, name='teacher_feedback'),
    path('director_feedback/', director_feedback, name='director_feedback'),
]
