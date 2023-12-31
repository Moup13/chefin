# Generated by Django 4.2 on 2023-07-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_carouselphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_usPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_us_photo')),
            ],
        ),
        migrations.CreateModel(
            name='DostavkaPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='dostavka_photos')),
            ],
        ),
        migrations.CreateModel(
            name='SpivrobitnictvoPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='spivrobitnictvo_photo')),
            ],
        ),
        migrations.CreateModel(
            name='VakansiiPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='vakansii_photo')),
            ],
        ),
    ]
