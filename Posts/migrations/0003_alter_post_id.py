# Generated by Django 5.1.4 on 2025-01-03 07:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_alter_post_cover_image_alter_post_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('83598894-88b3-485f-8a66-3aa8599bd68c'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]