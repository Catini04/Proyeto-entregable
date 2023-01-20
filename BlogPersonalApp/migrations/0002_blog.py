# Generated by Django 4.1.3 on 2023-01-19 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPersonalApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=200)),
                ('cuerpo', models.CharField(max_length=4000)),
                ('autor', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]