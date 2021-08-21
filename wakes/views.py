from wakes.form import WakeForm
from wakes.models import Wake
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.

def top(request):
    wakes = Wake.objects.all()
    context = {
        'wakes': wakes,
    }
    return render(request, 'wakes/top.html', context)


@login_required
def wake_new(request):
    if request.method == 'POST':
        form = WakeForm(request.POST)
        if form.is_valid():
            wake = form.save(commit=False)
            wake.created_by = request.user
            wake.save()
            return redirect(top)
    else:
        form = WakeForm()
    return render(request, 'wakes/wakes_new.html', {'form': form})
