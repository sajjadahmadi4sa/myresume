from django.urls import path
from pages.views import *

urlpatterns = [
    path('',home_view,name='home'),
    path('about/',about_view,name='about'),
    path('resume/',resume_view,name='resume'),
    path('portfolio/',portfolio_view,name='portfolio'),
    path('contact/',contact_view,name='contact'),
]
