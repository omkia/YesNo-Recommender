from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'advisor'
urlpatterns = [
    path('', views.home, name='home'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('gifts/', views.gift_advisor, name='gifts'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('about/', views.about, name='about'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),

    path('logout/', LogoutView.as_view(next_page='advisor:home'), name='logout'),
]