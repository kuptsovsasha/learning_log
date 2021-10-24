from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """register new user"""
    if request.method != 'POST':
        #show empty registration form
        form = UserCreationForm()
    else:
        #process the completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #authorizate new user and put him on main page
            login(request, new_user)
            return redirect('learning_logs:index')
    #show empty or not valid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)