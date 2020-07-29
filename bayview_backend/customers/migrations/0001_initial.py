# Generated by Django 3.0.4 on 2020-03-16 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
