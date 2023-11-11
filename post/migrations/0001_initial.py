# Generated by Django 4.2.7 on 2023-11-11 21:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('b6175934-61df-4cf0-ba8d-c106ff7274a8'), primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
