# Generated by Django 3.1.7 on 2021-03-05 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('spot_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=132)),
                ('picture', models.URLField()),
                ('detail_url', models.URLField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'db_table': 'spot',
            },
        ),
    ]
