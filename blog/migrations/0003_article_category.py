# Generated by Django 3.0.8 on 2020-07-29 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200729_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blog.Category', verbose_name='دسته\u200cبندی'),
        ),
    ]