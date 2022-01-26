from django.urls import reverse
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
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)

    else:
        init_values = {}
        if request.user.is_authenticated:
            init_values['author'] = request.user
        init_values['created_on'] = datetime.datetime.now()
        form = BlogPostForm(initial=init_values)
    return render(request, 'blog/blog_create.html', {'form': form})


# class UpdatePost(UpdateView):
#     model = BlogPost
#     template_name = 'blog/blog_edit.html'
#     form_class = BlogPostForm
#
#     def get_success_url(self):
#         return reverse('blog:none_published')

def updatePost(request, pk):
    post = BlogPost.objects.get(id=pk)

    init_values = {}

    init_values['title'] = post.title
    init_values['author'] = post.author
    init_values['last_updated'] = post.last_updated
    init_values['created_on'] = post.created_on
    init_values['published'] = post.published
    init_values['content'] = post.content

    form = BlogPostForm(initial=init_values)

    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        form.published = False
        if form.is_valid():
            form.save()
            post.delete()
            return HttpResponseRedirect(reverse('blog:none_published'))
    return render(request, 'blog/blog_edit.html', {'form': form})


def deletePost(request, pk):
    post = BlogPost.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect(reverse('blog:blog_list'))
    return render(request, 'blog/blog_delete.html', {'post': post})


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

