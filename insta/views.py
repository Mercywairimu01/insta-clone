from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Post,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def index(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'index.html',context)

def register(request):
    if request.user.is_authenticated:
        raise Http404
    else:
        if request.method == 'POST':
            form =UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username =form.cleaned_data.get('username')
                messages.success(request,f'Account created.Please login!')
                return redirect('login')
        else:
            form =UserRegisterForm()    
        
        return render(request,'users/register.html',{'form':form })

@login_required
def profile(request):
  
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)



class PostListView(ListView):
    model = Post
    template_name = 'index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    success_url = '/'
    fields = ['image','name', 'caption','likes']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['image','name', 'caption']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
@login_required
def SearchResults(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        user_id = User.objects.get(username=search_term)
        searched_profile = Profile.search_by_profile(user_id.id)
        message = f"{search_term}"
        print(searched_profile)
        posts = Post.objects.filter()
        return render(request, 'search.html', {"message": message, "profile": searched_profile,'posts':posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message })

