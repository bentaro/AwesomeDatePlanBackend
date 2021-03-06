# Generated by Django 3.1.7 on 2021-03-05 21:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210305_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('bf14bc8e-17c3-4755-8c22-e0e87151d042'), editable=False, primary_key=True, serialize=False),
        ),
    ]
