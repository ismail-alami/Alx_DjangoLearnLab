from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm, ProfileForm  
from .models import Profile
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

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
                  
# ListView - Display all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # Template for displaying the list
    context_object_name = 'posts'  # Context variable used in the template

# DetailView - Display an individual blog post
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

# CreateView - Allow users to create new posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']  # Only show title and content fields in the form
    template_name = 'post_form.html'

    # Automatically assign the logged-in user as the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# UpdateView - Allow post authors to edit their own posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Ensure only the post author can edit the post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# DeleteView - Allow post authors to delete their own posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('blog:post-list')

    # Ensure only the post author can delete the post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author