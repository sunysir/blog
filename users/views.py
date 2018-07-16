from django.shortcuts import render

# Create your views here.
from users.forms import UserForm


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    return render(request, 'users/register.html', context={'form': form})


