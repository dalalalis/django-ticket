
from django.urls import path


from . import views

urlpatterns = [
    path('sign_up/', views.user_register, name='sign_up'),
    path('log_in/', views.user_login, name='log_in'),
    path('log_out/', views.logout_view, name='log_out'),

]
