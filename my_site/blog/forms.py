from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        exclude = ["post"]

        labels = {
            "username" : "Your Name",
            "comment_text" : "Your Comment",
        }

        error_messages = {
            "user_name" : {
                "required" : "Your name must not be empty!",
                "max_length" : "Please enter a shorter name!"
            }
        }