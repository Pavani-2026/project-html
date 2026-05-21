from django.shortcuts import render
from userapp.models import Users
from userapp.forms import UserForm

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'success.html')

    else:
        form = UserForm()

    return render(request, 'userreg.html', {'form': form})