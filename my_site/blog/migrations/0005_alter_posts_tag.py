# Generated by Django 5.0.6 on 2024-06-03 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_posts_author_alter_posts_date_alter_posts_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='tag',
            field=models.ManyToManyField(to='blog.tag'),
        ),
    ]
