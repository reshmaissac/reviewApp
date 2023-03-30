from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm


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
    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            # log user in
            messages.success(request, 'You have successfully logged in.')
            return redirect('home-home')

        else:
            messages.error(request, "Invalid username or password.")

    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'users/login.html', context)

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


