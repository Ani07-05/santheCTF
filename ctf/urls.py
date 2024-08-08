from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('challenge/<int:pk>/', views.challenge_detail, name='challenge_detail'),
    path('submission_result/<int:pk>/', views.submission_result, name='submission_result'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('leaderboard/data/', views.leaderboard_data, name='leaderboard_data'),
]
