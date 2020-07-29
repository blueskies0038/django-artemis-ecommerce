# Generated by Django 3.0.7 on 2020-07-29 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('credit', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aesthetic.Collection')),
            ],
        ),
    ]
