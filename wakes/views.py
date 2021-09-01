from django import forms
from django.http.response import HttpResponseForbidden
from wakes.form import WakeForm, MemberForm
from wakes.models import Member, Wake
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.

def top(request):
    wakes = Wake.objects.all().order_by('-id')
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
    user_id = request.user.id
    wake = get_object_or_404(Wake, pk=wake_id)
    members = Member.objects.filter(created_by_id=user_id)
    members = members.order_by('name')
    if wake.created_by.id != request.user.id:
        return HttpResponseForbidden('このWakeの閲覧は許可されていません')
    context= {
        'wake': wake,
        'members': members
    }

    return render(request, 'wakes/wake_detail.html', context)

def wake_classic(request):
    return render(request, 'wakes/wake_classic.html')

@login_required
def wake_delete(request, wake_id):
    wake = get_object_or_404(Member, pk=wake_id)
    if wake.created_by.id != request.user.id:
        return HttpResponseForbidden('このWakeの削除は許可されていません')
    
    wake.delete()
    
    return redirect('top')

@login_required
def member(request):
    user_id = request.user.id
    members = Member.objects.filter(created_by_id=user_id)
    members = members.order_by('name')
    context= {
        'members': members,
    }

    return render(request, 'member/member.html', context)

@login_required
def member_new_list(request):
    form = MemberForm()
    user_id = request.user.id
    members = Member.objects.filter(created_by_id=user_id)
    members = members.order_by('name')
    context= {
        'members': members,
        'form': form,
    }

    return render(request, 'member/member_new_list.html', context)

@login_required
def member_edit_list(request):
    user_id = request.user.id
    members = Member.objects.filter(created_by_id=user_id)
    members = members.order_by('name')
    context= {
        'members': members,
    }

    return render(request, 'member/member_edit_list.html', context)

@login_required
def member_delete_list(request):
    user_id = request.user.id
    members = Member.objects.filter(created_by_id=user_id)
    members = members.order_by('name')
    context= {
        'members': members,
    }

    return render(request, 'member/member_delete_list.html', context)

@login_required
def member_new(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.created_by = request.user
            member.save()
            return redirect('member_new_list')
    else:
        return HttpResponseForbidden('正規の手続きを踏んでください')



@login_required
def member_edit(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if member.created_by.id != request.user.id:
        return HttpResponseForbidden('このMemberの編集は許可されていません')
    
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_edit_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'member/member_edit.html', {'form': form})



@login_required
def member_delete(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if member.created_by.id != request.user.id:
        return HttpResponseForbidden('このMemberの削除は許可されていません')
    
    member.delete()
    
    return redirect('member_delete_list')


