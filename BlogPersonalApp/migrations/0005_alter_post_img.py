# Generated by Django 4.1.3 on 2023-01-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPersonalApp', '0004_alter_post_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.URLField(),
        ),
    ]
