from django import forms
from django.http.response import HttpResponseForbidden
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
    return render(request, 'wakes/wake_new.html', {'form': form})

@login_required
def wake_edit(request, wake_id):
    wake = get_object_or_404(Wake, pk=wake_id)
    if wake.created_by.id != request.user.id:
        return HttpResponseForbidden('このWakeの編集は許可されていません')
    
    if request.method == 'POST':
        form = WakeForm(request.POST, instance=wake)
        if form.is_valid():
            form.save()
            return redirect('wake_detail', wake_id=wake_id)
    else:
        form = WakeForm(instance=wake)
    return render(request, 'wakes/wake_edit.html', {'form': form})

@login_required
def wake_detail(request, wake_id):
    wake = get_object_or_404(Wake, pk=wake_id)
    if wake.created_by.id != request.user.id:
        return HttpResponseForbidden('このWakeの閲覧は許可されていません')
    context= {
        'wake': wake,
    }

    return render(request, 'wakes/wake_detail.html', context)