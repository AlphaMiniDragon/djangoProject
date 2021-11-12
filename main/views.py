from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
# Create your views here. 
recipe = Recipe.objects.all()
def index (request):
    return render(request, 'main/Main.html',{'recipe':recipe})

def about(request):
    return render(request, 'main/About_us.html')
def account(request):
    return render(request, 'main/Accounts.html')
def contact(request):
    return render(request, 'main/Contacts.html')
def login(request):
    return render(request, 'main/Log_in.html')
def recipes(request):
    return render(request,'main/Recipes.html',{'recipe':recipe})
def signUp(request):
    return render(request,'main/Sign_up.html')
def tempuraRecipes(request):
    return render(request, 'main/Tempura_Recipe.html')

def profile(request):
    return render(request, 'main/profile.html')
