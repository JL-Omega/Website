from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import BlogPost
from .forms import BlogPostForm
import datetime


class ListPost(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog/blog_list.html'


class DetailPost(DetailView):
    model = BlogPost
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'


def CreatePost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        post = BlogPost.objects.all()
        print(post)
        # if form.is_valid():
        #     form.save()
        # return HttpResponseRedirect(request.path)

    else:
        init_values = {}
        if request.user.is_authenticated:
            init_values['author'] = request.user
        init_values['created_on'] = datetime.datetime.now()
        form = BlogPostForm(initial=init_values)
    return render(request, 'blog/blog_create.html', {'form': form})


class UpdatePost(UpdateView):
    pass


class DeletePost(DeleteView):
    pass


class NonePublished(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog/none_published.html'


class Published(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog/published.html'


# def detailView(request, id):
#     post = BlogPost.objects.get(id=id)
#     return render(request, 'blog/blog_detail.html', {'post': post})


def publish(request, id):
    posts = BlogPost.objects.all()
    post = BlogPost.objects.get(id=id)
    post.published = True
    post.created_on = datetime.datetime.now()
    post.save()
    return render(request, 'blog/none_published.html', {'posts': posts})


def unpublish(request, id):
    posts = BlogPost.objects.all()
    post = BlogPost.objects.get(id=id)
    post.published = False
    post.save()
    return render(request, 'blog/published.html', {'posts': posts})

