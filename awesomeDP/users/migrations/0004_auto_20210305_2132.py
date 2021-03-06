# Generated by Django 3.1.7 on 2021-03-05 21:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210305_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('105c578f-e803-4f0e-ab70-e0b2895b2bf3'), editable=False, primary_key=True, serialize=False),
        ),
    ]