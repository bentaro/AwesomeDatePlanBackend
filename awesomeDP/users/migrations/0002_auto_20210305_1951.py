# Generated by Django 3.1.7 on 2021-03-05 19:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('7d4cb8dc-ed2a-45fd-9fec-f07e12b86ee9'), editable=False, primary_key=True, serialize=False),
        ),
    ]