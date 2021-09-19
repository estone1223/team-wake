from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http.response import HttpResponseForbidden
from wakes.form import MemberForm
from wakes.models import Member
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# member用View

# member一覧用View
@login_required
def member(request):
    user_id = request.user.id
    members = Member.objects.filter(created_by_id=user_id)
    members = members.order_by('name')
    context= {
        'members': members,
    }

    return render(request, 'member/member.html', context)


# フォームページ用View
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


# 実行用View
@login_required
def member_new(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.created_by = request.user
            member.save()
            return redirect(request.META.get('HTTP_REFERER'))
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
            return redirect('member:member_edit_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'member/member_edit.html', {'form': form})



@login_required
def member_delete(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if member.created_by.id != request.user.id:
        return HttpResponseForbidden('このMemberの削除は許可されていません')
    
    member.delete()
    
    return redirect('member:member_delete_list')
