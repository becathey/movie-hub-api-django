# Generated by Django 4.2.7 on 2023-11-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('image', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=800)),
                ('genre', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
            ],
            options={
                'ordering': ['rating'],
            },
        ),
    ]
