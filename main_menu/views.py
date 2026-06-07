from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CommentForm, MemForm, CustomUserCreationForm
from .models import Mem, Like, User, Subscribes

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def main_menu(request):
    all_mems = Mem.objects.all()
    context = {'mems': all_mems}
    return render(request, 'main_menu/main_menu.html', context)

def contacts_view(request):
    return render(request, 'main_menu/contacts.html')

def profile(request, username):
    try:
        likes_obj = Like.objects.filter(author=request.user)
    except:
        likes_obj = None
    profile_user = get_object_or_404(User, username=username)
    all_mems = Mem.objects.filter(author_name=username).distinct()
    context = {
        'request': request,
        'own_user': profile_user,
        'mems': all_mems,
        'liked_mems': likes_obj
    }
    return render(request, 'profile.html', context)

def add_photo(request):
    if request.method == 'POST':
        form = MemForm(request.POST, request.FILES)
        if form.is_valid():
            new_mem = form.save(commit=False)
            new_mem.author_name = request.user.username
            new_mem.save()
            return redirect('main_menu')

    form = MemForm()
    context = {'form': form}
    return render(request, 'add_photo.html', context)

def mem_view(request, mem_id):
    mem = get_object_or_404(Mem, id=mem_id)
    comments = mem.comment_set.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.mem = mem
            new_comment.author_name = request.user.username
            new_comment.save()
            return redirect('mem_detail', mem_id=mem_id)

    form = CommentForm()
    context = {
        "mem": mem,
        'userZ': request.user.username,
        'comments': comments,
        'form': form,
    }
    return render(request, 'mem_visitka.html', context)

@login_required(login_url='login')
def like_mem(request, mem_id):
    mem = get_object_or_404(Mem, id=mem_id)
    like_obj = Like.objects.filter(mem=mem, author=request.user).first()

    if like_obj:
        like_obj.delete()
    else:
        Like.objects.create(mem=mem, author=request.user)

    return redirect(request.META.get('HTTP_REFERER', 'main_page'))

@login_required(login_url='login')
def sub_suber(request, sub_username):
    sub = get_object_or_404(User, username=sub_username)
    sub_obj = Subscribes.objects.filter(sub=sub, suber=request.username).first()

    if sub_obj:
        sub_obj.delete()
    else:
        Subscribes.objects.create(sub=sub, suber=request.user)

    return redirect(request.META.get('HTTP_REFERER', 'main_page'))

@login_required(login_url='login')
def delete_mem(request, mem_id):
    mem = get_object_or_404(Mem, id=mem_id)
    if request.user.username == mem.author_name or request.user.is_superuser:
        mem.delete()
    return redirect('profile', username=request.user.username)