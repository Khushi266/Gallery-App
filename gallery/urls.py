from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('ticket/', views.ticket, name='ticket'),
    path('event/', views.event, name='event'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('home/', views.gallery_home, name='gallery_home'),
    path('artwork/<int:pk>/', views.artwork_detail, name='artwork_detail'),
    # path('artwork/<int:pk>/bid/', views.place_bid, name='place_bid'),
    path('login/', auth_views.LoginView.as_view(template_name='gallery/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='gallery/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('payment/<int:art_id>/', views.payment_page, name='payment_page'),
    path('payment-success/<int:art_id>/', views.payment_success, name='payment_success'),
]
