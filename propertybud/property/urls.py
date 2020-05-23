from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('careers/', views.careers, name='careers'),
    path('advertiseWithUs/', views.advertise, name='ads'),
    path('affiliateProgramme/', views.affiliate, name='affiliate'),
    path('terms&Conditions/', views.t_and_c, name='t&c'),
    path('privacyPolicy/', views.policy, name='policy'),
    path('feedback/', views.feedback, name='feedback'),
    path('agents/find/', views.agents, name='agents'),
    path('about/', views.about, name='about'),
    path('faq/', views.faqs, name='faqs'),
    path('<str:pk>/', views.profile, name='profile'),
    path('<str:pk>/dashboard/', views.dashboard, name='dashboard'),
    path('<str:pk>/favorites/', views.favorites, name='favorites'),
    path('<str:pk>/messages/', views.msg, name='msg'),
    path('<str:pk>/notifications/', views.notifications, name='notifications'),
    path('<str:pk>/listing/new/', views.list_property, name='listing'),
]
