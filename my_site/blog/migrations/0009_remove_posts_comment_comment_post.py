# Generated by Django 5.0.6 on 2024-06-11 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_posts_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.posts'),
        ),
    ]
