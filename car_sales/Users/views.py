from django.shortcuts import render, redirect
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import SignupFrom,UpdateUserForm
from orders.models import Order



class UserSignUpView(CreateView):
    form_class = SignupFrom
    template_name = 'signup.html'
    def get_success_url(self):
        return reverse_lazy('login')
    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Signup'
        return context
    
class UserLoginView(LoginView):
    template_name = 'signup.html'
    def get_success_url(self):
        return reverse_lazy('homepage')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    

def profile(request):
    user_orders = Order.objects.filter(user=request.user)
    return render(request, 'profile.html', {'orders': user_orders})

class edit_profile(UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'edit_profile.html'
    success_url =reverse_lazy('profile')
    def get_object(self, queryset=None):
        return self.request.user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Update Profile'
        return context
    
class PasswordChange(PasswordChangeView):
    template_name = 'pass_change.html'
    success_url = reverse_lazy('profile') 

class UserLogout(LogoutView):
    next_page = reverse_lazy('homepage') 