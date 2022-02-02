
from django.urls import path
from django.contrib.auth.views import *
from django.conf.urls import include
from . import views
urlpatterns = [
    # path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', LoginView.as_view(), name='profile'),
    path('accounts/profile/', include('service.urls')),



    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordResetDoneView.as_view(), name='password_change_done'),

    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]