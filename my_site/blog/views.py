
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from .models import Posts, Comment

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView


 

posts = Posts.objects.all()



def index(request):
    latest_posts = posts.order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


# class StartingPageView(ListView):
#     template_name = "blog/index.html"
#     model = Posts
#     ordering = ["-date"]
#     contex_object_name = "posts"


#     def get_queryset(self):
#         querySet = super().get_queryset()
#         data = querySet[:3]
#         return data
    

def all_posts(request):
    try:
        return render(request, "blog/all_posts.html", {"posts": posts})

    except:
        raise Http404()
    
# class AllPostsView(ListView):
#     template_name = "blog/all_posts.html"
#     model = Posts
#     ordering = ["-date"]
#     contex_object_name = "posts"

    



class SinglePostView(View):

    def is_stored_post(self, request, post_id): 
        stored_posts = request.session.get("stored_posts")
        
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later


    def get(self, request, slug):
        post = Posts.objects.get(slug=slug)


        context = {
            "post": post,
            "tags": post.tag.all(),
            "form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/single_post.html", context)
    
    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Posts.objects.get(slug=slug)

        if form.is_valid():
            comment =form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("detailed_post", args=[slug]))

        context = {
            "post": post,
            "tags": post.tag.all(),
            "form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/single_post.html", context)
        


class ReadLater(View):
    def get(self, request):
        read_later_posts = request.session.get("stored_posts")
        context = {}
        if read_later_posts is None or len(read_later_posts) == 0:
            context["posts"] = []
            context["has_post"] = False
        else:
            posts  = Posts.objects.filter(id__in=read_later_posts)
            context["posts"] = posts
            context["has_post"] = True
        return render(request, "blog/stored_list.html", context)
    
    def post(self, request):
        read_later_posts = request.session.get("stored_posts")
        post_id = int(request.POST["post_id"])

        if read_later_posts is None:
            read_later_posts = []
        
        if post_id not in read_later_posts:
            read_later_posts.append(post_id)

        else:
            read_later_posts.remove(post_id)
        
        request.session["stored_posts"] = read_later_posts

        return HttpResponseRedirect("/")