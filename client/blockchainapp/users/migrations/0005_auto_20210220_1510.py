# Generated by Django 3.1.7 on 2021-02-20 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_public_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures'),
        ),
    ]