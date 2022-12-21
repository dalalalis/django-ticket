from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Webpage import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('sign_up/', views.user_register, name='sign_up'),
    path('log_in/', views.user_login, name='log_in'),
    path('log_out/', views.logout_view, name='log_out'),
    path('tickts/', views.ticket_add, name='tickts_page'),
    path('dashboard/',views.create_ticket, name="create_ticket"),
    path('profile/',views.prfile_page, name="profile_page"),
    path('tickts/views',views.ticket_view, name="ticket_view_page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)