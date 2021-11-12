from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about', views.about, name='about'),
    path('account', views.account,name='account'),
    path('contact', views.contact,name='contacts'),
    path('login', views.login,name='login'),
    path('recipes', views.recipes,name='recipes'),
    path('signUP', views.signUp,name='signup'),
    path('tempuraRecipes', views.tempuraRecipes,name='tempuraRecipe'),
    path('profile',views.profile,name='profile')
]