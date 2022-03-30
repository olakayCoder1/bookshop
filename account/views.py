from django.contrib import messages
from django.shortcuts import render , redirect
from .forms import CustomUserCreationForm
# Create your views here.






def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'YOUR ACCOUNT HAS BEEN CREATED. YOU CAN NOW LOGIN')
            return redirect('/account/login/')
        print(form.errors)
    return render(request, 'account/register.html', {'form':form})