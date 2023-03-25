from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CustomAuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        


        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! Now you can login!')           
            return redirect('login')
        else:
            messages.warning(request, 'Invalid input')

            return redirect('home-home')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form, 'title': 'Register'})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been successfully updated')

        return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }

        return render(request, 'users/profile.html', context)

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                

                login(request, user)
                messages.success(request, f'Welcome {username}!')
                return redirect('home-home')
            else:
                messages.warning(request, 'Invalid username or password')
                return redirect('login')
    else:
        form = CustomAuthenticationForm()
    form.helper = FormHelper()
    form.helper.form_method = 'post'
    form.helper.add_input(Submit('submit', 'Login', css_class='btn-primary'))
    return render(request, 'users/login.html', {'form': form, 'title': 'Sign In'})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')
