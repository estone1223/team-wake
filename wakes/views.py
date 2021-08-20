from accounts.models import Wake
from django.shortcuts import render

# Create your views here.

def top(request):
    wakes = Wake.objects.all()
    context = {
      'wakes': wakes,
    }
    return render(request, 'wakes/top.html', context)