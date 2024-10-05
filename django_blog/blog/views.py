from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm, ProfileForm  
from .models import Profile


# Home view - For the home page after login or for general use
def home(request):
    return render(request, 'home.html')

    
# Registration view
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to a home page or other desired page
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

# Custom Login view if you need to customize the Login process further
class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

# Custom Logout view if needed
class CustomLogoutView(LogoutView):
    template_name = 'logged_out.html'

# Profile view for viewing and editing user profiles
@login_required  # Ensure only logged-in users can access this view
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect back to the profile page
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})