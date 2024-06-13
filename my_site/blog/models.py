from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator


# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name_plural = "tags"
    

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural =  "authors"




class Posts(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    summery = models.CharField(max_length=300)
    text = models.TextField(validators=[MinLengthValidator(10)])
    image = models.ImageField(upload_to ='posts', null=True)
    slug = models.SlugField(db_index=True, unique=True)
    tag = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("detailed_post", args=[self.slug])
    
    def __str__(self):
        return f"{self.title} (by {self.author})"
    
    class Meta:
        verbose_name_plural = "posts"


class Comment(models.Model):
    username = models.CharField(max_length = 100)
    comment_text = models.TextField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.comment_text} (by {self.username})"