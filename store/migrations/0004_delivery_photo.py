# Generated by Django 4.2 on 2023-07-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_about_usphoto_dostavkaphoto_spivrobitnictvophoto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery_photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='delivery_photo')),
            ],
        ),
    ]
