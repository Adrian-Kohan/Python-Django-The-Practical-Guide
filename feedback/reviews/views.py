from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .models import Review


# Create your views here.
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {"form":form})

#     def post(self, request):
#             form = ReviewForm(request.POST)

#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect("thank-you")
            
#             return render(request, "reviews/review.html", {"form":form})

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
    

# with using this one we don't need to build a form.py because it will do this for us then it will save new entry to the databaase
# so if we don't have any predefined form then we don't need to refer to it (from_class will be emited).

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    
        

class ThankyouView(TemplateView):
    template_name = "reviews/thank-you.html"
    
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs) 
         context["message"] = "This works!"
         return context
    

class ReviewListView(ListView):
    template_name = "reviews/reviews_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #      query =  super().get_queryset()
    #      data = query.filter(rating__gt=4)
    #      return data
    
    
    
# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"
    
#     def get_context_data(self, **kwargs):
#          context = super().get_context_data(**kwargs) 
#          review_id = kwargs["id"]
#          selected_review = Review.objects.get(pk=review_id)
#          context["review"] = selected_review
#          return context
    
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        contex =  super().get_context_data(**kwargs)
        loaded_review  = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        contex["is_fav"] = loaded_review.id == favorite_id
        return contex


class AddFavorite(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = int(review_id)
        return HttpResponseRedirect(f"/reviews/{review_id}")
