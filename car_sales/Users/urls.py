from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.UserLogout.as_view(),name='logout'),
    path('edit_profile/',views.edit_profile.as_view(),name='edit_profile'),
    path('pass_change',views.PasswordChange.as_view(),name='pass_change'),
    
]