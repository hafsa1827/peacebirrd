from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'peacebird-home'),
    path('enrollment/', views.enrollment, name= 'peacebird-enrollment'),
    path('contact_us/', views.contact_us, name='success'),
]
