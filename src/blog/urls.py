from django.contrib.auth.decorators import login_required
from django.urls import path
from .import views

app_name = 'blog'
urlpatterns = [
    path('blog_list/', login_required(views.ListPost.as_view()), name='blog_list'),
    path('blog_detail_<str:pk>/', login_required(views.DetailPost.as_view()), name='blog_detail'),
    path('publish_<str:id>/', login_required(views.publish), name='publish'),
    path('unpublish_<str:id>/', login_required(views.unpublish), name='unpublish'),
    path('none_published/', login_required(views.NonePublished.as_view()), name='none_published'),
    path('published/', login_required(views.Published.as_view()), name='published'),
    path('blog_create/', login_required(views.CreatePost), name='blog_create'),
    path('blog_edit_<str:pk>/', login_required(views.updatePost), name='blog_edit'),
    path('blog_delete_<str:pk>/', login_required(views.deletePost), name='blog_delete'),
]