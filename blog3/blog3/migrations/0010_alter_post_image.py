# Generated by Django 4.0 on 2021-12-30 20:43

import blog3.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog3', '0009_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blog3.models.user_directory_path),
        ),
    ]
