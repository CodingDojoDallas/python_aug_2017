# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 20:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books_authors',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='book_authors.Authors'),
        ),
        migrations.AlterField(
            model_name='books_authors',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book_authors.Books'),
        ),
    ]
