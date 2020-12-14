# Generated by Django 3.0.7 on 2020-08-15 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_homeslide'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeslide',
            name='caption',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='homeslide',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
