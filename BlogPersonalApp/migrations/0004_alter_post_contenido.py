# Generated by Django 4.1.3 on 2023-01-19 17:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPersonalApp', '0003_post_delete_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
