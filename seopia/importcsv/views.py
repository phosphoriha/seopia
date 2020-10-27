from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings

# Create your views here.


def panel(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return render(request, 'panel.html')
