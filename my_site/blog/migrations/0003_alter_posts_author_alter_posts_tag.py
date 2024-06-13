# Generated by Django 5.0.6 on 2024-06-02 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_tag_alter_posts_options_alter_posts_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.author'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='tag',
            field=models.ManyToManyField(null=True, to='blog.tag'),
        ),
    ]
