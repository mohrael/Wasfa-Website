from django.shortcuts import render,redirect, get_object_or_404
from .models import user, Recipe
from django.contrib import messages  
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password



def homepage(request):
    return render(request,'parts/HomePage.html')

def userhomepage(request):
    return render(request,'parts/userhomepage.html')

def adminhomepage(request):
    return render(request,'parts/adminhomepage.html')

def aboutadmin(request):
    return render(request,'parts/aboutadmin.html')

def aboutuser(request):
    return render(request,'parts/aboutuser.html')

def allrecipes_notlogged(request):
    recipes = Recipe.objects.all()
    return render(request,'parts/allrecipes-notlogged.html', {'recipes': recipes})

def allrecipes_logged(request):
    recipes = Recipe.objects.all()
    return render(request,'parts/allrecipes-logged.html', {'recipes': recipes})

def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, 'parts/recipe_detail.html', {'recipe': recipe})

def mealoftheday(request):
    return render(request,'parts/Meal_of_the_day.html')

def about(request):
    return render(request,'parts/about.html')


def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password=request.POST.get('confirmPassword')
        username = request.POST.get('username')
        is_admin = request.POST.get('is_admin') == 'on'

        if not all([email, password, username, confirm_password]):
            messages.error(request, "All fields are required.")
            return render(request, 'parts/register.html')

        if user.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken.")
            return render(request, 'parts/register.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'parts/register.html')
        
        hashed_password = make_password(password)
        data = user(email=email, password=hashed_password, is_admin=is_admin, username=username)
        data.save()
   
        return redirect('/login.html')  

    return render(request, 'parts/register.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email or not password:
            messages.error(request, "Both email and password are required.")
            return render(request, 'parts/login.html')

        try:
            user_instance = user.objects.get(email=email)
        except user.DoesNotExist:
            user_instance = None

        if user_instance is None or not check_password(password, user_instance.password):
            messages.error(request, "Invalid email or password.")
            return render(request, 'parts/login.html')

        if user_instance.is_admin:
            return redirect('/adminhomepage.html')
        else:
            return redirect('/userhomepage.html')

    return render(request, 'parts/login.html')